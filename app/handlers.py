from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()


class Catalog(StatesGroup):
    table = State()
    parameters = State()
    parameters_list = {}


@router.message(CommandStart())
async def start(massage: Message):
    await massage.answer("start", reply_markup=kb.start)


@router.message(F.text == "Каталог")
@router.message(Command("catalog"))
async def open_catalog(massage: Message, state: FSMContext):
    tables = ["1", "2", "3", "4"]  # запрос на получение всех названий таблиц
    await state.set_state(Catalog.table)

    await massage.answer("*каталог*", reply_markup=await kb.create_keyboard("tables", tables))


@router.callback_query(lambda c: c.data.startswith('tables:'))
async def choose_table(callback: CallbackQuery, state: FSMContext):
    data = callback.data.split(':')
    table = data[1]
    await state.update_data(table=table)
    parameter = [{"key": ["1", "2"]}, 3]  # зпрос на получение первого вопроса
    options = parameter[0]
    quantity = parameter[1]
    await callback.message.edit_text(text="опа", reply_markup=await kb.create_keyboard("parameters", options, quantity))


@router.callback_query(lambda c: c.data.startswith('parameters:'))
async def choose_options(callback: CallbackQuery, state: FSMContext):
    data = callback.data.split(':')
    option = data[1]
    quantity = data[2]
    quantity -= 1
    if quantity > 0:



