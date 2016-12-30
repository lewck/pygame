from engine.userinteract.model.base import base
from engine.userinteract.helper import helper as uihelper

import settings

class menustart(base):
    def __init__(self, **kwargs):
        self.basePriority = 110
        self.basePos = [0,0]
        self.baseDim = [550,1050]

        base.__init__(self, **kwargs)

    #--------------------------------------------------
    #  Assign Inputs
    #--------------------------------------------------
    def addInputs(self):
        self.addCommon(uid='coverall')
        # New game button
        self.addInput(type='mouseAction', priority=5, attribute={
            'click': 1,
            'pos': [300, 400],
            'dim': [50,250],
            'event': 'createGame',
        })
        # Join game button
        self.addInput(type='mouseAction', priority=5, attribute={
            'click': 1,
            'pos': [400, 400],
            'dim': [50, 250],
            'event': 'joinGame',
        })

    #--------------------------------------------------
    #  Assign Outputs
    #--------------------------------------------------
    def addOutputs(self):
        # UI
        self.addOutput(pos=[80,425], type='text', priority= 2, attribute={
            'font': 'primaryFont',
            'size': 60,
            'value': 'Welcome',
            'color': (255, 255, 255)
        })
        self.addOutput(pos=[50, 425], type='image', priority=6, attribute={
            'uid': 'icon',
            'scale': (200, 200)
        })

        # Start new game button
        self.addOutput(pos=[300, 400], type='shape', priority=2, attribute={
            'shape': 'rectangle',
            'dim': [50,250],
            'color': (255, 0, 0)
        })
        self.addOutput(pos=[312, 445], type='text', priority=3, attribute={
            'font': 'primaryFont',
            'size': 30,
            'value': 'Start New Game',
            'color': (255, 255, 255)
        })

        # Join game button
        self.addOutput(pos=[400, 400], type='shape', priority=2, attribute={
            'shape': 'rectangle',
            'dim': [50, 250],
            'color': (255, 0, 0)
        })
        self.addOutput(pos=[412, 445], type='text', priority=3, attribute={
            'font': 'primaryFont',
            'size': 30,
            'value': 'Join A Game',
            'color': (255, 255, 255)
        })
        self.addOutput(pos=self.basePos, type='shape', attribute={
            'shape': 'rectangle',
            'dim': self.baseDim,
            'color': (255,255,255)
        })

    #--------------------------------------------------
    #  Model-Specific Functionality
    #--------------------------------------------------
    def createGame(self):
        # Toggle to create game menu
        uihelper.toggleModel('menustart')
        uihelper.toggleModel('gamesettings')

    def joinGame(self):
        uihelper.toggleModel('menustart')
        uihelper.toggleModel('menujoingame')