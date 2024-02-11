from loader import bot
from keyboards.reply.start_button import markup
from telebot.types import Message
from handlers.default_handlers import help


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    bot.reply_to(message, f'Привет, {message.from_user.full_name}!', reply_markup=markup)


