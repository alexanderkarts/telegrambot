from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def btn_registration() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)

    btn1 = InlineKeyboardButton('Узнать погоду в городе', callback_data='city_weather')
    keyboard.add(btn1)
    return keyboard
