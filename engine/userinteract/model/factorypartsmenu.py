from engine.userinteract.model.base import base
from engine.userinteract.model.menuproducerbuy import menuproducerbuy
from engine.userinteract.helper import helper as uihelper

import settings

class factorypartsmenu(base):
    def __init__(self, **kwargs):
        self.basePriority = 70
        self.title = 'factory'
        super(factorypartsmenu, self).__init__(**kwargs)

    def createPartSelect(self):
        uihelper.updateAttribute('factorypartsselectpart','objectPosition', self.objectPosition)
        uihelper.toggleModel('factorypartsselectpart')

    def addInputs(self):
        self.addInput(type='mouseAction', priority=5, title='openBuyMenu', attribute={
            'click': 1,
            'pos': [50, 110],
            'dim': [40, 70],
            'event': 'createPartSelect',
        })
        self.addCommon(uid='close', pos=[0, 512])

    def addOutputs(self):
        self.addOutput(pos=[10, 10], type='text', priority=2, title='factoryparttitle',
            attribute={
               'font': 'primaryFont',
               'size': 50,
               'value': 'Factory Menu',
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

        if(hasattr(self, 'objectPosition')):
            #Assume claimed

            #Draw Part
            if(settings.grid[self.objectPosition[0]][self.objectPosition[1]].part != 0):
                text = settings.grid[self.objectPosition[0]][self.objectPosition[1]].part
            else:
                text = 'Select'



            self.addOutput(pos=[60, 10], type='text', priority= 5, title='factoryparttitle',
               attribute={
                   'font': 'primaryFont',
                   'size': 30,
                   'value': 'Part ID    : '+str(text),
                   'color': (255, 255, 255)
               }
            )


            '''
            #Visulisation of button area
            self.addOutput(pos=[50, 110], type='shape', priority=self.basePriority + 4, title='factoryparttitle',
                attribute = {
                    'shape': 'rectangle',
                    'dim': [40, 70],
                    'color': (255, 0, 0)
                }
               )
            '''



    def load(self, pos):
        self.objectPosition = pos

        self.refresh()