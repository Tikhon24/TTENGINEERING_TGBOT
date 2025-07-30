from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def start(massage: Message):
    await massage.answer("start", reply_markup=kb.start)


@router.message(F.text == "Каталог")
@router.message(Command("catalog"))
async def open_catalog(massage: Message):
    await massage.answer("*каталог*")


