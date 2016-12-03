import pygame
from inventory import inventory

from entity.base import base

class car(base):
    def __init__(self, **args):
        self.type = 'vehicle'
        super(car, self).setVars()
        self.image = pygame.image.load('sprites/car.png')
        self.tickListen = [5]
        self.inventory = inventory(5)

    def doTick(self, tickID):
        if(tickID==0):
            self.doMove()

