from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_low_get_city_btn() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    btn1 = InlineKeyboardButton('Узнать погоду в городе', callback_data='low_city_weather')
    keyboard.row(btn1)
    btn2 = InlineKeyboardButton('Команды бота', callback_data='commands_bot')
    keyboard.row(btn2)
    return keyboard
