'''
'
'   NB correct class naming convention: modeltype subtype action
'
'''

from engine.userinteract.model.base import base
from engine.userinteract.helper import helper as uihelper

import settings

class menuloading(base):
    def __init__(self, **kwargs):
        self.basePriority = 120
        self.basePos = [0,0]
        self.baseDim = [550,1050]
        super(menuloading, self).__init__(**kwargs)

    def addInputs(self):
        self.addCommon(uid='coverall')

    def addOutputs(self):
        self.addOutput(pos=[250,400], type='text', priority= 2, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 60,
            'value': 'LOADING...',
            'color': (0, 0, 0)
        })
