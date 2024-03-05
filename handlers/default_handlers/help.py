from loader import bot

from telebot.types import Message


@bot.message_handler(commands=['help'])
def func_help(message: Message):
    bot.reply_to(message, f'<b>Комады бота:</b>\n\n'
                          f'Поздороваться с ботом — напиши "Привет"\n\n'
                          f'/start — запуск бота\n'
                          f'/hello_world — приветствие\n'
                          f'/help — помощь по командам бота\n'
                          f'/registration — регистрация\n'
                          f'\n<b>Команды погоды:</b>\n\n'
                          f'/weather — текущая погода\n'
                          f'/low — минимальная температура за 5 дней каждые 3 часа\n'
                          f'/high — максимальная температура за 5 дней каждые 3 часа', parse_mode='HTML')
