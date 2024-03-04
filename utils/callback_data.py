from handlers.default_handlers.help import func_help
from loader import bot
from utils.get_city import get_city
from utils.high_get_city import high_location_weather, high_get_city
from utils.low_get_city import low_get_city, low_location_weather


@bot.callback_query_handler(func=lambda call: call.data.startswith('lowlocation_'))
def callback_query_low_location(call):
    print(call.data)

    lat, lon = call.data.split('_')[1:]
    print(f"Lat: {lat}, Lon: {lon}")

    low_location_weather(call.message, lat, lon)

    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith('highlocation_'))
def callback_query_high_location(call):
    print(call.data)

    lat, lon = call.data.split('_')[1:]
    print(f"Lat: {lat}, Lon: {lon}")

    high_location_weather(call.message, lat, lon)

    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: True)
def process_callback(call):
    bot.answer_callback_query(call.id)
    if call.data == "city_weather" or call.data == "button1":
        bot.send_message(call.from_user.id, 'Введи название города')
        bot.register_next_step_handler(call.message, get_city)
    elif call.data == "low_city_weather":
        bot.send_message(call.from_user.id, 'Введи название города')
        bot.register_next_step_handler(call.message, low_get_city)
    elif call.data == "high_city_weather":
        bot.send_message(call.from_user.id, 'Введи название города')
        bot.register_next_step_handler(call.message, high_get_city)
    elif call.data == "commands_bot" or call.data == "button2":
        func_help(call.message)
