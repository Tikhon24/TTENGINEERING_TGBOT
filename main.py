# Здесь мы запускаем бота и инициализируем БД
import asyncio
from aiogram import Dispatcher

from app.handlers import router
from create_bot import bot

from database.data import db_session

dp = Dispatcher()


async def init_db():
    global filename
    filename = 'database/db/technic.db'
    db_session.global_init(filename)


async def main() -> None:
    await init_db()

    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
