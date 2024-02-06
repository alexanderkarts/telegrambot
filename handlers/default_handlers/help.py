from loader import bot

from telebot.types import Message


@bot.message_handler(commands=['help'])
def func_help(message: Message):
    bot.reply_to(message, f'Комады бота: \n'
                          f'/hello_world — приветствие\n'
                          f'/help — помощь по командам бота\n'
                          f'/low — вывод минимальных показателей (с изображением товара/услуги/и таr далее)\n'
                          f'/high — вывод максимальных (с изображением товара/услуги/и тд)\n'
                          f'/custom — вывод показателей пользовательского диапазона'
                          f' (с изображением товара/услуги/и так далее)\n'
                          f'/history — вывод истории запросов пользователей.')
