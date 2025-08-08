from base_tool import BaseMaster


class GetMaster(BaseMaster):

    def __init__(self, Model):
        super().__init__(Model)

    async def get_data(self, **filters):
        """ Возвращает все экземпляры по фильтрам """

        query = self.session.query(self.Model)

        if 'Сцепка' in filters:
            # Сцепка
            query = query.filter(self.Model.coupling == filters['Сцепка'])
        if 'Рядность' in filters:
            # Рядность
            query = query.filter(self.Model.row_by_row == filters['Рядность'])
        if 'Модель' in filters:
            # Модель
            query = query.filter(self.Model.model == filters['Модель'])

        return query.all()
