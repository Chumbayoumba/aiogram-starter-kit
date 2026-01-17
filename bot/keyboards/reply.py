from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_main_menu() -> ReplyKeyboardMarkup:
    """Main reply keyboard"""
    builder = ReplyKeyboardBuilder()
    
    builder.row(
        KeyboardButton(text="📊 Профиль"),
        KeyboardButton(text="⚙️ Настройки")
    )
    builder.row(
        KeyboardButton(text="📞 Контакты", request_contact=True)
    )
    
    return builder.as_markup(resize_keyboard=True)
