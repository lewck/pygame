from util.tool import tool

class player:
    def __init__(self, **kwargs):
        # Assign initial values

        self.newPlayer(**kwargs)

    def newPlayer(self, **kwargs):
        #Init vars
        self.id = tool.genRandomString(16)

        playerVariableDefaults = {
            'name': 'player1'
        }

        self.playerVariables = {}
        # Set player variables (pv prefix, non camel-case for simplicity)

        for key, value in playerVariableDefaults.items():
            try:
                self.playerVariables[key] = kwargs['pv'+key]
            except KeyError:
                # Assume default
                self.playerVariables[key] = value

        self.balance = 9999