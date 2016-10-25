from engine.userinteract.model.base import base
from engine.userinteract.model.menuproducerbuy import menuproducerbuy
from engine.userinteract.helper import helper as uihelper

import settings

class factoryPartsMenu(base):
    def __init__(self):
        self.basePriority = 70
        super(factoryPartsMenu, self).__init__()


    def addInputs(self):
        self.addInput(type='mouseAction', priority=self.basePriority, title='base', attribute={
            'click': 1,
            'pos': [750, 0],
            'dim': [50, 750],
            'event': 'none',
        })

        self.addInput(type='mouseAction', priority=self.basePriority+5, title='openBuyMenu', attribute={
            'click': 1,
            'pos': [750, 0],
            'dim': [50, 750],
            'event': 'openBuyMenu',
        })

    def addOutputs(self):
        self.addOutput(pos=[750, 0], type='shape', priority=self.basePriority ,
                       title='overlayBackground', attribute={
                'shape': 'rectangle',
                'dim': [50, 750],
                'color': (51, 51, 51)
            })

        self.addOutput(pos=[760, 10], type='text', priority= self.basePriority + 2, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 20,
            'value': 'Balance:ssssssssss {0}',
            'variables': ['settings.player.balance'],
            'color': (255, 255, 255)
        })