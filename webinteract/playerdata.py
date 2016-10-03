from webinteract.base import base

class playerData(base):
    def __init__(self):
        #Init parent
        super(playerData, self).__init__()

    def get(self, playerID):
        return self.requestCall('playerData', {'playerID':playerID})