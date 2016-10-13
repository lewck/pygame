import pygame
import settings



class base:
    def __init__(self):
        self.setVars()

    def setVars(self):
        #TODO make this work for non vegetables
        self.itemDetails = settings.itemDB['vegetable'][self.id]
        pass
