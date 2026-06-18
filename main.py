import netwrk_fix
import time
import logging
from telebot import TeleBot

from configs import bot
import handlers.start
import handlers.catalogs

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_bot():
    while True:
        try:
            logging.info("🤖 Bot started polling...")

            bot.infinity_polling(
                timeout=30,
                long_polling_timeout=30,
                skip_pending=True,
                allowed_updates=["message", "callback_query"]
            )

        except Exception as e:
            logging.error(f"Polling crashed: {e}")
            time.sleep(5)  # restart delay

if __name__ == "__main__":
    run_bot()




