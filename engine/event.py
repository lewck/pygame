import settings
from util.tool import tool


class event:
    def __init__(self, modelID, data, trigger, id):
        self.modelID = modelID
        self.data = data
        self.id = id
        self.trigger = trigger



    def doEvent(self):
        #Verify buffer not active
        getattr(settings.activeModelDB[self.modelID], self.trigger)()
        print('doneeve')

    @staticmethod
    def create(modelID, data, trigger):
        id = tool.genRandomString(16)
        settings.activeEventDB[id] = event(modelID, data, trigger, id)
        return id



    @staticmethod
    def call(eventID):
        # Find Position
        settings.activeEventDB[eventID].doEvent()

