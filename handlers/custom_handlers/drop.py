from database.bot_database import drop_user_reg
from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['drop'])
def registration(message: Message) -> None:
    drop_user_reg(message)
    bot.send_message(message.from_user.id, 'Ваши данные удалены!')
