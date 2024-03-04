from database.bot_database import start_find_user, name_user
from keyboards.inline.inline_low_get_city_btn import inline_low_get_city_btn
from keyboards.reply.start_button import start_button
from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['low'])
def low_get_weather(message: Message):
    if start_find_user(message):
        name = name_user(message)
        bot.send_message(message.from_user.id, f'{name}, эта команда позволит узнать минимальную погоду за 5 дней '
                                               f'каждые 3 часа\n',
                         reply_markup=inline_low_get_city_btn())

    else:
        bot.reply_to(message, f'Привет, {message.from_user.username}!\n'
                              f'Этот бот умеет показывать температуру в городе\n'
                              f'Для этого зарегистрируйся\n'
                              f'Команда -> /registration', reply_markup=start_button())
