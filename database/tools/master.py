from database.tools.get_tools import GetMaster
from database.tools.post_tools import PostMaster


class DataBaseMaster(GetMaster, PostMaster):

    def __init__(self, Model):
        super().__init__(Model)
