import pygame
import settings
from random import randint

from engine.ui.uis.base import base
from engine.ui.uis.ioobject import ioobject
from engine.ui.uis.popups.welcome import welcome

'''
'   Generates output to the user, no input required other than close message function
'
'''
class popup(base):
    def __init__(self, **kwargs):
        #init
        super(popup, self).__init__(**kwargs)
        self.active()

    def active(self):
        self.subObject = eval(self.subType+'()')
        self.inout = self.subObject.active()
        self.activeOutput = self.inout[0]
        self.activeInput = self.inout[1]