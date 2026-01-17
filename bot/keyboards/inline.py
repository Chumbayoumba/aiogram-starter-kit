from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_main_keyboard() -> InlineKeyboardMarkup:
    """Main inline keyboard"""
    builder = InlineKeyboardBuilder()
    
    builder.row(
        InlineKeyboardButton(text="📱 Сайт", url="https://example.com"),
        InlineKeyboardButton(text="💬 Поддержка", url="https://t.me/longfest")
    )
    builder.row(
        InlineKeyboardButton(text="✨ Подписаться", callback_data="subscribe")
    )
    
    return builder.as_markup()


def get_confirm_keyboard() -> InlineKeyboardMarkup:
    """Confirmation keyboard"""
    builder = InlineKeyboardBuilder()
    
    builder.row(
        InlineKeyboardButton(text="✅ Да", callback_data="confirm_yes"),
        InlineKeyboardButton(text="❌ Нет", callback_data="confirm_no")
    )
    
    return builder.as_markup()
