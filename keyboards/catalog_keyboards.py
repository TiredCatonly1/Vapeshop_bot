from utils.products_db import load_products
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_products_keyboard(category):
    keyboard = InlineKeyboardMarkup(row_width=2)
    products = load_products()
    for product_name in products.get(category, {}):
        keyboard.add(
        InlineKeyboardButton(product_name, callback_data=f"prod|{category}|{product_name}")
        )
    keyboard.add(
        InlineKeyboardButton(
            "🔙 Назад",
            callback_data="main"
        )
    )

    return keyboard

def create_back_keyboard(category, product_name):

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            "💰 Купить",
            callback_data=f"buy|{category}|{product_name}",
        ),
        InlineKeyboardButton(
            "🔙 Назад",
        callback_data=f"back|{category}",
        )
    )

    return keyboard





