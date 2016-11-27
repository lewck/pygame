from engine.userinteract.model.base import base
from engine.userinteract.helper import helper as uihelper
import settings

class menustart(base):
    def __init__(self, **kwargs):
        self.basePriority = 110
        self.basePos = [0,0]
        self.baseDim = [550,1050]
        super(menustart, self).__init__(**kwargs)

    def createGame(self):
        # Toggle to create game menu
        uihelper.toggleModel('menustart')
        uihelper.toggleModel('gamesettings')

    def joinGame(self):
        uihelper.toggleModel('menustart')
        uihelper.toggleModel('menujoingame')

    def addInputs(self):
        self.addCommon(uid='coverall')
        # New game button
        self.addInput(type='mouseAction', priority=5, title='createGame', attribute={
            'click': 1,
            'pos': [200, 400],
            'dim': [50,250],
            'event': 'createGame',
        })
        # Join game button
        self.addInput(type='mouseAction', priority=5, title='joinGame', attribute={
            'click': 1,
            'pos': [300, 400],
            'dim': [50, 250],
            'event': 'joinGame',
        })

    def addOutputs(self):
        self.addOutput(pos=[80,425], type='text', priority= 2, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 60,
            'value': 'Welcome',
            'color': (255, 255, 255)
        })

        # Start new game button
        self.addOutput(pos=[200, 400], type='shape', priority=2, title='menustoragebuytext', attribute={
            'shape': 'rectangle',
            'dim': [50,250],
            'color': (255, 0, 0)
        })
        self.addOutput(pos=[212, 445], type='text', priority=3, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 30,
            'value': 'Start New Game',
            'color': (255, 255, 255)
        })

        # Join game button
        self.addOutput(pos=[300, 400], type='shape', priority=2, title='menustoragebuytext', attribute={
            'shape': 'rectangle',
            'dim': [50, 250],
            'color': (255, 0, 0)
        })
        self.addOutput(pos=[312, 445], type='text', priority=3, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 30,
            'value': 'Join A Game',
            'color': (255, 255, 255)
        })

        self.addOutput(pos=self.basePos, type='shape', priority= 0, title='background', attribute={
            'shape': 'rectangle',
            'dim': self.baseDim,
            'color': (51,51,51)
        })
