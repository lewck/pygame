import settings
from util.tool import tool

class event:
    def __init__(self, **kwargs):
        # Initiate local variables with provided arguments
        self.modelID = kwargs['modelID']
        self.data = kwargs['data']
        self.id = kwargs['id']
        self.trigger = kwargs['trigger']
        self.args = kwargs['args']
        self.active = False

    def doEvent(self):
        # Verify buffer not active
        if(self.args != 0):
            getattr(settings.activeModelDB[self.modelID], self.trigger)(*self.args)
        else:
            getattr(settings.activeModelDB[self.modelID], self.trigger)()

    @staticmethod
    def create(**kwargs):
        id = tool.genRandomString(16)
        if('modelID' in kwargs):
            # Assume visual event
            # modelID, data, trigger, args
            settings.activeEventDB[id] = event(**kwargs, id=id)
            return id
        # Extension for other event types

    @staticmethod
    def getActive():
        activeBuffer = {}
        # Append all with active attribute and return
        for key, each in (settings.activeEventDB.items()):
            if(each.active==True):
                activeBuffer[key] = each

        return activeBuffer