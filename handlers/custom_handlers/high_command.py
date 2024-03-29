from database.bot_database import start_find_user, name_user
from keyboards.inline.inline_high_get_city_btn import inline_high_get_city_btn
from keyboards.reply.start_button import start_button
from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['high'])
def high_get_weather(message: Message):
    print('Пришла команда high')
    if start_find_user(message):
        name = name_user(message)
        bot.send_message(message.from_user.id, f'{name}, эта команда позволит узнать максимальную погоду за 5 дней '
                                               f'каждые 3 часа\n',
                         reply_markup=inline_high_get_city_btn())

    else:
        bot.reply_to(message, f'Нужно зарегистрироваться⛔️\n'
                              f'Команда -> /registration', reply_markup=start_button())