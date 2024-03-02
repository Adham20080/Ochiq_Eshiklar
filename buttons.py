from aiogram import types

key = [
    [types.KeyboardButton(text="Users"), types.KeyboardButton(text="Chat")]
]
keyboard = types.ReplyKeyboardMarkup(keyboard=key, resize_keyboard=True)
