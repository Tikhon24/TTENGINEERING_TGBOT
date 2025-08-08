import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Roller(SqlAlchemyBase, SerializerMixin):
    """
    Каток:
        - Наименование
        - Кол-во барабанов
        - Требуемая мощность
        - Цена
        - Модель*
        - Ширина захвата
        - Масса
        - Рабочая скорость
        - Диаметр барабана
        - Транспортная ширина
        - Фото
        - Видео
    """
    __tablename__ = 'Каток'

    # - Идентификационный номер
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    # - Наименование
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # - Кол-во барабанов
    reels_count = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Требуемая мощность
    required_power = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # - Цена
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Модель*
    model = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # - Ширина захвата
    capture_width = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Рабочая скорость
    working_speed = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Масса
    weight = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Диаметр барабана
    reels_diameter = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Транспортная ширина
    transport_width = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Фото
    photo = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # - Видео
    video = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __str__(self):
        return str(Roller.name)
