import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello_world'])
def send_welcome(message):
    bot.reply_to(message, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['help'])
def func_help(message):
    bot.reply_to(message, f'Комады бота: \n'
                          f'/hello_world — приветствие\n'
                          f'/help — помощь по командам бота\n'
                          f'/low — вывод минимальных показателей (с изображением товара/услуги/и таr далее)\n'
                          f'/high — вывод максимальных (с изображением товара/услуги/и тд)\n'
                          f'/custom — вывод показателей пользовательского диапазона'
                          f' (с изображением товара/услуги/и так далее)\n'
                          f'/history — вывод истории запросов пользователей.')


@bot.message_handler(content_types='text')
def say_hello_on_text(message):
    if message.text.lower() == 'привет':
        bot.reply_to(message, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')


if __name__ == '__main__':
    bot.infinity_polling()
