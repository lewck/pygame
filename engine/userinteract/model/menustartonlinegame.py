'''
'
'   NB correct class naming convention: modeltype subtype action
'
'''

from engine.userinteract.model.base import base
from engine.userinteract.helper import helper as uihelper

import settings

class menustartonlinegame(base):
    def __init__(self, **kwargs):
        self.basePriority = 120
        self.basePos = [0,0]
        self.baseDim = [550,1050]
        super(menustartonlinegame, self).__init__(**kwargs)

    def startGame(self):
        settings.currentScreen = 'game'

        uihelper.toggleModel('menustartonlinegame')
        uihelper.toggleModel('menuloading')

    def addInputs(self):
        self.addCommon(uid='coverall')
        #New game button
        self.addInput(type='mouseAction', priority=5, title='openBuyMenu', attribute={
            'click': 1,
            'pos': [200, 400],
            'dim': [50,250],
            'event': 'startGame',
        })

    def addOutputs(self):
        self.addOutput(pos=[80,400], type='text', priority= 2, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 60,
            'value': 'Online Game',
            'color': (255, 255, 255)
        })

        self.addOutput(pos=[150, 425], type='text', priority=2, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 30,
            'value': 'Game ID: '+str(settings.gameData['game_id']),
            'color': (255, 255, 255)
        })
        self.addOutput(pos=[170, 425], type='text', priority=2, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 30,
            'value': 'Access Pin: ' + str(settings.gameData['game_pin']),
            'color': (255, 255, 255)
        })

        #Start new game button
        self.addOutput(pos=[200, 400], type='shape', priority=2, title='menustoragebuytext', attribute={
            'shape': 'rectangle',
            'dim': [50,250],
            'color': (255, 0, 0)
        })
        self.addOutput(pos=[212, 445], type='text', priority=3, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 30,
            'value': 'Continue',
            'color': (255, 255, 255)
        })
        self.addOutput(pos=self.basePos, type='shape', priority=0, title='shopBackground', attribute={
            'shape': 'rectangle',
            'dim': self.baseDim,
            'color': (51, 51, 51)
        })
