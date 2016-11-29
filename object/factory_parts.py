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
        self.setSegregation = False
        self.speedLevel = 0


    def doTick(self, tickID):

        if(tickID==0):
            # Chance grow increase
            pass


        if (tickID == 1):

            if(self.part==0):
                #No part assigned
                return False

            else:
                if(self.setSegregation == False):
                    if (not settings.itemDB[self.part]['required'] == {}):
                        self.inventory.segregate(list(settings.itemDB[self.part]['required'].keys()))
                        self.setSegregation = True


            if(settings.itemDB[self.part]['required']=={}):
                #Just generate Parts
                self.inventoryOutput.addItem(self.part,settings.itemDB[self.part]['makes']*settings.objectDB['producer']['factory_parts']['speed_upgrades_modifier'][self.speedLevel])

            else:
                #Assume has to check inventory for parts
                data = settings.itemDB[self.part]

                hasItems = 0

                for name, quantity in data['required'].items():
                    if(self.inventory.has(name, quantity)):
                        hasItems += 1

                if((len(data['required'])) == hasItems):

                    #Get Items To Remove
                    toRemove = settings.itemDB[self.part]['required']

                    #Remove Items
                    for key, quantity in toRemove.items():
                        self.inventory.removeItem(id=key, quantity=quantity)

                    self.inventoryOutput.addItem(self.part, settings.itemDB[self.part]['makes'] *settings.objectDB['producer']['factory_parts']['speed_upgrades_modifier'][self.speedLevel])


                else:
                    if(self.status != 2):
                        #2 means waiting, but job waitforitems created
                        self.job = jobset.create(typ='waitForItems', position=[self.y, self.x], items=data['required'])
                        self.status = 2

                if(self.inventoryOutput.isFull()):
                    jobset.create(typ='collectFromObjectAndStore', startPosition=[self.y, self.x, self.direction],
                                  itemID=self.inventoryOutput.getInventory('all')[0].id)


            if (not self.inventoryOutput.isFull()):
                self.image = self.load(self.title)

            else:
                self.image = self.load(self.title + '_full')


                #TODO fix force pick
                jobset.create(typ='collectFromObjectAndStore', startPosition=[self.y, self.x, self.direction],
                              itemID=self.inventoryOutput.getInventory()[0].id)


    def eventClick(self):
        settings.activeModelDB[settings.activeUI['factorypartsmenu']].objectPosition = [self.y,self.x]
        uihelper.toggleModel('factorypartsmenu', True)