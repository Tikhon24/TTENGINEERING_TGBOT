from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

start = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Каталог")],
    [KeyboardButton(text="О нас"), KeyboardButton(text="Помощь")]
])

order = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Заказать", callback_data="order"),
     InlineKeyboardButton(text="Назад", callback_data="back")]
])


async def create_keyboard(general_callback, buttons, key=None, other_data=None):
    keyboard = InlineKeyboardBuilder()
    for button in buttons:
        keyboard.add(InlineKeyboardButton(text=button, callback_data=f"{general_callback}:{button}:{key}:{other_data}"))
    return keyboard.adjust(1).as_markup()


async def create_order_keyboard(model, data):
    keyboard = InlineKeyboardBuilder()

    print("jgf", data['count'])
    keyboard.add(InlineKeyboardButton(text="Заказать", callback_data=f"order:{model}"))
    keyboard.add(InlineKeyboardButton(text="Назад", callback_data=f"parameters:::{data['count']}"))

    return keyboard.adjust(2).as_markup()
