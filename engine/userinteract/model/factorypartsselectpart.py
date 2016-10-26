from engine.userinteract.model.base import base
from engine.userinteract.model.menuproducerbuy import menuproducerbuy
from engine.userinteract.helper import helper as uihelper

import settings

class factorypartsselectpart(base):
    def __init__(self, **kwargs):
        self.basePriority = 80
        self.title = 'factory'
        super(factorypartsselectpart, self).__init__(**kwargs)

    def selectPart(self, part):
        settings.grid[self.objectPosition[0]][self.objectPosition[1]].part = part
        print('part selected')
        uihelper.toggleModel('factorypartsselectpart')

    def addInputs(self):
        self.addInput(type='mouseAction', priority=self.basePriority + 5, title='openBuyMenu', attribute={
            'click': 1,
            'pos': [50, 110],
            'dim': [40, 70],
            'event': 'doSomething',
        })

    def addOutputs(self):
        self.addOutput(pos=[10, 10], type='text', priority=self.basePriority + 2, title='factoryparttitle',
            attribute={
               'font': 'primaryFont',
               'size': 50,
               'value': 'Factory Part Menu',
               'color': (255, 255, 255)
           }
        )

        self.addOutput(pos=[0,0], type='shape', priority=self.basePriority, title='factoryPartBackground',
            attribute={
                'shape': 'rectangle',
                'dim': [512, 512],
                'color': (0, 0, 0)
            }
        )

        max = len(settings.itemDB) - 1

        count = 0
        posx = 12
        posy = 100
        for y in range(0, 8):
            for x in range(0, 12):
                self.addOutput(pos=[posy + 2, posx + 2], type='shape', priority=self.basePriority + 5,
                               title='shopBackground' + str(y) + str(x), attribute={
                        'shape': 'rectangle',
                        'dim': [39, 39],
                        'color': (0, 0, 0)
                    })

                if (count <= max):
                    uid = list(settings.itemDB.keys())[count]
                    self.addOutput(pos=[posy + 2, posx + 2], type='image', priority=self.basePriority + 6, title='btn',
                                   attribute={
                                       'uid': uid,
                                       'scale': (39, 39)
                                   })
                    self.addInput(type='mouseclick', priority=6, title='btnin', attribute={
                        'click': 1,
                        'pos': [posy + 2, posx + 2],
                        'dim': [39, 39],
                        'event': 'selectPart',
                        'eventArgs': [uid],
                    })
                    print('uid' + str(uid))
                    count += 1
                posx += 41
            posx = 12
            posy += 41


    def load(self, pos):
        self.objectPosition = pos

        self.refresh()