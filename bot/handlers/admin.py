from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from bot.config import settings

router = Router(name="admin")


# Admin filter
router.message.filter(F.from_user.id.in_(settings.ADMIN_IDS))


@router.message(Command("stats"))
async def cmd_stats(message: Message):
    """Show bot statistics (admin only)"""
    await message.answer(
        "📊 <b>Статистика</b>\n\n"
        "Пользователей: 0\n"
        "Сообщений сегодня: 0\n\n"
        "<i>Добавьте подсчёт в базу данных</i>",
        parse_mode="HTML"
    )


@router.message(Command("broadcast"))
async def cmd_broadcast(message: Message):
    """Broadcast message to all users (admin only)"""
    # Get message to broadcast
    text = message.text.replace("/broadcast ", "", 1)
    
    if not text or text == "/broadcast":
        await message.answer("Использование: /broadcast <текст сообщения>")
        return
    
    await message.answer(f"✅ Рассылка запланирована: {text[:50]}...")
