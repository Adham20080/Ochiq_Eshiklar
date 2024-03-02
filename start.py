from aiogram import Bot

from config import Admin


async def start_up(bot: Bot):
    await bot.send_message(chat_id=Admin, text="Bot ishga tushdi")


async def start_down(bot: Bot):
    await bot.send_message(chat_id=Admin, text="Bot ishdan to'xtadi")
