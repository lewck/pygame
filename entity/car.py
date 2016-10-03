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
        self.inventory = inventory(10)

    def followPath(self):
        pass

    def place(self):
        settings.surface.blit(self.image, (self.x*5*settings.zoom, self.y*5*settings.zoom))

    def draw(self):
        directionRotation = {
            0: 0,
            1: 270,
            2: 180,
            3: 90
        }
        #print(str((5 * settings.zoom)/2))
        base = pygame.transform.scale(self.image, (int(((5 * settings.zoom))), int(((5 * settings.zoom)))))
        base1 = base

        if(self.direction!=4):
            base1 = pygame.transform.rotate(base, directionRotation[self.direction])

        settings.surface.blit(base1, (self.x, self.y))


    def loadItems(self):
        self.inventory.addItem()

    def doTick(self, tickID):
        if(tickID==0):
            if(self.status==1):
                xTile = (int(self.x / (5 * settings.zoom)))
                yTile = (int(self.y / (5 * settings.zoom)))
                
                #print(xTile)
                #print(yTile)
                #print('----------')
                #print(self.path[1])
                
                for i in range(0,len(self.path[1])):
                    for o in range(0, len(self.path[1][i])):
                        if(self.y/(5 * settings.zoom)==self.path[1][i][o][0] and self.x/(5 * settings.zoom)==self.path[1][i][o][1]):
                            if(self.direction==4):
                                #Here
                                self.status = 3
                                jobhelper.complete(self.jobID)

                            currDirection = self.direction
                            self.direction = self.path[1][i][o][2]
                            print(self.direction)
                        #print(self.path[1][i][o])

                #print('---------')
                # update location tick
                if (self.direction == 0):
                    self.y += -10
                elif (self.direction == 1):
                    self.x += 10
                elif (self.direction == 2):
                    self.y += 10
                elif (self.direction == 3):
                    self.x += -10
                #print(matches)
            if (self.status == 3):
                #idle
                pass


