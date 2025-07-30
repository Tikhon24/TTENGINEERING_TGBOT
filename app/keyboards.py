from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

start = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Каталог")],
    [KeyboardButton(text="О нас"), KeyboardButton(text="Помощь")]
])


async def create_keyboard(general_callback, buttons, other_data=None):
    keyboard = InlineKeyboardBuilder()
    for button in buttons:
        keyboard.add(InlineKeyboardButton(text=button, callback_data=f"{general_callback}:{button}:{other_data}"))
    return keyboard.adjust(1).as_markup()

