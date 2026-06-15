import os
from dotenv import load_dotenv
import telebot

load_dotenv()

BOT_TOKEN = os.getenv("bot")

bot = telebot.TeleBot(BOT_TOKEN)
