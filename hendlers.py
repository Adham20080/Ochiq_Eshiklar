from buttons import keyboard
from aiogram import types
from config import Admin


async def start_com(message: types.Message):
    if message.from_user.id == Admin:
        await message.answer("Xush kelibsiz Admin!", reply_markup=keyboard)
    else:
        await message.answer(f"Xush kelibsiz hurmatli {message.from_user.first_name}")
