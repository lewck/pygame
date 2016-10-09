import settings
from util.tool import tool


class event:
    def __init__(self, modelID, data, trigger):
        self.modelID = modelID
        self.data = data
        self.id = tool.genRandomString(16)
        self.trigger = trigger



    def doEvent(self):
        getattr(settings.activeModelDB[self.modelID], self.trigger)()
        print('doneeve')

    @staticmethod
    def create(modelID, data, trigger):
        settings.activeEventDB.append(event(modelID, data, trigger))
        return settings.activeEventDB[len(settings.activeEventDB)-1].id



    @staticmethod
    def call(eventID):
        # Find Position
        for i in range(0, len(settings.activeEventDB)):
            if (settings.activeEventDB[i].id == eventID):
                settings.activeEventDB[i].doEvent()
                break

