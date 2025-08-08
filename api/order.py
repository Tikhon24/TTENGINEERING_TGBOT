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
    async def another_request(table_name: str, data: dict = None, counter: int = None) -> dict:
        """
        Распоряжается другими запросами и отдает данные|
            counter = None, если это первый вызов функции в контексте
        """

        master = DataBaseMaster(table_settings.MODELS[table_name])

        if counter is None:
            result = dict()
            result['questions'] = table_settings.QUESTIONS[table_name]
            tables_names = await OrderMaster.first_request()

        if table_name == 'Плуг чизельный':
            pass
        if table_name == 'Борона зубовая':
            pass
        if table_name == 'Борона дисковая':
            pass
        if table_name == 'Каток':
            pass
