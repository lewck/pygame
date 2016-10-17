from object.base import base
from inventory import inventory
from jobset.factory import factory as jobset
import settings


class factory_parts(base):
    def __init__(self, **kwargs):
        self.title = 'factory_parts'
        self.type = 'producer'

        super(factory_parts, self).setVars(image=self.title, **kwargs)
        self.passable = []
        self.inventory = inventory(30)
        self.status = 0
        self.used = False

    def doTick(self, tickID):

        if(tickID==0):
            #chance grow increase
            if(not self.inventory.isFull()):
                self.image = self.load(self.title)


        if (tickID == 1):
            if(self.inventory.addItem('vegetableCarrot',8)=='INVFULL') & (self.used==False):

                self.image = self.load(self.title+'_full')

                jobset.create(typ='collectFromObjectAndStore', startPosition=[self.y, self.x, self.direction])
                self.used = True
