from telebot.apihelper import ApiTelegramException
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from configs import bot


@bot.message_handler(commands=['start'])
def cmd_start(message: Message):
    try:
        keyboard = InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            InlineKeyboardButton("💨 Одноразки", callback_data="cat|disposables"),
            InlineKeyboardButton("🧃 Жидкости", callback_data="cat|liquids"),
            InlineKeyboardButton("🔋 Картриджи", callback_data="cat|cartridges")
        )

        text = (
            "Добро пожаловать в PGSMOKE!\n\n"
            "Здесь ты можешь быстро оформить заказ.\n\n"
            "📋 Меню:\n"
            "— Найти товар\n"
            "— Акции\n"
            "— Связь с продавцом\n\n"
            "Выбирай категорию 👇"
        )

        bot.send_message(
            chat_id=message.chat.id,
            text=text,
            reply_markup=keyboard
        )

    except ApiTelegramException as e:
        print(f"[Telegram API error] {e}")

    except Exception as e:
        print(f"[Handler error] {e}")