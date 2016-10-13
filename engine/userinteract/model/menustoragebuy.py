'''
'
'   NB correct class naming convention: modeltype subtype action
'
'''

from engine.userinteract.model.base import base
from shop import shop
from item.factory import factory as itemFactory
from object.factory import factory as objectFactory

import settings

class menustoragebuy(base):
    def __init__(self):
        self.basePriority = 100
        super(menustoragebuy, self).__init__()

    def buyObject(self, type, uid):
        obj = objectFactory.create(uid=uid, direction=2)
        if(obj):
            settings.inputBuffer = ['setObject', obj]
        self.close()
        settings.activeUI['menustoragebuy'] = False

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
            'value': 'Storage Shop',
            'color': (255, 255, 255)
        })

        self.addOutput(pos=[0, 0], type='shape', priority= self.basePriority +0, title='shopBackground', attribute={
            'shape': 'rectangle',
            'dim': [512,512],
            'color': (51,51,51)
        })

        self.addOutput(pos=[0, 502], type='shape', priority=6, title='shopBackground', attribute={
            'shape': 'rectangle',
            'dim': [10, 10],
            'color': (255, 0,0)
        })


        max = len(settings.objectDB['storage'])-1

        count = 0
        posx = 12
        posy = 100
        for y in range(0,8):
            for x in range(0,12):
                self.addOutput(pos=[posy + 2, posx + 2], type='shape', priority= self.basePriority + 5, title='shopBackground' + str(y) + str(x), attribute={
                    'shape': 'rectangle',
                    'dim': [39, 39],
                    'color': (0, 0, 0)
                })

                if(count<=max):
                    uid = list(settings.objectDB['storage'].keys())[count]
                    self.addOutput(pos=[posy + 2, posx + 2], type='image', priority= self.basePriority+6, title='btn',  attribute={
                        'uid': uid,
                        'scale': (39,39)
                    })
                    self.addInput(type='mouseclick', priority=6, title='btnin', attribute={
                        'click': 1,
                        'pos': [posy + 2, posx + 2],
                        'dim': [39,39],
                        'event': 'buyObject',
                        'eventArgs': ['storage','genericHouse'],
                    })
                    count += 1
                posx += 41
            posx = 12
            posy += 41
