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
        self.inventoryOutput = inventory(30)
        self.status = 0
        self.used = False
        self.part = 0

    def doTick(self, tickID):

        if(tickID==0):
            #chance grow increase
            if(not self.inventory.isFull()):
                self.image = self.load(self.title)


        if (tickID == 1):
            if(self.part ==0):
                #No part assigned
                return False
            if(settings.itemDB[self.part]['required']=={}):

                if(self.inventoryOutput.addItem('body',5)=='INVFULL') & (self.used==False):
                    print('I AM FULL, CREATING JOB')
                    print(self.inventoryOutput.inventory[0].id)

                    self.image = self.load(self.title+'_full')

                    jobset.create(typ='collectFromObjectAndStore', startPosition=[self.y, self.x, self.direction], itemID=self.inventoryOutput.inventory[0].id)

                    print('AFTER JOBSET CREATED')
                    print(settings.activeJobsetDB)
                    self.used = True

            else:

                #Assume has to check inventory for parts
                data = settings.itemDB[self.part]

                hasItems = 0

                for name, quantity in data['required'].items():
                    if(self.inventory.has(name, quantity)):
                        hasItems += 1

                '''

                print('dbg')
                print(data['required'])
                print(self.inventory.inventory)

                print(len(data['required']))
                print(hasItems)

                print(len(self.inventoryOutput.inventory))
                print('^outlenm')
                print(len(self.inventory.inventory))
                print('^inLength')

                '''

                if((len(data['required'])) == hasItems):
                    print('CAN CONSTRUCT PLANE')


                    toRemove = settings.itemDB[self.part]['required']
                    print(toRemove)

                    for key, quantity in toRemove.items():
                        self.inventory.removeItem(id=key, quantity=quantity)


                    self.inventoryOutput.addItem(self.part, 1)


                else:
                    if(self.status != 2):
                        #2 means waiting, but job created
                        self.job = jobset.create(typ='waitForItems', position=[self.y, self.x], items=data['required'])
                        self.status = 2

                if(self.inventoryOutput.isFull()):
                    jobset.create(typ='collectFromObjectAndStore', startPosition=[self.y, self.x, self.direction],
                                  itemID=self.inventoryOutput.inventory[0].id)




    def eventClick(self):
        print('CLICKEED ON ME')