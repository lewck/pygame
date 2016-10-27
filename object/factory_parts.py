from object.base import base
from inventory import inventory
from jobset.factory import factory as jobset
from engine.userinteract.helper import helper as uihelper


import settings


class factory_parts(base):
    def __init__(self, **kwargs):
        self.title = 'factory_parts'
        self.type = 'producer'
        self.part = 0
        super(factory_parts, self).setVars(image=self.title, **kwargs)
        self.passable = []
        self.inventory = inventory(30)
        self.inventoryOutput = inventory(30)
        self.status = 0
        self.used = False
        self.ui = ''
        self.counter = 0
        self.jobCreated = False


    def doTick(self, tickID):

        if(tickID==0):
            #chance grow increase
            pass


        if (tickID == 1):

            if(self.part==0):
                #No part assigned
                return False


            if(settings.itemDB[self.part]['required']=={}):
                #Just generate Parts
                self.inventoryOutput.addItem(self.part,5)
                print(self.inventoryOutput.inventory)
                print('ADDING')

            else:

                #Assume has to check inventory for parts
                data = settings.itemDB[self.part]

                hasItems = 0

                for name, quantity in data['required'].items():
                    if(self.inventory.has(name, quantity)):
                        hasItems += 1

                if((len(data['required'])) == hasItems):
                    print('CAN CONSTRUCT PLANE')


                    toRemove = settings.itemDB[self.part]['required']
                    print(toRemove)

                    for key, quantity in toRemove.items():
                        self.inventory.removeItem(id=key, quantity=quantity)


                    self.inventoryOutput.addItem(self.part, 1)


                else:
                    if(self.status != 2):
                        #2 means waiting, but job waitforitems created
                        self.job = jobset.create(typ='waitForItems', position=[self.y, self.x], items=data['required'])
                        self.status = 2

                if(self.inventoryOutput.isFull()):
                    jobset.create(typ='collectFromObjectAndStore', startPosition=[self.y, self.x, self.direction],
                                  itemID=self.inventoryOutput.inventory[0].id)


            if (not self.inventoryOutput.isFull()):
                self.image = self.load(self.title)

            else:
                self.image = self.load(self.title + '_full')


                print('I AM FULL, CREATING JOB')
                print(self.inventoryOutput.inventory[0].id)



                jobset.create(typ='collectFromObjectAndStore', startPosition=[self.y, self.x, self.direction],
                              itemID=self.inventoryOutput.inventory[0].id)

                print('AFTER JOBSET CREATED')
                print(settings.activeJobsetDB)


    def eventClick(self):
        settings.activeModelDB[settings.activeUI['factorypartsmenu']].objectPosition = [self.y,self.x]
        uihelper.toggleModel('factorypartsmenu', True)