from database.data.db_session import create_session
from sqlalchemy.orm import Session


class BaseTool:
    """
    Инициализирует сессию
    """

    def __init__(self):
        self.session: Session = create_session()


class BaseMaster(BaseTool):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

    async def delete_by_name(self, name):
        """ Удаляет экземпляр по названию """
        try:
            self.session.query(self.Model).filter(self.Model.name == name).delete()
            self.session.commit()
        except Exception as ex:
            print('ERROR:', ex)

    async def get_by_name(self, name):
        try:
            items = self.session.query(self.Model).filter(self.Model.name == name).all()
            return items
        except Exception as ex:
            print('ERROR:', ex)
            return None
