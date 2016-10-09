from random import randint

from engine.ui.uis.ioobject import ioobject

from legacy.ui.uis.base import base


class welcome(base):
    def __init__(self):
        super(welcome, self).__init__()

    def getSubClassName(self):
        return self.__class__.__name__

    def doEvent(self, event):
        print('eventijg'+event)

    def eventClose(self):
        print('Closing!')

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

        self.addOutput(pos=[200, 200], type='text', priority=50)
        self.addOutputAttrs({
            'size': 10,
            'value': 'Basic introduction!',
            'color': (255, 255, 0)
        })

        self.addInput(type='mouseAction', priority = 5)
        self.addInputAttrs({
            'click': 1,
            'pos':[0,0],
            'dim':[200,100],
            'eventID': self.addEvent('close'),
        })



        return [self.activeOutput, self.activeInput]