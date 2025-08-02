from base_tool import BaseMaster


class GetMaster(BaseMaster):

    def __init__(self, Model):
        super().__init__(Model)

    async def get_data(self, **filters):

        query = self.session.query(self.Model)

        if '' in filters:
            # Сцепка
            query = query.filter(self.Model.coupling == filters[''])
        if '' in filters:
            # Рядность
            query = query.filter(self.Model.row_by_row == filters[''])
        if '' in filters:
            # Модель
            query = query.filter(self.Model.model == filters[''])

        return query.all()
