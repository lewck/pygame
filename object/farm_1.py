from object.base import base
from inventory import inventory
from jobset.factory import factory as jobset
import settings


class farm_1(base):
    def __init__(self, **kwargs):
        self.title = 'farm_1'
        self.type = 'producer'

        super(farm_1, self).setVars(image='farm_1', **kwargs)
        self.passable = []
        self.inventory = inventory(30)
        self.status = 0
        self.used = False


    def eventClick(self):
        super(farm_1, self).log()

    def doTick(self, tickID):
        if(tickID==0):
            #chance grow increase
            if(self.inventory.isFull()):
                self.image = self.load(self.title)


        if (tickID == 1):
            if(self.inventory.addItem('vegetableCarrot',8)=='INVFULL') & (self.used==False):

                self.image = self.load(self.title+'_full')

                print('ADDING JOB')
                jobset.create(typ='collectFromObjectAndStore', startPosition=[self.y, self.x, self.direction])
                self.used = True
