from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name="help")


@router.message(Command("help"))
async def cmd_help(message: Message):
    """Handle /help command"""
    await message.answer(
        "📚 <b>Справка</b>\n\n"
        "Этот бот создан на базе Aiogram Starter Kit.\n\n"
        "<b>Доступные команды:</b>\n"
        "/start - Начать работу\n"
        "/help - Показать эту справку\n\n"
        "💡 Разверните своего бота за 5 минут:"
        "\ngithub.com/Chumbayoumba/aiogram-starter-kit",
        parse_mode="HTML"
    )
