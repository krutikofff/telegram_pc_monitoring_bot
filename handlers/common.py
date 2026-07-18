from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    start_message = (
        "<b>Welcome to yours PC monitoring bot!</b>\n"
        "You need to type /status to see your PC load.\n"
        "You also can type /help or /? to see available commands."
    )
    await message.answer(start_message, parse_mode="HTML")

@router.message(Command("help","?"))
async def help_handler(message: Message):
    help_message = (
        "<b>┏━━━━━━━━━━━━━━━━━━━━━━━━┓\n"
        " ::: COMMAND REFERENCE :::\n"
        "┗━━━━━━━━━━━━━━━━━━━━━━━━┛</b>\n\n"
        "/start - starts the bot\n"
        "/status - shows current PC load\n"
        "/top or /processes + N - shows top N processes (if you didn't specify N then default quantity is 5).\n"
        "/alert_on - enables automatic load alerts\n"
        "/alert_off - disables automatic load alerts\n"
        "/alert_threshold + N - sets the CPU/RAM alert threshold to N% (e.g. /alert_threshold 80)\n"
    )
    await message.answer(help_message, parse_mode="HTML")