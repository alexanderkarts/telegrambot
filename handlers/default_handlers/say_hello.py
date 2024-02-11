from loader import bot

from telebot.types import Message


@bot.message_handler(content_types=['text'])
def bot_echo(message: Message):
    if message.text.lower() == "привет":
        bot.reply_to(message, f'Привет - привет!')

