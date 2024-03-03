from buttons import keyboard
from aiogram import types
from config import Admin
from db import Database

db = Database("database.db")


async def start_com(message: types.Message):
    if message.from_user.id == Admin:
        await message.answer("Xush kelibsiz Admin!", reply_markup=keyboard)
    else:
        await message.answer(f"Xush kelibsiz hurmatli {message.from_user.first_name}")
        db.add_user(message.from_user.full_name, message.from_user.username,
                    message.from_user.id)
