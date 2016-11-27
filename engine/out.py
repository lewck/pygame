import settings
from util.tool import tool


class out:
    def __init__(self, modelID, data, id):
        self.modelID = modelID
        self.data = data
        self.id = id
        self.priority = data['priority']
        self.active = False

    @staticmethod
    def create(modelID, data):
        id = tool.genRandomString(16)
        settings.activeOutDB[id]=(out(modelID, data, id))
        return id

    @staticmethod
    def getActiveByPriority():
        scanned = {}
        for key, each in settings.activeOutDB.items():
            if (each.active != False):
                scanned[key] = each

        sort = tool.bubbleSort(values=scanned, localvariable='priority')
        return sort