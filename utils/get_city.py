import json
import requests

from config_data.config import API_KEY
from database.bot_database import start_find_user
from handlers.default_handlers.help import func_help
from keyboards.inline.get_city_button import get_city_button
from loader import bot


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
