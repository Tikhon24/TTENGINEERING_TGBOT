from database.tools.base_tool import BaseMaster


class PostMaster(BaseMaster):

    def __init__(self, Model):
        super().__init__(Model)

    async def post_media_by_name(self, name: str, photo: list, video: list) -> bool:
        """ Добавляет в БД фото и видео """
        try:
            item = self.session.query(self.Model).filter(self.Model.name == name).first()
            if item is None:
                return None
            # Разделяем список на строку по знаку ";"
            item.photo = ';'.join([str(i) for i in photo])
            item.video = ';'.join([str(i) for i in video])
            self.session.commit()
            return True
        except Exception as ex:
            print('ERROR:', ex)
            return False
