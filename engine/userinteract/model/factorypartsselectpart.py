from engine.userinteract.model.base import base
from engine.userinteract.model.menuproducerbuy import menuproducerbuy
from engine.userinteract.helper import helper as uihelper

import settings

class factorypartsselectpart(base):
    def __init__(self, **kwargs):
        self.basePriority = 80
        self.title = 'factorypartsselectpart'
        super(factorypartsselectpart, self).__init__(**kwargs)

    def selectPart(self, part):
        settings.grid[self.objectPosition[0]][self.objectPosition[1]].part = part
        uihelper.toggleModel('factorypartsselectpart')

    def addInputs(self):
        self.addInput(type='mouseAction', priority= 5, title='openBuyMenu', attribute={
            'click': 1,
            'pos': [50, 110],
            'dim': [40, 70],
            'event': 'doSomething',
        })

    def addOutputs(self):
        self.addOutput(pos=[10, 10], type='text', priority= 2, title='factoryparttitle',
            attribute={
               'font': 'primaryFont',
               'size': 50,
               'value': 'Factory Part Menu',
               'color': (255, 255, 255)
           }
        )

        self.addOutput(pos=[0,0], type='shape', priority=0, title='factoryPartBackground',
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
        shouldBreak = False
        keys = list(settings.itemDB.keys())

        for y in range(0, 8):
            for x in range(0, 12):

                if (count <= max):
                    self.addOutput(pos=[posy + 2, posx + 2], type='shape', priority=5,
                                   title='shopBackground' + str(y) + str(x), attribute={
                            'shape': 'rectangle',
                            'dim': [39, 39],
                            'color': (51, 51, 51)
                        })

                    uid = keys[count]
                    self.addOutput(pos=[posy + 2, posx + 2], type='image', priority=6, title='btn',
                                   attribute={
                                       'uid': uid,
                                       'scale': (39, 39)
                                   })

                    if(settings.itemDB[keys[count]]['discovered'] == True):
                        self.addInput(type='mouseclick', priority=6, title='btnin', attribute={
                            'click': 1,
                            'pos': [posy + 2, posx + 2],
                            'dim': [39, 39],
                            'event': 'selectPart',
                            'eventArgs': [uid],
                        })
                    else:
                        self.addOutput(pos=[posy + 2, posx + 12], type='shape', priority= 8,
                                       title='shopBackground' + str(y) + str(x), attribute={
                                'shape': 'rectangle',
                                'dim': [39, 5],
                                'color': (255, 0, 0)
                            })
                    count += 1
                else:
                    shouldBreak = True
                    break
                posx += 41

            if(shouldBreak == True):
                break
            posx = 12
            posy += 41


    def load(self, pos):
        self.objectPosition = pos
        self.refresh()