from engine.userinteract.model.base import base

import settings

class defaultoverlay(base):
    def __init__(self):
        self.basePriority = 60
        super(defaultoverlay, self).__init__()

    def addInputs(self):
        self.addInput(type='mouseAction', priority=self.basePriority, title='base', attribute={
            'click': 1,
            'pos': [500, 0],
            'dim': [50, 500],
            'event': 'none',
        })

    def addOutputs(self):
        self.addOutput(pos=[500, 0], type='shape', priority=self.basePriority ,
                       title='overlayBackground', attribute={
                'shape': 'rectangle',
                'dim': [50, 500],
                'color': (51, 51, 51)
            })

        self.addOutput(pos=[510, 10], type='text', priority= self.basePriority + 2, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 20,
            'value': 'Balance: {0}',
            'variables': ['settings.player.balance'],
            'color': (255, 255, 255)
        })