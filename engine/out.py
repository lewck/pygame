import settings
from util.tool import tool


class out:
    def __init__(self, modelID, data):
        self.modelID = modelID
        self.data = data
        self.id = tool.genRandomString(16)


    @staticmethod
    def create(modelID, data):
        settings.activeOutDB.append(out(modelID, data))
        return settings.activeOutDB[len(settings.activeEventDB)-1].id