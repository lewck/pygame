from object.base import base
from inventory import inventory
import settings


class farm_1(base):
    def __init__(self, y, x, direction):
        self.name = 'farm_1'
        print('initFarm')
        super(farm_1, self).setVars(y,x,0,self.name,direction, [20,30])
        self.passable = []
        self.inventory = inventory(30)


    def eventClick(self):
        super(farm_1, self).log()

    def doTick(self, tickID):
        if(tickID==0):
            pass
            #chance grow increase
        if (tickID == 1):
            if(self.inventory.addItem('vegetableCarrot',8)=='INVFULL'):
                self.image = self.load(self.name+'_full')
