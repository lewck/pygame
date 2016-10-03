from object.base import base
from inventory import inventory

class market(base):
    def __init__(self, y, x, direction):
        print('initMarket')
        super(market, self).setVars(y,x,0,'market',direction, False)
        self.passable = []
        self.inventory = inventory(25)
        self.price = 500

    def eventClick(self):
        super(market, self).log()