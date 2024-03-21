from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def btn_locations_high_and_low_get_city(data) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for location in data:
        button_text = f"{location.get('local_names', {}).get('ru', location.get('name', 'Default Name'))}" \
                      f" - {location.get('country')} - {location.get('state', 'Default State')}"

        callback_data = f"highlocation_{location.get('lat')}_{location.get('lon')}"

        keyboard.add(InlineKeyboardButton(button_text, callback_data=callback_data))

        return keyboard
