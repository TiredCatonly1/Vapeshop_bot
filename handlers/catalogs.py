from unicodedata import category
from configs import bot
from products import PRODUCTS, get_products
import telebot
from telebot.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.catalog_keyboards import create_products_keyboard, create_back_keyboard


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

    if call.data == "cat|disposables":
        bot.send_message(
            call.message.chat.id,
            "Ваша уверенность — наш приоритет. Если одноразка не проработает стандартные две недели, мы вернём вам 15% от цены в качестве компенсации, при подтверждении факта неисправности. Покупайте без лишних переживаний!\n\n"
            "Выберите товар:",
            reply_markup=create_products_keyboard("disposables")
        )
    if call.data == "cat|liquids":
        bot.send_message(
            call.message.chat.id,
            "Выберите товар:",
            reply_markup=create_products_keyboard("liquids")
        )
    if call.data == "cat|cartridges":
        bot.send_message(
            call.message.chat.id,
            "Выберите товар:",
            reply_markup=create_products_keyboard("cartridges")
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
    product = PRODUCTS[category][product_name]
    with open(product["photos"], "rb") as photo:
        bot.send_photo(
            call.message.chat.id,
            photo,
            caption=product["name"],
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
        InlineKeyboardButton("🔋 Картриджи", callback_data="cat|cartridges")
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
