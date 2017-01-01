from engine.userinteract.model.base import base
from engine.userinteract.helper import helper as uihelper
from shop import shop
from item.helper import helper as itemhelper

import settings

class menuunlock(base):
    def __init__(self, **kwargs):
        self.basePriority = 80
        self.basePos = [0, 0]
        self.baseDim = [512, 512]

        base.__init__(self, **kwargs)

    #--------------------------------------------------
    #  Assign Inputs
    #--------------------------------------------------
    def addInputs(self):
        self.addCommon(uid='close', pos=[0, 512])
        self.addCommon(uid='coverall', color=(51, 51, 51))

    #--------------------------------------------------
    #  Assign Outputs
    #--------------------------------------------------
    def addOutputs(self):
        self.addOutput(pos=[10, 10], type='text', priority=2, attribute={
           'font': 'primaryFont',
           'size': 50,
           'value': 'Unlock Menu',
           'color': (255, 255, 255)
        })

        basey = 50
        for key, each in settings.itemDB.items():
            if('discovered' in each):
                # Non compound object
                if(self.renderDiscovered(basey, key, each)):
                    basey += 50
            else:
                # Compound Object
                for keySub, eachSub in each['type'].items():
                    if(self.renderDiscovered(basey, key, eachSub, keySub)):
                        basey += 50

    #--------------------------------------------------
    #  Model-Specific Functionality
    #--------------------------------------------------
    def unlockItem(self, itemID, type=None):
        unlockPrice = itemhelper.getPrice(itemID, type)

        if (shop.canPurchase(unlockPrice)):
            shop.purchase(unlockPrice)


            itemhelper.discover(itemID, type)
            uihelper.toggleModel('menuunlock', True)

    def renderDiscovered(self, basey, identifier, data, type=None):
        if (data['discovered']):
            return False

        # Show Price
        self.addOutput(pos=[basey, 10], type='text', priority=2, attribute={
           'font': 'primaryFont',
           'size': 30,
           'value': str(data['title']) + '   Price: ' + str(data['unlockPrice']),
           'color': (255, 0, 0)
       })

        # UI
        self.addOutput(pos=[basey, 400], type='shape', priority=2,attribute={
           'shape': 'rectangle',
           'dim': [50, 50],
           'color': (255, 255, 0)
        })
        self.addOutput(pos=[basey, 400], type='text', priority=5, attribute={
           'font': 'primaryFont',
           'size': 20,
           'value': 'Buy',
           'color': (0, 0, 0)
        })
        self.addInput(type='mouseAction', priority=5, attribute={
            'click': 1,
            'pos': [basey, 400],
            'dim': [50, 50],
            'event': 'unlockItem',
            'eventArgs': [str(identifier), type],
        })

        return True