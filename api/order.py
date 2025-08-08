from api.settings import TableSettings as table_settings
from database.tools.master import DataBaseMaster


class OrderMaster:
    """
    Ведет сценарий заказа
    """

    @staticmethod
    async def first_request() -> list[str]:
        """ Возвращает названия таблиц из базы данных """
        tables_names = await table_settings.get_tables_name()
        return tables_names

    @staticmethod
    async def second_request(table_name) -> int:
        """ Возвращает кол-во вопросов """
        count = table_settings.QUESTIONS[table_name]
        return count

    @staticmethod
    async def another_request(table_name: str, data: dict = {}, counter: int = None):
        """
        Распоряжается другими запросами и отдает данные|
            counter = None, если это первый вызов функции в контексте
        """
        master = DataBaseMaster(table_settings.MODELS[table_name])
        req = table_settings.MODELS_QUESTIONS[table_name][counter]
        query = await master.get_data(data)
        if req == table_settings.MODELS_QUESTIONS[table_name][len(table_settings.MODELS_QUESTIONS[table_name]) - 1]:
            # Проверка на то, последний ли это вопрос(здесь вопрос последний, возвращаем список имен)
            result = [str(item.name) for item in query]
        else:
            # Здесь вопрос не последний
            result = {}
            if req == 'Сцепка':
                my_data = result = [str(item.coupling) for item in query]
            if req == 'Рядность':
                my_data = result = [str(item.row_by_row) for item in query]
            if req == 'Модель':
                my_data = result = [str(item.model) for item in query]
            result[req] = my_data
        return result
