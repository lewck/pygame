from util.tool import tool

class tick:
    def __init__(self):
        self.tick = {}

    def register(self, tick, action, identifier=0):
        # Identifier is optional, allows all ticks to be removed
        tickID = tool.genRandomString()
        self.tick[tickID] = [identifier, tick, action]
        return tickID

    def getAll(self):
        return self.tick

    def get(self, tickID):
        # Return the tick if it exists
        try:
            return(self.tick[tickID])
        except IndexError:
            return False

    def remove(self, **kwargs):
        if('identifier' in kwargs):
            # Remove all with a common identifier if provided
            removeBuffer = []
            for key, each in self.tick.items():
                if(each[0]==kwargs['identifier']):
                    removeBuffer.append(key)

            for each in removeBuffer:
                del self.tick[each]