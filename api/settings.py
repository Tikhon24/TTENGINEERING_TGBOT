import sqlite3


class TableSettings:

    QUESTIONS = {
        'Плуг чизельный': 1,
        'Борона зубовая': 1,
        'Борона дисковая': 2,
        'Каток': 1
    }

    FILENAME = '../database/db/technic.db'

    @staticmethod
    async def get_tables_name():
        # Подключаемся к базе данных
        with sqlite3.connect(TableSettings.FILENAME) as conn:
            # Создаем курсор
            cursor = conn.cursor()
            # Выполняем SQL-запрос для получения списка таблиц
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            # Получаем все результаты
            tables_names = cursor.fetchall()
            tables_names = [i[0] for i in tables_names]
            return tables_names
