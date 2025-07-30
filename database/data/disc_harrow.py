import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class DiskHarrow(SqlAlchemyBase, SerializerMixin):
    """
    Класс дисковой бороны
        - Наименование
        - Кол-во дисков
        - Требуемая мощность
        - Цена
        - Сцепка*
        - Рядность*
        - Ширина захвата
        - Рабочая скорость
        - Масса
        - Расстояние между дисками
        - Расстояние между рядами
    """
    __tablename__ = 'Борона дисковая'

    # - Идентификационный номер
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    # - Наименование
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # - Кол-во дисков
    disk_count = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # Требуемая мощность
    required_power = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # Цена
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # Сцепка*
    coupling = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # Рядность*
    row_by_row = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # Ширина захвата
    capture_width = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # Рабочая скорость
    working_speed = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # Масса
    weight = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # Расстояние между дисками
    distance_btw_disks = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # Расстояние между рядами
    distance_btw_rows = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    def __str__(self):
        return str(DiskHarrow.name)
