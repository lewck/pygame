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

    def newPlayer(self, **kwargs):
        #Init vars
        self.id = tool.genRandomString(16)

        playerVariableDefaults = {
            'name': 'player1'
        }

        self.playerVariables = {}
        #set game variables (pv prefix, non camel-case for simplicity)

        for key, value in playerVariableDefaults.items():
            try:
                self.playerVariables[key] = kwargs['pv'+key]
            except KeyError:
                #Assume default
                self.playerVariables[key] = value

        self.balance = 3000