from utils.admin_state import admin_states
from configs import bot, ADMIN_ID
from telebot import types
from utils.products_db import add_product, load_products
from telebot.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from keyboards.catalog_keyboards import create_products_keyboard, create_back_keyboard

@bot.message_handler(commands=['add'])
def add_product_start(message: Message):
    if message.from_user.id != ADMIN_ID:
        bot.send_message(message.chat.id, "Нет доступа ❌")
        return

    admin_states[message.from_user.id] = {}

    state = admin_states[message.from_user.id]
    state["step"] = "category"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('disposables', "liquids", "cartridges", "snus", "pods")

    bot.send_message(
        message.chat.id,
        "Выбери категорию:",
        reply_markup=markup
    )
    bot.register_next_step_handler(message, get_category)

def get_category(message):
    admin_states[message.from_user.id]["category"] = message.text

    bot.send_message(message.chat.id, "Введи название товара")
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    admin_states[message.from_user.id]["name"] = message.text

    bot.send_message(message.chat.id, "Введите описание товара")
    bot.register_next_step_handler(message, get_describe)

def get_describe(message):
    admin_states[message.from_user.id]["describe"] = message.text

    bot.send_message(message.chat.id, "Отправь фото:")
    bot.register_next_step_handler(message, get_photo)

def get_photo(message):
    state = admin_states[message.from_user.id]

    state["photo"] = message.photo[-1].file_id


    add_product(
        state["category"],
        state["name"],
    {"describe": state["describe"],
     "photo": state["photo"]
        }
    )
    admin_states.pop(message.from_user.id, None)

    bot.send_message(message.chat.id, "Товар добавлен ✅")



def is_menu_button(call: CallbackQuery):
    return call.data.startswith('cat|')

def is_prod(call: CallbackQuery):
    return call.data.startswith('prod|')

def is_back_call(call: CallbackQuery):
    return call.data.startswith("back|")

def is_buy(call: CallbackQuery):
    return call.data.startswith("buy|")

@bot.callback_query_handler(func=is_menu_button)
def handlers_callback(call: CallbackQuery):

    bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )
    category = call.data.split("|")[1]

    bot.send_message(
        call.message.chat.id,
        "Ваша уверенность — наш приоритет. Если одноразка не проработает стандартные две недели, мы вернём вам 15% от цены в качестве компенсации, при подтверждении факта неисправности. Покупайте без лишних переживаний!\n\n"
        "Выберите товар:",
        reply_markup=create_products_keyboard(category)
    )

    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=is_prod)
def handlers_prod_callback(call: CallbackQuery):

    bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )
    parts = call.data.split("|")
    category = parts[1]
    product_name = parts[2]
    products = load_products()
    product = products.get(category, {}).get(product_name)
    if not product:
        bot.send_message(call.message.chat.id, "Товар не найден")
        return
    bot.send_photo(
        call.message.chat.id,
        product["photo"],
        caption=product["describe"],
        reply_markup=create_back_keyboard(category, product_name)
        )
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=is_back_call)
def handlers_back_call(call: CallbackQuery):

    bot.delete_message(
        call.message.chat.id,
        call.message.message_id
    )
    category = call.data.replace("back|", "")
    if category == "disposables":
        bot.send_message(
            call.message.chat.id,
            "Ваша уверенность — наш приоритет. Если одноразка не проработает стандартные две недели, мы вернём вам 15% от цены в качестве компенсации, при подтверждении факта неисправности. Покупайте без лишних переживаний!\n\n"
            "Выберите товар:",
            reply_markup=create_products_keyboard(category)
        )
        return 

    bot.send_message(
        call.message.chat.id,
        "Выберите товар:",
        reply_markup=create_products_keyboard(category)
    )

    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda call: call.data.startswith("main"))
def back_handler(call: CallbackQuery):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("💨 Одноразки", callback_data="cat|disposables"),
        InlineKeyboardButton("🧃 Жидкости", callback_data="cat|liquids"),
        InlineKeyboardButton("🔋 Картриджи", callback_data="cat|cartridges"),
        InlineKeyboardButton("🧊 Снюс", callback_data="cat|snus"),
        InlineKeyboardButton("⚡ POD-системы", callback_data="cat|pods")
    )

    bot.send_message(
        call.message.chat.id,
        "Выберите товар:",
        reply_markup=keyboard
    )
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=is_buy)
def handlers_buy_button(call: CallbackQuery):
    parts = call.data.split("|")
    category = parts[1]
    bot.delete_message(call.message.chat.id, call.message.message_id)

    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("🔙Назад",
        callback_data=f"main",
        )
    )
    bot.send_message(
        call.message.chat.id,
        "👉 Связаться: @quardey2k",
        reply_markup=keyboard
    )
    bot.answer_callback_query(call.id)
