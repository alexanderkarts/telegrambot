from keyboards.reply.start_button import start_button
from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    bot.reply_to(message, f'Привет, {message.from_user.full_name}!', reply_markup=start_button())


