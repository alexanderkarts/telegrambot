import json
import requests
from config_data.config import API_KEY
from database.bot_database import start_find_user, name_user
from handlers.default_handlers.help import func_help
from keyboards.inline.get_city_button import get_city_button
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


def get_city(message):
    if start_find_user(message):
        try:
            city = message.text.strip().lower()
            res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
            data = json.loads(res.text)
            data_temp = data["main"]["temp"]
            bot.reply_to(message, f'Сейчас погода {data_temp}°C', reply_markup=get_city_button())
        except Exception:
            bot.reply_to(message, f'Город не найден. Попробуй еще раз')
            if message.text.startswith('/'):
                func_help(message)
            else:
                bot.register_next_step_handler(message, get_city)
    else:
        bot.reply_to(message, 'Вы не зарегестрированы\n'
                              'Команда -> /registration')


@bot.callback_query_handler(func=lambda call: True)
def process_callback_button1(call):
    bot.answer_callback_query(call.id)
    if call.data == "city_weather" or call.data == "button1":
        bot.send_message(call.from_user.id, 'Введи название города')
        bot.register_next_step_handler(call.message, get_city)
    elif call.data == "commands_bot" or call.data == "button2":
        func_help(call.message)
