import pygame
import settings



class base:
    def __init__(self):
        self.setVars()

    def setVars(self):
        self.itemDetails = settings.itemIDName[self.itemID]

