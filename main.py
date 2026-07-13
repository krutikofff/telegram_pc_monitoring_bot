import asyncio
from aiogram import Bot, Dispatcher
from handlers.common import router as common_router
from handlers.monitor import router as monitor_router
from config import TOKEN

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(common_router, monitor_router)

    await dp.start_polling(bot)

asyncio.run(main())