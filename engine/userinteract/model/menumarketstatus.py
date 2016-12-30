from engine.userinteract.model.base import base
from engine.userinteract.helper import helper as uihelper

import settings

class menumarketstatus(base):
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
        self.addCommon(uid='coverall', color=(51,51,51))

    #--------------------------------------------------
    #  Assign Outputs
    #--------------------------------------------------
    def addOutputs(self):
        # UI
        self.addOutput(pos=[10, 10], type='text', priority=2, attribute={
           'font': 'primaryFont',
           'size': 50,
           'value': 'Global Market',
           'color': (255, 255, 255)
        })

        basey = 50
        limit = 10
        current = 0

        for each in settings.webinteract['market'].getDemand():
            if (current <= limit):
                # Show market item
                self.addOutput(pos=[basey, 10], type='text', priority=2, attribute={
                   'font': 'primaryFont',
                   'size': 30,
                   'value': str(each['itemid']) + ' : ' + str(each['current_demand_addition']),
                   'color': (255, 255, 255)
                })
                current += 1
                basey += 30
            else:
                break