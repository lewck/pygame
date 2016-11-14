from engine.userinteract.model.base import base
from engine.userinteract.model.menuproducerbuy import menuproducerbuy
from engine.userinteract.helper import helper as uihelper

import settings

class defaultoverlay(base):
    def __init__(self, **kwargs):
        self.basePriority = 60
        super(defaultoverlay, self).__init__(**kwargs)

    def openMenu(self, uid):
        uihelper.toggleModel(uid)

    def addInputs(self):
        self.addInput(type='mouseAction', priority=self.basePriority, title='base', attribute={
            'click': 1,
            'pos': [settings.yMax*50, 0],
            'dim': [50, settings.xMax*50],
            'event': 'none',
        })

        self.addInput(type='mouseAction', priority=self.basePriority+5, title='openProducerMenu', attribute={
            'click': 1,
            'pos': [settings.yMax*50, 150],
            'dim': [50, 150],
            'event': 'openMenu',
            'eventArgs': ['menuproducerbuy'],
        })

        self.addInput(type='mouseAction', priority=self.basePriority + 5, title='oepnvehiclemenu', attribute={
            'click': 1,
            'pos': [settings.yMax * 50, 305],
            'dim': [50, 150],
            'event': 'openMenu',
            'eventArgs': ['menuvehiclebuy'],
        })

        self.addInput(type='mouseAction', priority=self.basePriority + 5, title='openmarketmenu', attribute={
            'click': 1,
            'pos': [settings.yMax * 50, 460],
            'dim': [50, 150],
            'event': 'openMenu',
            'eventArgs': ['menumarketstatus'],
        })

        self.addInput(type='mouseAction', priority=self.basePriority + 5, title='openunlocksmenu', attribute={
            'click': 1,
            'pos': [settings.yMax * 50, 615],
            'dim': [50, 150],
            'event': 'openMenu',
            'eventArgs': ['menuunlock'],
        })


    def addOutputs(self):
        #Background
        self.addOutput(pos=[settings.yMax*50, 0], type='shape', priority=self.basePriority , title='overlayBackground',
            attribute={
                'shape': 'rectangle',
                'dim': [50, settings.xMax*50],
                'color': (51, 51, 51)
            }
        )
        #sidebar
        self.addOutput(pos=[0, settings.xMax * 50], type='shape', priority=self.basePriority, title='overlayBackground',
           attribute={
               'shape': 'rectangle',
               'dim': [(settings.yMax*50)+50, 300],
               'color': (51, 51, 51)
           }
        )
        self.addOutput(pos=[20, (settings.xMax * 50)+20], type='text', priority=self.basePriority + 2,title='menustoragebuytext',
           attribute={
               'font': 'primaryFont',
               'size': 30,
               'value': 'Environment',
               'color': (255, 255, 255)
           }
        )

        self.addOutput(pos=[50, (settings.xMax * 50) + 20], type='text', priority=self.basePriority + 2, title='menustoragebuytext',
           attribute={
               'font': 'primaryFont',
               'size': 20,
               'value': 'Balance: {0}',
               'variables': ['settings.player.balance'],
               'color': (255, 255, 255)
           }
        )


        #Balance
        self.addOutput(pos=[(settings.yMax*50) +10, 10], type='text', priority= self.basePriority + 2, title='menustoragebuytext',
            attribute={
                'font': 'primaryFont',
                'size': 20,
                'value': 'Balance: {0}',
                'variables': ['settings.player.balance'],
                'color': (255, 255, 255)
            }
        )

        #Producer Menu Button
        self.addOutput(pos=[settings.yMax * 50, 150], type='shape', priority=self.basePriority+2, title='overlayBackground',
           attribute={
               'shape': 'rectangle',
               'dim': [50, 150],
               'color': (255, 255, 0)
           }
        )
        self.addOutput(pos=[(settings.yMax * 50) + 15, 175], type='text', priority=self.basePriority + 5, title='menustoragebuytext',
           attribute={
               'font': 'primaryFont',
               'size': 20,
               'value': 'Producer Menu',
               'color': (0, 0, 0)
           }
        )

        # Vehicle Menu Button
        self.addOutput(pos=[settings.yMax * 50, 305], type='shape', priority=self.basePriority + 2, title='overlayBackground',
           attribute={
               'shape': 'rectangle',
               'dim': [50, 150],
               'color': (255, 255, 0)
           }
        )
        self.addOutput(pos=[(settings.yMax * 50) + 15, 335], type='text', priority=self.basePriority + 5, title='menustoragebuytext',
           attribute={
               'font': 'primaryFont',
               'size': 20,
               'value': 'Vehicle Menu',
               'color': (0, 0, 0)
           }
        )

        self.addOutput(pos=[settings.yMax * 50, 460], type='shape', priority=self.basePriority + 2, title='overlayBackground',
           attribute={
               'shape': 'rectangle',
               'dim': [50, 150],
               'color': (255, 255, 0)
           }
        )
        self.addOutput(pos=[(settings.yMax * 50) + 15, 500], type='text', priority=self.basePriority + 5, title='menustoragebuytext',
           attribute={
               'font': 'primaryFont',
               'size': 20,
               'value': 'Market',
               'color': (0, 0, 0)
           }
        )

        self.addOutput(pos=[settings.yMax * 50, 615], type='shape', priority=self.basePriority + 2,
                       title='overlayBackground',
                       attribute={
                           'shape': 'rectangle',
                           'dim': [50, 150],
                           'color': (255, 255, 0)
                       }
                       )
        self.addOutput(pos=[(settings.yMax * 50) + 15, 650], type='text', priority=self.basePriority + 5,
                       title='menustoragebuytext',
                       attribute={
                           'font': 'primaryFont',
                           'size': 20,
                           'value': 'Unlocks',
                           'color': (0, 0, 0)
                       }
                       )