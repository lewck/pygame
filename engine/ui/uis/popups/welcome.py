from engine.ui.uis.ioobject import ioobject
from engine.ui.uis.base import base
from random import randint

class welcome(base):
    def __init__(self):
        super(welcome, self).__init__()

    def active(self):
        self.activeOutput.append(ioobject(pos=[0, 0], type='shape', priority=1))
        self.activeOutput[0].addAttrs({
            'dim': [50, 150],
            'color': (randint(0, 255), randint(0, 255), randint(0, 255))
        })

        self.activeOutput.append(ioobject(pos=[0, 100], type='shape', priority=0))
        self.activeOutput[len(self.activeOutput) - 1].addAttrs({
            'dim': [50, 150],
            'color': (randint(0, 255), randint(0, 255), randint(0, 255))
        })

        self.activeOutput.append(ioobject(pos=[0, 0], type='image', priority=5))
        self.activeOutput[len(self.activeOutput) - 1].addAttrs({
            'uid': 'welcome',
            'scale': 1
        })

        self.activeOutput.append(ioobject(pos=[200, 200], type='text', priority=50))
        self.activeOutput[len(self.activeOutput) - 1].addAttrs({
            'size': 10,
            'value': 'Basic introduction!',
            'color': (255, 255, 0),

        })

        self.activeInput.append(ioobject(type='mouseAction', priority = 5))

        self.activeInput[len(self.activeInput) - 1].addAttrs({
            'click': 1,
            'pos':[0,0],
            'dim':[200,100],
            'event': 'close',
        })


        return [self.activeOutput, self.activeInput]