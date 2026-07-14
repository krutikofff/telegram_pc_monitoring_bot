from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from services.system_info import (
    get_cpu_status,
    get_ram_status,
    get_disk_status
)
from config import ADMIN_ID

router = Router()

@router.message(Command("status"))
async def status_handler(message: Message):
    cpu_text = get_cpu_status()
    ram_text = get_ram_status()
    disks = get_disk_status()

    total_free, total_available = 0, 0
    for disk in disks:
        total_free += disk["free"]
    for disk in disks:
        total_available += disk["total"]
    total_percent = round((total_free / total_available) * 100, 2)


    # check if the bot is yours
    if message.from_user.id != ADMIN_ID:
        await message.answer(
            f"Your Telegram ID does not coincide with the ID in config.py at your PC.\n"
            f"Please change it to yours!\n"
            f"Your Telegram ID is {message.from_user.id}"
        )
        return

    full_message = (
        "<b>┏━━━━━━━━━━━━━┓\n"
        " ::: PC HARDWARE MONITOR :::\n"
        "┗━━━━━━━━━━━━━┛</b>\n\n"
        f"<b>📊 CPU usage:</b> <code>{cpu_text}</code>\n"
        f"<b>💾 RAM usage:</b> <code>{ram_text}</code>\n\n"
        "<b>┏━━━━━━━━━┓\n"
        " ::: DISCS & MEMORY:::\n"
        "┗━━━━━━━━━┛</b>\n\n"
        f"<b>💽 Total:</b> <code>{total_percent}%</code>  ({total_free} GB free / {total_available} GB total)\n\n"
    )
    for disk in disks:
        full_message += (
            f"<b>💽 Disk {disk["name"]}</b> <code>{disk["percent"]}%</code> "
            f" ({disk["free"]:.2f} GB free / {disk["total"]:.2f} GB total)\n"
        )

    await message.answer(full_message, parse_mode="HTML")