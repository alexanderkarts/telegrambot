from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_start_btn() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)

    btn1 = InlineKeyboardButton('Узнать погоду в городе', callback_data='city_weather')
    btn2 = InlineKeyboardButton('Команды бота', callback_data='commands_bot')
    keyboard.add(btn1, btn2)
    return keyboard
