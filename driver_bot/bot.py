import asyncio
from aiogram import Bot, Dispatcher
from handlers import comand_handlers, callback_handlers, message_handlers




async def main():
    bot = Bot(token='6199903328:AAFK9VpL_otOHkSsF4arWGyy8MEL1ws-Z0o')
    dp = Dispatcher()
    dp.include_routers(message_handlers.router, comand_handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())