from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.messages as messages
from api.order import OrderMaster

router = Router()


class Catalog(StatesGroup):
    table = State()
    parameters = State()
    count = State()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(messages.start(), reply_markup=kb.start)


@router.message(F.text == "Каталог")
@router.message(Command("catalog"))
async def open_catalog(massage: Message, state: FSMContext):  # Открываем каталог и задаем вопрос какя техника требуется

    tables = await OrderMaster.first_request()  # запрос на получение всех названий таблиц

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
    quantity = await OrderMaster.second_request(table)
    print(quantity)
    data = await state.get_data()
    print(data)
# -=----------------------------------------------------------------------------------------------------------=-

    parameter = await OrderMaster.another_request(**data)  # запрос на получение первого вопроса---
    print("прараметры", parameter)
# -=----------------------------------------------------------------------------------------------------------=-

    col = list(parameter.keys())[0]  # название столбца
    options = parameter[col]  # варианты ответа

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

    if flag:
# -=----------------------------------------------------------------------------------------------------------=-
        parameter = await OrderMaster.another_request(**data)  # запрос на получение первого вопроса---
        print("прараметры", parameter)
# -=----------------------------------------------------------------------------------------------------------=-

        col = list(parameter.keys())[0]  # название столбца
        options = parameter[col]  # варианты ответа

        await callback.message.edit_text(text=f"Вопрос {count}",
                                         reply_markup=await kb.create_keyboard("parameters", options, key=col, other_data=quantity))
    else:
# -=-----------------------------------=Оправка последних данных=---------------------------------------------=-
        print(data)  # отправка финальных данных
        models = await OrderMaster.another_request(**data)  # Получаем все модели
# -=----------------------------------------------------------------------------------------------------------=-

        await callback.message.edit_text(text="Выберите модель",
                                         reply_markup=await kb.create_keyboard("models", models))


@router.callback_query(lambda c: c.data.startswith('models:'))
async def choose_model(callback: CallbackQuery, state: FSMContext):
    callback_data = callback.data.split(':')  # получаем все денные из колбэка и разбиваем по переменным
    model = callback_data[1]

    data = await state.get_data()
# -=----------------------------------------------------------------------------------------------------------=-
    print(model)  # отправка выбранной модели
    text = "данные"
# -=----------------------------------------------------------------------------------------------------------=-

    await callback.message.edit_text(text=f"{model}\n{text}", reply_markup=await kb.create_order_keyboard(model, data))


@router.callback_query(lambda c: c.data.startswith('models:'))
async def make_order(callback: CallbackQuery):
    pass

