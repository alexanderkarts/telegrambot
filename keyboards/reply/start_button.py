from loader import bot
from telebot import types

markup = types.ReplyKeyboardMarkup()

btn1 = types.KeyboardButton('/help')
markup.add(btn1)