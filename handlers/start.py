from configs import bot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@bot.message_handler(commands=['start'])
def cmd_start(message: Message) -> None:
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("💨 Одноразки", callback_data="cat|disposables"),
        InlineKeyboardButton("🧃 Жидкости", callback_data="cat|liquids"),
        InlineKeyboardButton("🔋 Картриджи", callback_data="cat|cartridges")

    )
    user_name = message.from_user.username
    text = (
        f"Добро пожаловать в PGSMOKE!\n\n"
        f"Здесь ты можешь быстро оформить заказ на электронные сигареты и жидкости.\n\n"
        f"📋 Меню бота поможет тебе:\n\n"
        f"Найти нужный товар.\n"
        f"Узнать о текущих акциях.\n"
        f"Связаться со мной.\n\n"
        f"Выбирай категорию в меню, чтобы начать."
    )

    bot.reply_to(message=message, text=text, reply_markup=keyboard)
