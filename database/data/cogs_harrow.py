import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class CogsHarrow(SqlAlchemyBase, SerializerMixin):
    """
    Борона зубовая:
        - Наименование
        - Кол-во борон
        - Требуемая мощность
        - Цена
        - Рядность*
        - Ширина захвата
        - Производительность
        - Глубина обработки
        - Масса
        - Рабочая скорость
    """
    __tablename__ = 'Борона зубовая'

    # - Идентификационный номер
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    # - Наименование
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # - Кол-во борон
    harrows_count = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Требуемая мощность
    required_power = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # - Цена
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Рядность*
    row_by_row = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # - Ширина захвата
    capture_width = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Рабочая скорость
    working_speed = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Масса
    weight = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # - Глубина обработки
    process_depth = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    def __str__(self):
        return str(CogsHarrow.name)
