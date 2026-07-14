import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession # import for proxy
from handlers.common import router as common_router
from handlers.monitor import router as monitor_router
from config import TOKEN

async def main():
    # before this, you need to install a proxy server on your PC
    session = AiohttpSession(proxy="http://127.0.0.1:10808")

    # session needed only if you started proxy
    bot = Bot(token=TOKEN, session=session)
    dp = Dispatcher()

    dp.include_routers(common_router, monitor_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
