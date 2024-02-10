from loader import bot

from telebot.types import Message


@bot.message_handler(commands=['hello_world'])
def send_welcome(message: Message):
    bot.reply_to(message, f'Привет МИР!')
