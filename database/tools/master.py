from database.tools.get_tools import GetMaster


class DataBaseMaster(GetMaster):

    def __init__(self, Model):
        super().__init__(Model)
