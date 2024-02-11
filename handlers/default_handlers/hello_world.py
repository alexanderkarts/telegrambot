from loader import bot

from telebot.types import Message


@bot.message_handler(commands=['hello_world'])
def send_welcome(message: Message):
    bot.send_message(message.chat.id, f'Привет, МИР!')