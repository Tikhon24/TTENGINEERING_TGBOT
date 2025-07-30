from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

router = Router()


@router.message(CommandStart())
async def start(massage: Message):
    await massage.answer("start")
