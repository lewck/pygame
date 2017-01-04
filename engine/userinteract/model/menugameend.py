from engine.userinteract.model.base import base

import settings

class menugameend(base):
    def __init__(self, **kwargs):
        self.basePriority = 999
        self.basePos = [0,0]
        self.baseDim = [550,1050]

        base.__init__(self, **kwargs)

    #--------------------------------------------------
    #  Assign Inputs
    #--------------------------------------------------
    def addInputs(self):
        self.addCommon(uid='coverall', color=(51,51,51))

    #--------------------------------------------------
    #  Assign Outputs
    #--------------------------------------------------
    def addOutputs(self):
        # Title
        self.addOutput(pos=[80,425], type='text', priority=2, attribute={
            'font': 'primaryFont',
            'size': 60,
            'value': 'Game Over!',
            'color': (255, 255, 255)
        })

        if(hasattr(self, 'winstatus')):
            # Show Win / Loose UI
            if(self.winstatus == True):
                self.addOutput(pos=[140, 450], type='text', priority=2, attribute={
                    'font': 'primaryFont',
                    'size': 60,
                    'value': 'You Win!',
                    'color': (0, 255, 0)
                })
            else:
                self.addOutput(pos=[140, 450], type='text', priority=2, attribute={
                    'font': 'primaryFont',
                    'size': 60,
                    'value': 'You Lose!',
                    'color': (255, 0, 0)
                })