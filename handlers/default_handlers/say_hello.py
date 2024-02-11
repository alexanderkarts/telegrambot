from loader import bot

from telebot.types import Message


@bot.message_handler(func=lambda message: True)
def bot_echo(message: Message):
    if message.text.lower() == "привет":
        bot.reply_to(message, f'Привет - привет!')
    # if message.text == "/hello_world":
    #     bot.reply_to(message, f'Привет МИР!')

