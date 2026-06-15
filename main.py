from configs import bot
import handlers.catalogs
import handlers.start
import telebot

if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()
