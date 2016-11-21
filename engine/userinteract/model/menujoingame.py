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
        super(menujoingame, self).__init__(**kwargs)
        self.balance = 0

    def selectBalance(self, balance):
        self.balance = balance

    def createGame(self):
        #Try webinteract to create game
        gamewebinteract = game()
        gamewebinteract.create(1, self.balance)
        uihelper.toggleModel('gamesettings')
        uihelper.reloadModel(settings.activeUI['menustartonlinegame'])
        uihelper.toggleModel('menustartonlinegame')

    def joinGame(self):
        print('joining')

    def inputPin(self):
        inputbuffer.create('getKeyInput', 16)

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
            'pos': [50, 135],
            'dim': [40, 160],
            'event': 'inputPin',
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
            'value': 'Game ID:',
            'color': (255, 255, 255)
        })

        # Balance Title
        self.addOutput(pos=[65, 150], type='text', priority=3, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 30,
            'value': 'Click To Edit',
            'color': (255, 255, 255)
        })

        self.addOutput(pos=[50, 135], type='shape', priority=2, title='menustoragebuytext', attribute={
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
