from object.base import base
from inventory import inventory

class genericHouse(base):
    def __init__(self, y, x, direction):
        print('initHouse')
        super(genericHouse, self).setVars(y,x,0,'house',direction, False)
        self.passable = []
        self.inventory = inventory(20)

    def eventClick(self):
        super(genericHouse, self).log()