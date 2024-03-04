from loader import bot

from telebot.types import Message


@bot.message_handler(commands=['help'])
def func_help(message: Message):
    bot.reply_to(message, f'Комады бота:\n\n'
                          f'Поздороваться с ботом — напиши "Привет" \n'
                          f'/start — запуск бота\n'
                          f'/hello_world — приветствие\n'
                          f'/help — помощь по командам бота\n'
                          f'/registration — регистрация\n'
                          f'\nКоманды погоды:\n\n'
                          f'/low — минимальная температура за 5 дней каждые 3 часа\n'
                          f'/high — максимальная температура за 5 дней каждые 3 часа')
