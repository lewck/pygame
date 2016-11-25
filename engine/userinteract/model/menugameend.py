'''
'
'   NB correct class naming convention: modeltype subtype action
'
'''

from engine.userinteract.model.base import base
from engine.userinteract.helper import helper as uihelper

from webinteract.game import game

import settings

class menugameend(base):
    def __init__(self, **kwargs):
        self.basePriority = 999
        self.basePos = [0,0]
        self.baseDim = [550,1050]
        super(menugameend, self).__init__(**kwargs)

    def addInputs(self):
        pass

    def addOutputs(self):

        self.addOutput(pos=[80,425], type='text', priority= 2, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 60,
            'value': 'Game Over!',
            'color': (255, 255, 255)
        })
        if(hasattr(self, 'winstatus')):
            if(self.winstatus == True):
                self.addOutput(pos=[140, 450], type='text', priority=2, title='menustoragebuytext', attribute={
                    'font': 'primaryFont',
                    'size': 60,
                    'value': 'You Win!',
                    'color': (0, 255, 0)
                })
            else:
                self.addOutput(pos=[140, 450], type='text', priority=2, title='menustoragebuytext', attribute={
                    'font': 'primaryFont',
                    'size': 60,
                    'value': 'You Lose!',
                    'color': (255, 0, 0)
                })


        self.addOutput(pos=self.basePos, type='shape', priority= 0, title='shopBackground', attribute={
            'shape': 'rectangle',
            'dim': self.baseDim,
            'color': (51,51,51)
        })
