from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from database.bot_database import add_user, add_user_name, add_user_phone, name_user, phone_user, id_user
from keyboards.reply.contact import request_contact
@bot.message_handler(commands=['registration'])
def registration(message: Message) -> None:
    user_status = add_user(message)
    if user_status == False:
        idUser = id_user(message)
        name = name_user(message)
        phone = phone_user(message)
        bot.send_message(message.from_user.id, f'Вы уже зарегистрированы!\n'
                                               f'Ваши данные:\n'
                                               f'id - {idUser}\n'
                                               f'Имя - {name}\n'
                                               f'Номер телефона - {phone}\n'
                                               f'Чтобы удалить ваши данные используйте команду /drop')
    else:
        bot.set_state(message.from_user.id, UserInfoState.name, message.chat.id)
        bot.send_message(message.from_user.id, f'Сейчас я тебя добавлю в свою базу\n'
                                               f'Введи своё имя')


@bot.message_handler(state=UserInfoState.name)
def get_name(message: Message) -> None:
    add_user_name(message)
    bot.send_message(message.from_user.id,
                     'Спасибо, записал. Отправь свой номер нажав на кнопку',
                     reply_markup=request_contact())
    bot.set_state(message.from_user.id, UserInfoState.phone_number, message.chat.id)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text


@bot.message_handler(content_types=['text', 'contact'], state=UserInfoState.phone_number)
def get_contact(message: Message) -> None:
    if message.content_type == 'contact':

        add_user_phone(message)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['phone_number'] = message.contact.phone_number

            text = f'Спасибо за предоставленную информацию, ваши данные:\n' \
                   f'Имя - {data["name"]}\n' \
                   f'Номер телефона - {data["phone_number"]}\n'
            bot.send_message(message.from_user.id, text)
        bot.delete_state(message.from_user.id, message.chat.id)

    else:
        bot.send_message(message.from_user.id, 'Чтобы отправить контактную информацию нажми на кнопку')