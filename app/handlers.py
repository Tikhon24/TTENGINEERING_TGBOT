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
    count = State()


@router.message(CommandStart())
async def start(massage: Message):
    await massage.answer("start", reply_markup=kb.start)


@router.message(F.text == "Каталог")
@router.message(Command("catalog"))
async def open_catalog(massage: Message, state: FSMContext):  # Открываем каталог и задаем вопрос какя техника требуется
    tables = ["1", "2", "3", "4"]  # запрос на получение всех названий таблиц
    await state.set_state(Catalog.table)
    await massage.answer("*каталог*", reply_markup=await kb.create_keyboard("tables", tables))


@router.callback_query(lambda c: c.data.startswith('tables:'))
async def choose_table(callback: CallbackQuery, state: FSMContext):  # получаем ответ с нужной тблицей
    data = callback.data.split(':')
    table = data[1]

    await state.update_data(table=table)
    await state.set_state(Catalog.parameters)
    await state.update_data(parameters={})
    await state.update_data(count=0)  # Начинаем счетчик с нуля!!!!!!!!!!!!!

# -=----------------------------------------------------------------------------------------------------------=-
    print(table)
    parameter = [{"key": ["1", "2"]}, 2]  # запрос на получение первого вопроса
# -=----------------------------------------------------------------------------------------------------------=-
    col = list(parameter[0].keys())[0]  # название столбца
    options = parameter[0][col]  # варианты ответа
    quantity = parameter[1]  # количество вопросов

    await callback.message.edit_text(text="опа", reply_markup=await kb.create_keyboard("parameters",
                                                                                       options, key=col, other_data=quantity))


@router.callback_query(lambda c: c.data.startswith('parameters:'))
async def choose_options(callback: CallbackQuery, state: FSMContext):  # Принимаем вариант ответа и щадаем следующий
    callback_data = callback.data.split(':')  # получаем все денные из колбэка и разбиваем по переменным
    option = callback_data[1]
    col = callback_data[2]
    quantity = int(callback_data[3])

    data = await state.get_data()  # данные по опросу

    count = data.get("count", [])
    count += 1
    await state.update_data(count=count)

    selected_params = data.get("parameters", [])
    selected_params[col] = option

    flag = True
    data = await state.get_data()

    if count >= quantity:
        flag = False
# -=----------------------------------------------------------------------------------------------------------=-
        print(data)  # отправка финальных данных
# -=----------------------------------------------------------------------------------------------------------=-

    if flag:
# -=----------------------------------------------------------------------------------------------------------=-
        print(data)
        parameter = [{"key": ["1", "2"]}]  # запрос на получение последующего вопроса и оправка данных
# -=----------------------------------------------------------------------------------------------------------=-

        col = list(parameter[0].keys())[0]  # название столбца
        options = parameter[0][col]  # варианты ответа

        await callback.message.edit_text(text=option,
                                         reply_markup=await kb.create_keyboard("parameters", options, key=col, other_data=quantity))
    else:
        user_data = await state.get_data()
        await callback.message.edit_text(text=str(user_data))
# -=----------------------------------------------------------------------------------------------------------=-
        print(data, "final")  # отправка конечной сводки
# -=----------------------------------------------------------------------------------------------------------=-





