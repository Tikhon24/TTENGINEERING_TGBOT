from database.tools.get_tools import GetMaster
from database.tools.base_tool import BaseMaster


class DataBaseMaster(GetMaster):

    def __init__(self, Model):
        super().__init__(Model)
