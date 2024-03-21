import json
import requests
from telebot import types

from config_data.config import API_KEY
from database.bot_database import start_find_user
from handlers.default_handlers.help import func_help
from keyboards.inline.btn_locations_high_and_low_get_city import btn_locations_high_and_low_get_city
from loader import bot


def low_get_city(message):
    if start_find_user(message):
        try:
            city = message.text.strip().lower()
            res = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API_KEY}')
            data = json.loads(res.text)
            if data:
                bot.reply_to(message, "Выберите местоположение:", reply_markup=btn_locations_high_and_low_get_city(data))
            else:
                bot.reply_to(message, "Местоположение не найдено. Попробуйте снова.")
        except Exception as exc:
            bot.reply_to(message, f'Ошибка:', exc)
            if message.text.startswith('/'):
                func_help(message)
    else:
        bot.reply_to(message, 'Вы не зарегестрированы\n'
                              'Команда -> /registration')


def low_location_weather(message, lat, lon):
    print('Получил', lat, lon)
    res = requests.get(f' https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}'
                       f'&appid={API_KEY}&units=metric&lang=ru')
    data = json.loads(res.text)
    with open('test.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    table = "```\n"
    table += "{:^15} | {:^10} | {:^15}\n".format("Дата и время", "Мин. темп. (°C)", "Описание\n")
    for forecast in data['list']:
        date_time = forecast['dt_txt']
        min_temp = forecast['main']['temp_min']
        description = forecast['weather'][0]['description']
        table += "{:^15} | {:^10} | {:^15}\n".format(date_time, min_temp, description)
    table += "```"

    bot.send_message(message.chat.id, table, parse_mode='Markdown')
