from engine import event
from engine.userinteract.model.base import base
from random import randint

import settings

class welcome(base):
    def __init__(self):
        super(welcome, self).__init__()

    def addInputs(self):
        self.addInput(type='mouseAction', priority = 5, title='close', attribute={
            'click': 1,
            'pos': [0, 0],
            'dim': [200, 100],
            'event': 'close'
        })

    def addOutputs(self):
        self.addOutput(pos=[200, 200], type='text', priority=10, title='welcomeText', attribute={
            'size': 10,
            'value': 'Basic introduction!',
            'color': (255, 255, 0)
        })

        self.addOutput(pos=[0, 0], type='shape', priority=5, title='shopBackground', attribute={
            'shape': 'rectangle',
            'dim': [512,512],
            'color': (51,51,51)
        })


