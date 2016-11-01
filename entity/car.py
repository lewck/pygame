import pygame
import settings
from inventory import inventory
from job.factory import factory as job
from job.helper import helper as jobhelper

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

