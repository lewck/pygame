import settings
from util.tool import tool


class event:
    def __init__(self, modelID, data, trigger, args, id):
        self.modelID = modelID
        self.data = data
        self.id = id
        self.trigger = trigger
        self.args = args



    def doEvent(self):
        #Verify buffer not active
        if(self.args != 0):
            getattr(settings.activeModelDB[self.modelID], self.trigger)(*self.args)
        else:
            getattr(settings.activeModelDB[self.modelID], self.trigger)()

    @staticmethod
    def create(modelID, data, trigger, args):
        id = tool.genRandomString(16)
        settings.activeEventDB[id] = event(modelID, data, trigger, args, id)
        return id



    @staticmethod
    def call(eventID):
        # Find Position
        settings.activeEventDB[eventID].doEvent()

