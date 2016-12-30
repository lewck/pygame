from engine.userinteract.model.base import base
from engine.userinteract.model.menuproducerbuy import menuproducerbuy
from engine.userinteract.helper import helper as uihelper
from shop import shop

import settings

class factorypartsmenu(base):
    def __init__(self, **kwargs):
        self.basePriority = 70
        self.title = 'factory'

        base.__init__(self, **kwargs)

    def getSpeedUpgradePrice(self):
        try:
            obj = settings.grid[self.objectPosition[0]][self.objectPosition[1]]

            if(obj.speedLevel+1 in settings.objectDB['producer']['factory_parts']['speed_upgrades']):
                return settings.objectDB['producer']['factory_parts']['speed_upgrades'][obj.speedLevel+1]
        except AttributeError:
            # Assume model not yet assigned to a item, so function will not be called
            pass

    def doSpeedUpgrade(self):
        obj = settings.grid[self.objectPosition[0]][self.objectPosition[1]]

        if (obj.speedLevel + 1 in settings.objectDB['producer']['factory_parts']['speed_upgrades']):
            if (shop.canPurchase(settings.objectDB['producer']['factory_parts']['speed_upgrades'][obj.speedLevel + 1])):
                shop.purchase(settings.objectDB['producer']['factory_parts']['speed_upgrades'][obj.speedLevel + 1])
                obj.speedLevel += 1
                uihelper.toggleModel('factorypartsmenu')

    def createPartSelect(self):
        uihelper.updateAttribute('factorypartsselectpart','objectPosition', self.objectPosition)
        uihelper.toggleModel('factorypartsselectpart')

    def addInputs(self):
        self.addInput(type='mouseAction', priority=5, title='openBuyMenu', attribute={
            'click': 1,
            'pos': [50, 110],
            'dim': [40, 70],
            'event': 'createPartSelect',
        })
        self.addInput(type='mouseAction', priority=5, title='attemptSpeedUpgrade', attribute={
            'click': 1,
            'pos': [90, 170],
            'dim': [40, 70],
            'event': 'doSpeedUpgrade',
        })
        self.addCommon(uid='close', pos=[0, 512])

    def addOutputs(self):
        self.addOutput(pos=[10, 10], type='text', priority=2, title='factoryparttitle',
            attribute={
               'font': 'primaryFont',
               'size': 50,
               'value': 'Factory Menu',
               'color': (255, 255, 255)
           }
        )

        self.addOutput(pos=[0,0], type='shape', priority=0, title='factoryPartBackground',
            attribute={
                'shape': 'rectangle',
                'dim': [512, 512],
                'color': (0, 0, 0)
            }
        )

        self.addOutput(pos=[100, 10], type='text', priority=5, title='factoryparttitle',
           attribute={
               'font': 'primaryFont',
               'size': 30,
               'value': 'Speed Upgrade:  '+str(self.getSpeedUpgradePrice()),
               'color': (255, 255, 255)
           }
        )
        self.addOutput(pos=[90, 170], type='shape', priority= 4, title='factoryparttitle',
                       attribute={
                           'shape': 'rectangle',
                           'dim': [40, 70],
                           'color': (255, 0, 0)
                       }
                       )

        if(hasattr(self, 'objectPosition')):
            # Assume claimed

            # Draw Part
            if(settings.grid[self.objectPosition[0]][self.objectPosition[1]].part != 0):
                text = settings.grid[self.objectPosition[0]][self.objectPosition[1]].part
            else:
                text = 'Select'



            self.addOutput(pos=[60, 10], type='text', priority= 5, title='factoryparttitle',
               attribute={
                   'font': 'primaryFont',
                   'size': 30,
                   'value': 'Part ID    : '+str(text),
                   'color': (255, 255, 255)
               }
            )



    def load(self, pos):
        self.objectPosition = pos

        self.refresh()