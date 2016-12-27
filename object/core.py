import pygame

import settings
from engine.userinteract.helper import helper as uihelper
from engine.helper import helper as enginehelper
from inventory import inventory
from jobset import factory as jobset
from shop import shop


class factory:
    @staticmethod
    def getObject(**kwargs):
        results = eval(kwargs['uid'] + '(**kwargs)')
        return results

    @staticmethod
    def create(**kwargs):
        if('obj' in kwargs):
            result = kwargs['obj']
        else:
            result = factory.getObject(**kwargs)

        # Is item being placed?
        if 'y' in kwargs:
            if not (hasattr(result, 'base')):
                # Use existing base
                result.base = settings.grid[kwargs['y']][kwargs['x']].base
            # Assume needs plot
            if 'dev' in kwargs:
                # Force Create
                settings.grid[kwargs['y']][kwargs['x']] = result
                return True

            else:
                # Check balance etc
                if (shop.canPurchase(result.price)):
                    shop.purchase(result.price)
                    settings.grid[kwargs['y']][kwargs['x']] = result
                    return True
                else:
                    return False

        # Assume wants object response
        if (shop.canPurchase(result.price)):
            return result
        return False

class base:
    def __init__(self):
        # Init Boilerplate
        self.highlighted = False
        self.tickCount = 0
        self.part = 0
        self.passable = []

        self.inventory = inventory(30)
        self.inventoryOutput = inventory(30)

        self.status = 0
        self.ui = ''
        self.counter = 0
        self.jobCreated = False
        self.setSegregation = False
        self.speedLevel = 0

    def setVars(self, **kwargs):
        # Get and set provided vars
        provided = settings.objectDB[self.type][self.title]
        self.details = provided
        self.tickListen = provided['tickListen']
        self.price = provided['price']
        self.image = enginehelper.loadImage(self.title)

        if('base' in kwargs):
            self.base = enginehelper.loadImage(kwargs['base'])

        if('y' in kwargs):
            self.y = kwargs['y']
            self.x = kwargs['x']
            self.direction = kwargs['direction']

            # Needs registered ticks, hasPosition
            for each in self.tickListen:
                settings.tick.register(each, 'settings.grid[' + str(self.y) + '][' + str(self.x) + '].tick()')

    def setPathDev(self,g,h,f):
        self.devOverlay = [g,h,f]

    def highlightAdd(self, direction):
        self.highlighted = True
        self.highlightedDirection = direction

    def highlight(self):
        image = enginehelper.loadImage('highlight')
        directionModifier = {
            0: 180,
            1: 90,
            2: 0,
            3: 270,
            4: 0,
        }

        image = pygame.transform.rotate(image, directionModifier[self.highlightedDirection])

        settings.surface.blit(pygame.transform.scale(image, (50, 50)), (self.x*50,self.y*50))


    def isPassible(self, entityid):
        if(entityid in self.passable):
            return True
        return False

    def tick(self):
        self.tickCount += 1
        for i in range(0, len(self.tickListen)):
            if (self.tickCount % self.tickListen[i] == 0):
                self.doTick(i)
                if(i==len(self.tickListen)):
                    self.tickCount = 0

            # print(self.tickCount)
            # TODO ticks not being reset

    def hasInventory(self):
        if(hasattr(self, 'inventory')):
            return True

    def checkFullInventory(self):
        if (not self.inventoryOutput.isFull()):
            self.image = enginehelper.loadImage(self.title)
            self.jobcollectcreated = False

        else:
            self.image = enginehelper.loadImage(self.title + '_full')

            # TODO fix force pick
            if (self.jobcollectcreated == False):
                jobset.create(typ='collectFromObjectAndStore', startPosition=[self.y, self.x, self.direction],
                              itemID=self.inventoryOutput.getInventory()[0].id)

                self.jobcollectcreated = True

class factory_parts(base):
    def __init__(self, **kwargs):
        self.title = 'factory_parts'
        self.type = 'producer'

        base.__init__(self)
        base.setVars(self, **kwargs)

        self.ui = ''
        self.counter = 0
        self.jobCreated = False
        self.setSegregation = False
        self.speedLevel = 0
        self.jobcollectcreated = False


    def doTick(self, tickID):
        if (tickID == 0):
            if(self.part==0):
                # No part assigned
                return False

            self.checkFullInventory()

            if(self.setSegregation == False):
                if (not settings.itemDB[self.part]['required'] == {}):
                    self.inventory.segregate(list(settings.itemDB[self.part]['required'].keys()))
                    self.setSegregation = True


            if(settings.itemDB[self.part]['required']=={}) & (not self.inventoryOutput.isFull()):
                # Just generate Parts
                self.inventoryOutput.addItem(self.part,settings.itemDB[self.part]['makes']*settings.objectDB['producer']['factory_parts']['speed_upgrades_modifier'][self.speedLevel])

            else:
                # Assume has to check inventory for parts
                data = settings.itemDB[self.part]

                hasItems = 0

                for name, quantity in data['required'].items():
                    if(self.inventory.has(name, quantity)):
                        hasItems += 1

                if((len(data['required'])) == hasItems):
                    # Get Items To Remove
                    toRemove = settings.itemDB[self.part]['required']

                    # Remove Items
                    for key, quantity in toRemove.items():
                        self.inventory.removeItem(id=key, quantity=quantity)

                    self.inventoryOutput.addItem(self.part, settings.itemDB[self.part]['makes'] *settings.objectDB['producer']['factory_parts']['speed_upgrades_modifier'][self.speedLevel])

                else:
                    if(self.status != 2):
                        # 2 means waiting, but job waitforitems created
                        self.job = jobset.create(typ='waitForItems', position=[self.y, self.x], items=data['required'])
                        self.status = 2

    def eventClick(self):
        settings.activeModelDB[settings.activeUI['factorypartsmenu']].objectPosition = [self.y,self.x]
        uihelper.toggleModel('factorypartsmenu', True)

class processor_base(base):
    def __init__(self):
        self.type = 'processor'
        base.__init__(self)

    def doTick(self, tickID):
        if (tickID == 0):
            # Handle Full Inventory
            self.checkFullInventory()

            if(self.inventory.getInventory()):
                # Has some items
                for each in self.inventory.getInventory():
                    toProduce = settings.processingDB[self.process]['transformations'][each.id]
                    if(self.inventory.has(each.id, toProduce['required'])):
                        # Has required quantity
                        items = self.inventory.takeItem(each.id, toProduce['required'])
                        for prodKey, prodQuant in toProduce['produces'].items():
                            self.inventoryOutput.addItem(prodKey, prodQuant)
                            print(self.inventoryOutput.getInventory())
            return False

class producer_base(base):
    def __init__(self):
        self.type = 'producer'
        self.itemID = None

        base.__init__(self)

    def doTick(self, tickID):
        if (tickID == 0):
            if(self.itemID):
                #print(self.details['speed_upgrades_modifier'][self.speedLevel])

                self.inventoryOutput.addItem(self.itemID, settings.itemDB[self.itemID]['makes'] *
                                            self.details['speed_upgrades_modifier'][
                                                 self.speedLevel])

                print(len(self.inventoryOutput.getInventory()))



            else:
                print('NOID')

class factory_miner(producer_base):
    def __init__(self, **kwargs):
        self.title = 'factory_miner'
        producer_base.__init__(self)
        producer_base.setVars(self, **kwargs)
        self.itemID = 'metalCopper'

class factory_press(processor_base):
    def __init__(self, **kwargs):
        self.title = 'factory_press'
        self.process = 'press'
        self.part = 'bronzecoin'

        processor_base.__init__(self)
        processor_base.setVars(self, image=self.title, **kwargs)


    def eventClick(self):
        settings.activeModelDB[settings.activeUI['factorypartsmenu']].objectPosition = [self.y,self.x]
        uihelper.toggleModel('factorypartsmenu', True)

class factory_puncher(processor_base):
    def __init__(self, **kwargs):
        self.title = 'factory_puncher'
        self.process = 'puncher'
        self.part = 'bronzecoin'

        processor_base.__init__(self)
        processor_base.setVars(self, image=self.title, **kwargs)

    def eventClick(self):
        settings.activeModelDB[settings.activeUI['factorypartsmenu']].objectPosition = [self.y,self.x]
        uihelper.toggleModel('factorypartsmenu', True)


#===========================================================================
#  Non-factory objects
#==============================================================
#  Empty Object
#--------------------------------------------------

class empty(base):
    def __init__(self, **kwargs):
        self.type = 'placeholder'
        self.title = 'empty'
        base.__init__(self)
        base.setVars(self, base='empty', **kwargs)
        self.passable = []

    def eventClick(self):
        pass

class exports(base):
    def __init__(self, **kwargs):
        self.type = 'exports'
        self.title = 'exports'

        base.__init__(self)
        base.setVars(self,**kwargs)

        self.passable = []
        self.inventory = inventory(500)
        self.price = 500
        self.tickListen = [5]

    def doTick(self, tickID):
        if(tickID==0):
            if(self.inventory.hasAny()):
                toSell = self.inventory.takeItem('all', 'all')
                shop.sell(toSell)

    def eventClick(self):
        pass

class garage(base):
    def __init__(self, **kwargs):
        self.type = 'storageVehicles'
        self.title = 'garage'

        base.__init__(self)
        base.setVars(self, **kwargs)

        self.passable = []
        self.inventory = inventory(10, 'vehicle')
        self.price = 50000


    def eventClick(self):
        pass

class genericHouse(base):
    def __init__(self, **kwargs):
        self.type = 'storage'
        self.title = 'genericHouse'

        base.__init__(self)
        base.setVars(self, **kwargs)

        self.passable = []
        self.inventory = inventory(20)
        self.price = 200

    def eventClick(self):
        super(genericHouse, self).log()

class road(base):
    def __init__(self, **kwargs):
        self.type = 'transport'
        self.title = 'road'
        base.__init__(self)
        base.setVars(self, **kwargs)
        self.passable = [5]

    def eventClick(self):
        pass