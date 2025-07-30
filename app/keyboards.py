from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

start = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Каталог")],
    [KeyboardButton(text="О нас"), KeyboardButton(text="Помощь")]
])

