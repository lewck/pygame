from engine.userinteract.model.base import base

import settings

class menuloading(base):
    def __init__(self, **kwargs):
        self.basePriority = 120
        self.basePos = [0,0]
        self.baseDim = [550,1050]

        base.__init__(self, **kwargs)

    #--------------------------------------------------
    #  Assign Inputs
    #--------------------------------------------------
    def addInputs(self):
        self.addCommon(uid='coverall', color=(255,255,255))

    #--------------------------------------------------
    #  Assign Outputs
    #--------------------------------------------------
    def addOutputs(self):
        # Loading text
        self.addOutput(pos=[250,400], type='text', priority= 2, attribute={
            'font': 'primaryFont',
            'size': 60,
            'value': 'LOADING...',
            'color': (0, 0, 0)
        })