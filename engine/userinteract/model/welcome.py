from engine import event
from engine.userinteract.model.base import base
from random import randint

import settings

class welcome(base):
    def __init__(self):
        super(welcome, self).__init__()

    def close(self):
        #Clear interfaces
        self.deleteInterface('output', 'all')
        print(self.id)


    def addInputs(self):
        self.addInput(type='mouseAction', priority = 5, title='close', attribute={
            'click': 1,
            'pos': [0, 0],
            'dim': [200, 100],
            'event': 'close'
        })

    def addOutputs(self):
        self.addOutput(pos=[200, 200], type='text', priority=50, title='welcomeText', attribute={
            'size': 10,
            'value': 'Basic introduction!',
            'color': (255, 255, 0)
        })

        self.addOutput(pos=[0, 0], type='image', priority=50, title='shopBackground', attribute={
            'uid': 'shopBackground',
        })

        self.addOutput(pos=[0, 0], type='shape', priority=50, title='shopBackground', attribute={
            'shape': 'rectangle',
            'dim': [50, 150],
            'color': (randint(0, 255), randint(0, 255), randint(0, 255))
        })


