import json
import requests
from config_data.config import API_KEY
from database.bot_database import start_find_user
from handlers.default_handlers.help import func_help
from keyboards.inline.btn_locations_high_and_low_get_city import btn_locations_high_and_low_get_city
from loader import bot


def high_get_city(message):
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


def high_location_weather(message, lat, lon):
    print('Получил', lat, lon)
    res = requests.get(f' https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}'
                       f'&appid={API_KEY}&units=metric&lang=ru')
    data = json.loads(res.text)

    table = "```\n"
    table += "{:^15} | {:^10} | {:^15}\n".format("Дата и время", "Макс. темп. (°C)", "Описание\n")

    for forecast in data['list']:
        date_time = forecast['dt_txt']
        max_temp = forecast['main']['temp_max']
        description = forecast['weather'][0]['description']
        table += "{:^15} | {:^10} | {:^15}\n".format(date_time, max_temp, description)
    table += "```"

    bot.send_message(message.chat.id, table, parse_mode='Markdown')
