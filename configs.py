import os
from dotenv import load_dotenv
import telebot

load_dotenv()

BOT_TOKEN = os.getenv("bot")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing")

bot = telebot.TeleBot(
    BOT_TOKEN,
    parse_mode="HTML",
    threaded=True,
    num_threads=4
)

ADMIN_ID = 7042256454