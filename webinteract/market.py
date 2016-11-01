from webinteract.base import base

class market(base):
    def __init__(self):
        #Init parent
        super(market, self).__init__()

    def get(self, sortby = 'null'):
        return self.requestCall('market', {'sortby':sortby})

    def checkCache(self):
        #TODO fix
        return self.requestCall('checkCache', {'token': 1})