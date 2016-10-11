'''
'
'   NB correct class naming convention: modeltype subtype action
'
'''

from engine.userinteract.model.base import base

import settings

class menufactorybuy(base):
    def __init__(self):
        super(menufactorybuy, self).__init__()

    def addInputs(self):
        self.addInput(type='mouseAction', priority = 5, title='close', attribute={
            'click': 1,
            'pos': [0, 0],
            'dim': [200, 100],
            'event': 'close'
        })

    def addOutputs(self):
        self.addOutput(pos=[10, 10], type='text', priority=20, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 50,
            'value': 'Storage Shop',
            'color': (255, 255, 255)
        })



        self.addOutput(pos=[0, 0], type='shape', priority=5, title='shopBackground', attribute={
            'shape': 'rectangle',
            'dim': [512,512],
            'color': (51,51,51)
        })

        posx = 12
        posy = 100
        for y in range(0,8):
            for x in range(0,12):
                self.addOutput(pos=[posy+2, posx+2], type='shape', priority=10, title='shopBackground'+str(y)+str(x), attribute={
                    'shape': 'rectangle',
                    'dim': [39, 39],
                    'color': (0, 0, 0)
                })
                posx += 41
            posx = 12
            posy += 41
