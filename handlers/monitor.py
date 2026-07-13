from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from services.system_info import(
    get_cpu_status,
    get_ram_status
)
from config import ADMIN_ID

router = Router()

@router.message(Command("status"))
async def status_handler(message: Message):
    cpu_text = get_cpu_status()
    ram_text = get_ram_status()

    # check if the bot is yours
    if message.from_user.id != ADMIN_ID:
        await message.answer(
            f"Your Telegram ID does not coincide with the ID in config.py at your PC.\n"
            f"Please change it to yours!\n"
            f"Your Telegram ID is {message.from_user.id}"
        )
        return

    full_message = f"{cpu_text}\n{ram_text}"

    await message.answer(full_message)