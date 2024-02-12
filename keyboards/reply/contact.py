from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def request_contact() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(True, True)
    btn1 = KeyboardButton('Отправить контакт', request_contact=True)
    keyboard.add(btn1)
    return keyboard
