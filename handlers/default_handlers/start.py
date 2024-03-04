from database.bot_database import start_find_user, name_user
from keyboards.inline.inline_start_btn import inline_start_btn
from keyboards.reply.start_button import start_button
from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    if start_find_user(message):
        name = name_user(message)
        bot.send_message(message.from_user.id, f'С возращением, {name}!\n', reply_markup=inline_start_btn())

    else:
        bot.reply_to(message, f'Привет, {message.from_user.username}!\n'
                              f'Этот бот умеет показвать температуру в городе\n'
                              f'Для этого зарегистрируйся\n'
                              f'Команда -> /registration', reply_markup=start_button())
