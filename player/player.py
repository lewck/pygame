from webinteract.playerdata import playerData
from util.tool import tool

class player:
    def __init__(self, **kwargs):
        #Assign initial values

        self.newPlayer(**kwargs)

        '''
        if (self.id):
            self.loadPlayerData()
        try:

        except AttributeError:
            print('new player')
        '''

    def loadPlayerData(self, id):
        self.playerData = playerData()
        print(self.playerData.get(id))
        print('loading')
        return True
        #TODO SAVE ERROR

    def newPlayer(self, **kwargs):
        #Init vars
        self.id = tool.genRandomString(16)

        gameVariableDefaults = {
            'difficulty': 2,
            'balance': 5
        }

        self.gameVariables = {}

        #set game variables (gv prefix, non camel-case for simplicity)
        for key, value in gameVariableDefaults.items():
            try:
                self.gameVariables[key] = kwargs['gv'+key]
            except KeyError:
                #Assume default
                self.gameVariables[key] = value

        self.balance = 3000