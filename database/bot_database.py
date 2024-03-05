import sqlite3

with sqlite3.connect('database\\tgg_bot.db', check_same_thread=False) as database:
    """
    Создание таблицы с тремя показателями: 
                    user_id - Айди пользователя;
                    name - Имя пользователя;
                    phone_number - Номер телефона пользователя.
    """
    cursor = database.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                   user_id INTEGER,
                   name TEXT,
                   phone_number INTEGER
                   )''')


def start_find_user(message):
    """
    Функция проверяет, есть ли пользователь в базе данных, поиск происходит по айди.
    Если пользователь найден, возвращается True.
    Если нет - False.
    """
    cursor.execute("SELECT user_id FROM users WHERE user_id =?", (message.from_user.id,))
    user = cursor.fetchone()
    if not user:
        return False
    else:
        return True


def add_user(message):
    """
    Функция добавляет пользователя в базу.
    Сначала происходит поиск пользователя по айди, если он найден, возвращает False
    Иначе, добавлет его.
    """
    cursor.execute("SELECT user_id FROM users WHERE user_id =?", (message.chat.id,))
    user = cursor.fetchone()
    if not user:
        cursor.execute("INSERT INTO users (user_id) VALUES (?)", (message.chat.id,))
        database.commit()
    else:
        return False


def add_user_name(message):
    """
    Функция добавляет имя пользователя.
    """
    cursor.execute("UPDATE users SET name = ? WHERE user_id = ?", (message.text, message.chat.id))
    database.commit()


def add_user_phone(message):
    """
    Функция добавляет номер телефона пользователя.
    """
    cursor.execute("UPDATE users SET phone_number = ? WHERE user_id = ?",
                   (message.contact.phone_number, message.chat.id))
    database.commit()


def name_user(message):
    """
    Функция берет имя пользователя по айди из базы и возвращает его.
    """
    cursor.execute("SELECT name FROM users WHERE user_id =?", (message.from_user.id,))
    user_name = cursor.fetchone()[0]
    return user_name


def phone_user(message):
    """
    Функция берет номер телефона пользователя по айди из базы и возвращает его.
    """
    cursor.execute("SELECT phone_number FROM users WHERE user_id =?", (message.from_user.id,))
    phone_name = cursor.fetchone()[0]
    return phone_name


def id_user(message):
    """
    Функция берет айди пользователя по айди из базы и возвращает его.
    """
    cursor.execute("SELECT user_id FROM users WHERE user_id =?", (message.from_user.id,))
    user_id = cursor.fetchone()[0]
    return user_id


def drop_user_reg(message):
    """
    Функция удаляет пользователя из базы.
    """
    cursor.execute('DELETE FROM users WHERE user_id =?', (message.from_user.id,))
    database.commit()
