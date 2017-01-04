from engine.userinteract.model.base import base
from engine.userinteract.helper import helper as uihelper

import settings

class defaultoverlay(base):
    def __init__(self, **kwargs):
        self.basePos = [0, 0]
        self.baseDim = [550, 1050]
        self.basePriority = 60

        base.__init__(self, **kwargs)

    #--------------------------------------------------
    #  Assign Inputs
    #--------------------------------------------------
    def addInputs(self):
        # Open factory buy menu
        self.addInput(type='mouseAction', priority=5, attribute={
            'click': 1,
            'pos': [settings.yMax*50, 150],
            'dim': [50, 150],
            'event': 'openMenu',
            'eventArgs': ['menufactorybuy'],
        })

        # Open vehicle buy menu
        self.addInput(type='mouseAction', priority=5, attribute={
            'click': 1,
            'pos': [settings.yMax * 50, 305],
            'dim': [50, 150],
            'event': 'openMenu',
            'eventArgs': ['menuvehiclebuy'],
        })

        # Open market overview model
        self.addInput(type='mouseAction', priority=5, attribute={
            'click': 1,
            'pos': [settings.yMax * 50, 460],
            'dim': [50, 150],
            'event': 'openMenu',
            'eventArgs': ['menumarketstatus'],
        })

        # Open unlock menu
        self.addInput(type='mouseAction', priority=5, attribute={
            'click': 1,
            'pos': [settings.yMax * 50, 615],
            'dim': [50, 150],
            'event': 'openMenu',
            'eventArgs': ['menuunlock'],
        })

    #--------------------------------------------------
    #  Assign Outputs
    #--------------------------------------------------
    def addOutputs(self):
        # Sidebar
        self.addOutput(pos=[0, settings.xMax * 50], type='shape', attribute={
           'shape': 'rectangle',
           'dim': [(settings.yMax*50)+50, 300],
           'color': (51, 51, 51)
        })
        self.addOutput(pos=[20, (settings.xMax * 50)+20], type='text', priority=2, attribute={
           'font': 'primaryFont',
           'size': 30,
           'value': 'Environment',
           'color': (255, 255, 255)
        })
        self.addOutput(pos=[50, (settings.xMax * 50) + 20], type='text', priority=2, attribute={
           'font': 'primaryFont',
           'size': 20,
           'value': 'Balance: {0}',
           'variables': ['int(settings.player.balance)'],
           'color': (255, 255, 255)
        })

        # Balance
        self.addOutput(pos=[(settings.yMax*50) +10, 10], type='text', priority=2, attribute={
            'font': 'primaryFont',
            'size': 20,
            'value': 'Balance: {0}',
            'variables': ['int(settings.player.balance)'],
            'color': (255, 255, 255)
        })

        # Producer Menu Button
        self.addOutput(pos=[settings.yMax * 50, 150], type='shape', priority=2, attribute={
            'shape': 'rectangle',
            'dim': [50, 150],
            'color': (255, 255, 0)
        })
        self.addOutput(pos=[(settings.yMax * 50) + 15, 175], type='text', priority=5, attribute={
           'font': 'primaryFont',
           'size': 20,
           'value': 'Factory Menu',
           'color': (0, 0, 0)
        })

        # Vehicle Menu Button
        self.addOutput(pos=[settings.yMax * 50, 305], type='shape', priority=2, attribute={
           'shape': 'rectangle',
           'dim': [50, 150],
           'color': (255, 255, 0)
        })
        self.addOutput(pos=[(settings.yMax * 50) + 15, 335], type='text', priority=5, attribute={
           'font': 'primaryFont',
           'size': 20,
           'value': 'Vehicle Menu',
           'color': (0, 0, 0)
        })

        # Market Menu Button
        self.addOutput(pos=[settings.yMax * 50, 460], type='shape', priority=2, attribute={
           'shape': 'rectangle',
           'dim': [50, 150],
           'color': (255, 255, 0)
        })
        self.addOutput(pos=[(settings.yMax * 50) + 15, 500], type='text', priority=5, attribute={
           'font': 'primaryFont',
           'size': 20,
           'value': 'Market',
           'color': (0, 0, 0)
        })

        # Unlock Menu Button
        self.addOutput(pos=[settings.yMax * 50, 615], type='shape', priority=2, attribute={
           'shape': 'rectangle',
           'dim': [50, 150],
           'color': (255, 255, 0)
        })
        self.addOutput(pos=[(settings.yMax * 50) + 15, 650], type='text', priority=5, attribute={
           'font': 'primaryFont',
           'size': 20,
           'value': 'Unlocks',
           'color': (0, 0, 0)
        })

    #--------------------------------------------------
    #  Model-Specific Functionality
    #--------------------------------------------------
    def openMenu(self, uid):
        # Open menu Ui
        uihelper.toggle(uid)