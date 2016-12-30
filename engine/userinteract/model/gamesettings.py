from engine.userinteract.model.base import base
from engine.userinteract.helper import helper as uihelper
from webinteract.game import game

import settings

class gamesettings(base):
    def __init__(self, **kwargs):
        self.basePriority = 110
        self.basePos = [0,0]
        self.baseDim = [550,1050]
        self.balance = 0

        base.__init__(self, **kwargs)

    #--------------------------------------------------
    #  Assign Inputs
    #--------------------------------------------------
    def addInputs(self):
        self.addCommon(uid='coverall', color=(51,51,51))
        # New game button
        self.addInput(type='mouseAction', priority=5, attribute={
            'click': 1,
            'pos': [500,850],
            'dim': [50,100],
            'event': 'createGame',
        })

    #--------------------------------------------------
    #  Assign Outputs
    #--------------------------------------------------
    def addOutputs(self):
        # UI
        self.addOutput(pos=[10,10], type='text', priority= 2, attribute={
            'font': 'primaryFont',
            'size': 60,
            'value': 'Game settings',
            'color': (255, 255, 255)
        })
        self.addOutput(pos=[60, 10], type='text', priority=2, attribute={
            'font': 'primaryFont',
            'size': 40,
            'value': 'Objectives',
            'color': (255, 255, 255)
        })

        # Balance
        self.addOutput(pos=[95, 15], type='text', priority=3, attribute={
            'font': 'primaryFont',
            'size': 30,
            'value': 'Balance',
            'color': (255, 255, 255)
        })
        # Draw balance buttons
        balances = [
            10000, 50000, 100000, 1000000
        ]
        y = 90
        x = 120
        for each in balances:
            # Background
            self.addOutput(pos=[y, x], type='shape', priority=2, attribute={
                'shape': 'rectangle',
                'dim': [30, 100],
                'color': (255, 0, 0)
            })
            # Quantity
            self.addOutput(pos=[y+5, x+5], type='text', priority=3, attribute={
                'font': 'primaryFont',
                'size': 30,
                'value': str(each),
                'color': (255, 255, 255)
            })
            # Set Balance input
            self.addInput(type='mouseAction', priority=5, attribute={
                'click': 1,
                'pos': [y, x],
                'dim': [30, 100],
                'event': 'selectBalance',
                'eventArgs': [each],
            })
            x += 110

        # Start Button
        self.addOutput(pos=[500,850], type='shape', priority=2, attribute={
            'shape': 'rectangle',
            'dim': [50, 100],
            'color': (255, 0, 0)
        })
        self.addOutput(pos=[505,854], type='text', priority=3, attribute={
            'font': 'primaryFont',
            'size': 40,
            'value': 'START',
            'color': (255, 255, 255)
        })

    #--------------------------------------------------
    #  Model-Specific Functionality
    #--------------------------------------------------
    def selectBalance(self, balance):
        self.balance = balance

    def createGame(self):
        # Try webinteract to create game
        gamewebinteract = game()
        gameStatus = gamewebinteract.create(1, self.balance)

        if(gameStatus):
            # Game creation success
            uihelper.toggleModel('gamesettings')
            uihelper.reloadModel(settings.activeUI['menustartonlinegame'])

        # Game creation error
        print('Game Could Not Be Created')