import pygame

import settings
from engine.userinteract.helper import helper as uihelper
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


        else:
            # Assume wants object
            if (shop.canPurchase(result.price)):
                return result

        return False

class base:
    def setVars(self, **kwargs):
        # base, image, direction, tickListen
        # Init Boilerplate
        self.highlighted = False
        self.tickCount = 0

        # Load Vars
        provided = settings.objectDB[self.type][self.title]

        defaults = {
            'devOverlay': 0,
            'tickListen': [],
        }

        for key, value in provided.items():
            setattr(self, key, value)

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key, value in defaults.items():
            if not(hasattr(self, key)):
                #Set default
                setattr(self, key, value)

        self.image = self.load(self.image)

        if(hasattr(self, 'base')):
            self.base = self.load(self.base)

        # Set tick vars
        if(hasattr(self, 'tickListen') & hasattr(self, 'y')):
            # Needs registered ticks, hasPosition
            self.registerTicks()

    def registerTicks(self):
        for each in self.tickListen:
            settings.tick.register(each, 'settings.grid[' + str(self.y) + '][' + str(self.x) + '].tick()')



    def load(self, spriteID):
        stmt = 'sprites/'+str(spriteID)+'.png'
        return pygame.image.load(stmt)

    def setPathDev(self,g,h,f):
        self.devOverlay = [g,h,f]

    def highlightAdd(self, direction):
        self.highlighted = True
        self.highlightedDirection = direction

    def highlight(self):
        directions = {
            0:'UP',
            1:'RI',
            2:'DO',
            3:'LF',
            4:'4'
        }
        pygame.draw.rect(settings.surface, (255,0,0), [self.x*50,self.y*50,50,50])
        settings.surface.blit(settings.fonts['primaryFont'][30].render(directions[self.highlightedDirection], True, (255,255,255)), [self.x*50,self.y*50,50,50])

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

            #print(self.tickCount)
            #TODO ticks not being reset

    def hasInventory(self):
        if(hasattr(self, 'inventory')):
            return True

class factory_parts(base):
    def __init__(self, **kwargs):
        super(factory_parts, self).__init__()
        self.title = 'factory_parts'
        self.type = 'producer'
        self.part = 0
        super(factory_parts, self).setVars(image=self.title, **kwargs)

        self.passable = []
        self.inventory = inventory(30)
        self.inventoryOutput = inventory(30)
        self.status = 0
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

            if(self.setSegregation == False):
                if (not settings.itemDB[self.part]['required'] == {}):
                    self.inventory.segregate(list(settings.itemDB[self.part]['required'].keys()))
                    self.setSegregation = True


            if(settings.itemDB[self.part]['required']=={}):
                # Just generate Parts
                print('JUST GENERATING')
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


            if (not self.inventoryOutput.isFull()):
                self.image = self.load(self.title)
            else:
                self.image = self.load(self.title + '_full')
                # TODO fix force pick
                if (self.jobcollectcreated == False):
                    jobset.create(typ='collectFromObjectAndStore', startPosition=[self.y, self.x, self.direction],
                              itemID=self.inventoryOutput.getInventory()[0].id)

                    self.jobcollectcreated = True

                print(settings.activeJobsetDB)

    def eventClick(self):
        settings.activeModelDB[settings.activeUI['factorypartsmenu']].objectPosition = [self.y,self.x]
        uihelper.toggleModel('factorypartsmenu', True)


class factory_base(base):
    def __init__(self):
        self.part = 0
        self.type = 'processor'

        self.passable = []
        self.inventory = inventory(30)
        self.inventoryOutput = inventory(30)
        self.status = 0
        self.ui = ''
        self.counter = 0
        self.jobCreated = False
        self.setSegregation = False
        self.speedLevel = 0

    def doTick(self, tickID):
        if (tickID == 0):
            if (self.part == 0):
                # No specified output, check inventory.
                for each in self.inventory.getInventory():
                    pass


            # Output was specified
            data = settings.itemDB[self.part]

            # Verify required items are in inventory
            hasItems = 0
            for name, quantity in data['required'].items():
                if (self.inventory.has(name, quantity)):
                    hasItems += 1

            if ((len(data['required'])) == hasItems):
                # Has Required items
                # Get Items To Remove
                toRemove = settings.itemDB[self.part]['required']

                # Remove Items
                for key, quantity in toRemove.items():
                    self.inventory.removeItem(id=key, quantity=quantity)

                self.inventoryOutput.addItem(self.part, settings.itemDB[self.part]['makes'] *
                                             settings.objectDB['producer']['factory_parts']['speed_upgrades_modifier'][
                                                 self.speedLevel])
            else:
                # Does not have required items
                if (self.status != 2):
                    # 2 means waiting, but job waitforitems created
                    self.job = jobset.create(typ='waitForItems', position=[self.y, self.x], items=data['required'])
                    self.status = 2

            if (self.inventoryOutput.isFull()):
                jobset.create(typ='collectFromObjectAndStore', startPosition=[self.y, self.x, self.direction],
                              itemID=self.inventoryOutput.getInventory('all')[0].id)

            if (not self.inventoryOutput.isFull()):
                self.image = self.load(self.title)

            else:
                self.image = self.load(self.title + '_full')

                # TODO fix force pick
                jobset.create(typ='collectFromObjectAndStore', startPosition=[self.y, self.x, self.direction],
                              itemID=self.inventoryOutput.getInventory()[0].id)


class factory_press(factory_base):
    def __init__(self, **kwargs):
        self.title = 'factory_press'
        self.process = 'press'
        self.part = 'bronzecoin'

        super(factory_press, self).__init__()
        super(factory_press, self).setVars(image=self.title, **kwargs)

        self.job = jobset.create(typ='waitForItems', position=[self.y, self.x], items={'metalcopper':1})

    def eventClick(self):
        settings.activeModelDB[settings.activeUI['factorypartsmenu']].objectPosition = [self.y,self.x]
        uihelper.toggleModel('factorypartsmenu', True)



class empty(base):
    def __init__(self, **kwargs):
        self.type = 'placeholder'
        self.title = 'empty'
        super(empty, self).setVars(image = 'empty', base='empty', **kwargs)
        self.passable = []

    def eventClick(self):
        pass

class exports(base):
    def __init__(self, **kwargs):
        self.type = 'exports'
        self.title = 'exports'

        super(exports, self).setVars(image=self.title, **kwargs)

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

        super(garage, self).setVars(image=self.title, **kwargs)

        self.passable = []
        self.inventory = inventory(10, 'vehicle')
        self.price = 50000


    def eventClick(self):
        pass

class genericHouse(base):
    def __init__(self, **kwargs):
        self.type = 'storage'
        self.title = 'genericHouse'

        super(genericHouse, self).setVars(image = 'genericHouse', **kwargs)

        self.passable = []
        self.inventory = inventory(20)
        self.price = 200

    def eventClick(self):
        super(genericHouse, self).log()

class road(base):
    def __init__(self, **kwargs):
        self.type = 'transport'
        self.title = 'road'
        super(road, self).setVars(image='road', **kwargs)
        self.passable = [5]

    def eventClick(self):
        pass