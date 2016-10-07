import settings
from util.tool import tool


class event:
    def __init__(self, obj):
        self.obj = obj
        self.id = tool.genRandomString(16)

    def doEvent(self):
        self.obj.doEve()
        print('doneeve')

    @staticmethod
    def create(obj):
        settings.activeEventDB.append(event(obj))
        return settings.activeEventDB[len(settings.activeEventDB) - 1].id




