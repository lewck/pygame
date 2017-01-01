from engine.userinteract.model.base import base
from engine.userinteract.helper import helper as uihelper
from engine.userinteract.ui import ui
from shop import shop
import settings

class factoryminermenu(base):
    def __init__(self, **kwargs):
        self.basePriority = 60
        self.basePos = [0,0]
        self.baseDim = [512,512]

        base.__init__(self, **kwargs)

    #--------------------------------------------------
    #  Assign Inputs
    #--------------------------------------------------
    def addInputs(self):
        self.addCommon(uid='close', pos=[0, 512])
        self.addCommon(uid='coverall', color=(0, 0, 0))

        # Open Part Select menu
        self.addInput(type='mouseAction', priority=5, attribute={
            'click': 1,
            'pos': [50, 110],
            'dim': [40, 70],
            'event': 'createPartSelect',
        })

        # Speed upgrade button
        self.addInput(type='mouseAction', priority=5, attribute={
            'click': 1,
            'pos': [90, 170],
            'dim': [40, 70],
            'event': 'doSpeedUpgrade',
        })

    #--------------------------------------------------
    #  Assign Outputs
    #--------------------------------------------------
    def addOutputs(self):
        # Title
        self.addOutput(pos=[10, 10], type='text', priority=2, attribute={
           'font': 'primaryFont',
           'size': 50,
           'value': 'Miner Menu',
           'color': (255, 255, 255)
        })

        self.addOutput(pos=[100, 10], type='text', priority=5, attribute={
           'font': 'primaryFont',
           'size': 30,
           'value': 'Speed Upgrade:  '+str(self.getSpeedUpgradePrice()),
           'color': (255, 255, 255)
        })

        self.addOutput(pos=[90, 170], type='shape', priority=4,attribute={
           'shape': 'rectangle',
           'dim': [40, 70],
           'color': (255, 0, 0)
        })

        if(hasattr(self, 'objectPosition')):
            # Object is placed

            # Draw Part
            if(settings.grid[self.objectPosition[0]][self.objectPosition[1]].itemID != 0):
                text = settings.grid[self.objectPosition[0]][self.objectPosition[1]].itemID
            else:
                text = 'Select'

            self.addOutput(pos=[60, 10], type='text', priority=5, attribute={
                   'font': 'primaryFont',
                   'size': 30,
                   'value': 'Part ID    : '+str(text),
                   'color': (255, 255, 255)
            })

    #--------------------------------------------------
    #  Model-Specific Functionality
    #--------------------------------------------------
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
                uihelper.toggleModel(self.id)

    def createPartSelect(self):
        x = ui.create('factorypartsselectpart', 2)
        uihelper.updateAttribute(x,'objectPosition', self.objectPosition)
        uihelper.reloadModel(x)