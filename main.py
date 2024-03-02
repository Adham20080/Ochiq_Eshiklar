import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command

from config import Token
from hendlers import start_com
from start import start_up, start_down

bot = Bot(token=Token)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


async def main():
    dp.startup.register(start_up)
    dp.message.register(start_com, Command("start"))
    dp.shutdown.register(start_down)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
