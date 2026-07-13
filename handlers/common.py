from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Welcome! I am PC-monitor Bot.\n" \
        "Use the /status command to check system hardware metrics."
    )