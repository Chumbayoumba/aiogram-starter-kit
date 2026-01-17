from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router(name="start")


@router.message(CommandStart())
async def cmd_start(message: Message):
    """Handle /start command"""
    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        "Я бот, созданный на базе Aiogram Starter Kit.\n\n"
        "📝 Команды:\n"
        "/start - Начать заново\n"
        "/help - Помощь"
    )
