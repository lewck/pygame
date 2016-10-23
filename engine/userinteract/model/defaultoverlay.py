'''
'
'   NB correct class naming convention: modeltype subtype action
'
'''

from engine.userinteract.model.base import base

import settings

class defaultoverlay(base):
    def __init__(self):
        self.basePriority = 50
        super(defaultoverlay, self).__init__()

    def addInputs(self):
        self.addInput(type='mouseAction', priority = self.basePriority + 9, title='close', attribute={
            'click': 1,
            'pos': [0,502],
            'dim': [100, 100],
            'event': 'close'
        })

    def addOutputs(self):
        self.addOutput(pos=[10, 10], type='text', priority= self.basePriority + 2, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 50,
            'value': 'Current {0} Value: ',
            'variables': ['settings.player.balance'],
            'color': (255, 255, 255)
        })