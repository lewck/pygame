from object.base import base
from inventory import inventory
from shop import shop

class exports(base):
    def __init__(self, **kwargs):
        print('init exports')
        self.type = 'exports'
        self.title = 'exports'
        super(exports, self).setVars(image=self.title, **kwargs)
        self.passable = []
        self.inventory = inventory(500)
        self.price = 500
        self.tickListen = [5]

    def doTick(self, tickID):
        if(tickID==0):
            print(self.inventory.inventory)
            if(self.inventory.hasAny()):
                toSell = self.inventory.takeItem('all', 'all')

                print('TO SELL')
                print(toSell)

                shop.sell(toSell)


    def eventClick(self):
        super(exports, self).log()