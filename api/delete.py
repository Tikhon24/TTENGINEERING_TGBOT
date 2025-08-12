from api.settings import TableSettings as table_settings
from database.tools.master import DataBaseMaster


class DeleteMaster:
    """
    Ведет удаление техники из бд
    """

    @staticmethod
    async def first_request() -> list[str]:
        """ Возвращает названия таблиц из базы данных """
        tables_names = await table_settings.get_tables_name()
        return tables_names

    @staticmethod
    async def delete_request(table: str, name: str) -> bool:
        master = DataBaseMaster(table_settings.MODELS[table])
        return await master.delete_by_name(name)
