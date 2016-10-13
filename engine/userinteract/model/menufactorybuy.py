'''
'
'   NB correct class naming convention: modeltype subtype action
'
'''

from engine.userinteract.model.base import base
from shop import shop
from item.factory import factory as itemFactory

import settings

class menufactorybuy(base):
    def __init__(self):
        super(menufactorybuy, self).__init__()

    def buyItem(self, type, uid):
        obj = itemFactory.create(item = uid, quantity = 1)
        if(shop.purchase(obj.price)):
            print(obj)
        else:
            print('You are too poor')

    def addInputs(self):

        self.addInput(type='mouseAction', priority = 10, title='close', attribute={
            'click': 1,
            'pos': [0,502],
            'dim': [100, 100],
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

        self.addOutput(pos=[0, 502], type='shape', priority=6, title='shopBackground', attribute={
            'shape': 'rectangle',
            'dim': [10, 10],
            'color': (255, 0,0)
        })


        max = len(settings.itemDB['vegetable'])-1
        count = 0

        posx = 12
        posy = 100
        for y in range(0,8):
            for x in range(0,12):
                self.addOutput(pos=[posy + 2, posx + 2], type='shape', priority=10, title='shopBackground' + str(y) + str(x), attribute={
                    'shape': 'rectangle',
                    'dim': [39, 39],
                    'color': (0, 0, 0)
                })

                if(count<=max):
                    uid = list(settings.itemDB['vegetable'].keys())[count]
                    self.addOutput(pos=[posy + 2, posx + 2], type='image', priority=20, title='btn',  attribute={
                        'uid': uid,
                        'scale': (39,39)
                    })
                    self.addInput(type='mouseclick', priority=20, title='btnin', attribute={
                        'click': 1,
                        'pos': [posy + 2, posx + 2],
                        'dim': [39,39],
                        'event': 'buyItem',
                        'eventArgs': ['item','vegetableCarrot'],
                    })
                    count += 1

                posx += 41
            posx = 12
            posy += 41
