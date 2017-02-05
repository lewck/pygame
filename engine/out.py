import settings
from util.tool import tool


class out:
    def __init__(self, modelID, data, id):
        # Initiate variables from user input
        self.modelID = modelID
        self.data = data
        self.id = id
        self.priority = data['priority']
        self.active = False

    @staticmethod
    def create(modelID, data):
        # Generate random ID
        id = tool.genRandomString(16)
        # Assign to global dictionary
        settings.activeOutDB[id]=(out(modelID, data, id))
        return id

    @staticmethod
    def getActiveByPriority():
        scanned = {}
        # Retrieve all active
        for key, each in settings.activeOutDB.items():
            if (each.active != False):
                scanned[key] = each

        # Sort all active
        sorted = tool.bubbleSort(values=scanned, localvariable='priority')

        return sorted