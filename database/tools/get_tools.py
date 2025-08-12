from database.tools.base_tool import BaseMaster


class GetMaster(BaseMaster):

    def __init__(self, Model):
        super().__init__(Model)

    async def get_data(self, filters):
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

    async def get_all_by_name(self, name):
        try:
            items = self.session.query(self.Model).filter(self.Model.name == name).first()
            if items is None:
                return None
            result = items.to_dict()
            return result
        except Exception as ex:
            print('ERROR:', ex)
            return None

    async def get_media_by_name(self, name):
        try:
            items = self.session.query(self.Model).filter(self.Model.name == name).first()
            if items is None:
                return None
            result = items.to_dict(only=['photo', 'video'])
            # Разделяем строку на список по знаку ";"
            result['photo'] = str(result['photo']).split(';')
            result['video'] = str(result['video']).split(';')
            return result
        except Exception as ex:
            print('ERROR:', ex)
            return None
