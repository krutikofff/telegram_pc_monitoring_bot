import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession # import for proxy
from handlers.common import router as common_router
from handlers.monitor import router as monitor_router
from config import TOKEN, ADMIN_ID

async def main(is_proxy_needed = None):

    while True:
        is_proxy_needed = input("Is proxy needed? (y/n): ").lower()

        if is_proxy_needed == "y":
            proxy_link = input("Please enter proxy link (default: http://127.0.0.1:10808): ")

            if proxy_link == "":
                proxy_link = "http://127.0.0.1:10808"

            session = AiohttpSession(proxy=proxy_link)
            bot = Bot(token=TOKEN, session=session)
            break

        elif is_proxy_needed == "n":
            bot = Bot(token=TOKEN)
            break

        else: print("Error! You should enter either 'y' or 'n'.")

    dp = Dispatcher()

    dp.include_routers(common_router, monitor_router)

    while True:
        notify_choice = input("Send message to admin? (y/n): ")

        if notify_choice == "n":
            print("🚀 Bot has started! Listening for messages...")
            break
        elif notify_choice == "y":
            try:
                await bot.send_message(chat_id=ADMIN_ID, text="🚀 Bot has started!")
                print("Log: Startup notification sent to admin, bot has started.")
            except Exception as e:
                print(f"Log: Could not send startup notification: {e}")
            break
        else: print("Error! You should enter either 'y' or 'n'.")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
