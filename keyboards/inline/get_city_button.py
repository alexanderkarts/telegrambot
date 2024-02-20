from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_city_button() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)

    btn1 = InlineKeyboardButton('Другой город', callback_data='button1')
    btn2 = InlineKeyboardButton('Вернуться обратно', callback_data='button2')
    keyboard.add(btn1, btn2)
    return keyboard
