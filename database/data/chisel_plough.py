import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class ChiselPlough(SqlAlchemyBase, SerializerMixin):
    """
    Плуг чизельный:
        - Наименование
        - Кол-во стоек
        - Требуемая мощность
        - Цена
        - Сцепка*
        - Ширина захвата
        - Рабочая скорость
        - Кол-во рабочих органов
        - Масса
        - Фото
        - Видео
    """
    __tablename__ = 'Плуг чизельный'

    # - Идентификационный номер
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    # - Наименование
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # - Кол-во стоек
    racks_count = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Требуемая мощность
    required_power = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # - Цена
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Сцепка*
    coupling = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # - Ширина захвата
    capture_width = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Рабочая скорость
    working_speed = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Масса
    weight = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Кол-во рабочих органов
    work_bodies_count = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Фото
    photo = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # - Видео
    video = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __str__(self):
        return str(ChiselPlough.name)
