'''
'
'   NB correct class naming convention: modeltype subtype action
'
'''

from engine.userinteract.model.base import base
from engine.userinteract.helper import helper as uihelper
from engine.inputbuffer import inputbuffer

from webinteract.game import game

import settings

class menujoingame(base):
    def __init__(self, **kwargs):
        self.basePriority = 110
        self.basePos = [0,0]
        self.baseDim = [550,1050]
        self.gameID = 0
        self.gamePin = 0
        super(menujoingame, self).__init__(**kwargs)


    def selectGameID(self, gameID):
        self.gameID = gameID
        uihelper.reloadModel(self.id)

    def selectGamePin(self, gamePin):
        self.gamePin = gamePin
        uihelper.reloadModel(self.id)

    def joinGame(self):
        gamewebinteract = game()
        if(gamewebinteract.join(self.gameID, self.gamePin)):
            uihelper.toggleModel('menujoingame')
            settings.currentScreen = 'game'

    def inputGameID(self):
        inputbuffer.create('getKeyInput', trigger = 'selectGameID', model = self.id, maxlength=4)

    def inputGamePin(self):
        inputbuffer.create('getKeyInput', trigger='selectGamePin', model=self.id, maxlength=4)


    def addInputs(self):
        self.addCommon(uid='coverall')
        #New game button
        self.addInput(type='mouseAction', priority=5, title='createGame', attribute={
            'click': 1,
            'pos': [500,850],
            'dim': [50,100],
            'event': 'joinGame',
        })

        self.addInput(type='mouseAction', priority=5, title='createGame', attribute={
            'click': 1,
            'pos': [50, 255],
            'dim': [40, 160],
            'event': 'inputGameID',
        })
        self.addInput(type='mouseAction', priority=5, title='createGame', attribute={
            'click': 1,
            'pos': [110, 255],
            'dim': [40, 160],
            'event': 'inputGamePin',
        })


    def addOutputs(self):
        self.addOutput(pos=[10,10], type='text', priority= 2, title='gamesettingstitle', attribute={
            'font': 'primaryFont',
            'size': 60,
            'value': 'Join settings',
            'color': (255, 255, 255)
        })

        self.addOutput(pos=[60, 10], type='text', priority=2, title='gamesettingstitle', attribute={
            'font': 'primaryFont',
            'size': 40,
            'value': 'Game ID:'+str(self.gameID),
            'color': (255, 255, 255),
        })

        # Balance Title
        self.addOutput(pos=[65, 270], type='text', priority=3, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 30,
            'value': 'Click To Edit',
            'color': (255, 255, 255)
        })

        self.addOutput(pos=[50, 255], type='shape', priority=2, title='menustoragebuytext', attribute={
            'shape': 'rectangle',
            'dim': [40, 160],
            'color': (255, 0, 0)
        })


        self.addOutput(pos=[120, 10], type='text', priority=2, title='gamesettingstitle', attribute={
            'font': 'primaryFont',
            'size': 40,
            'value': 'Game Pin:' + str(self.gamePin),
            'color': (255, 255, 255),
        })

        # Balance Title
        self.addOutput(pos=[125, 270], type='text', priority=3, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 30,
            'value': 'Click To Edit',
            'color': (255, 255, 255)
        })

        self.addOutput(pos=[110, 255], type='shape', priority=2, title='menustoragebuytext', attribute={
            'shape': 'rectangle',
            'dim': [40, 160],
            'color': (255, 0, 0)
        })




        self.addOutput(pos=[500,850], type='shape', priority=2, title='menustoragebuytext', attribute={
            'shape': 'rectangle',
            'dim': [50, 100],
            'color': (255, 0, 0)
        })
        self.addOutput(pos=[505,854], type='text', priority=3, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 40,
            'value': 'START',
            'color': (255, 255, 255)
        })

        self.addOutput(pos=self.basePos, type='shape', priority= 0, title='menuBackground', attribute={
            'shape': 'rectangle',
            'dim': self.baseDim,
            'color': (51,51,51)
        })
