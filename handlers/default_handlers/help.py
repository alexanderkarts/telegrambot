from loader import bot

from telebot.types import Message


@bot.message_handler(commands=['help'])
def func_help(message: Message):
    bot.reply_to(message, f'Комады бота: \n'
                          f'/start — запуск бота'
                          f'/help — помощь по командам бота\n')
