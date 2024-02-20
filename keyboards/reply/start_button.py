from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def start_button() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(True, True)

    btn1 = KeyboardButton('Привет')

    keyboard.row(btn1)
    #
    # btn2 = KeyboardButton('/hello_world')
    # btn3 = KeyboardButton('/help')
    #
    # keyboard.row(btn2, btn3)
    return keyboard
