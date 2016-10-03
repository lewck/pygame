import pygame
from pygame.locals import Rect
import settings


class base:
    def __init__(self):
        print('base')

    def setVars(self, ypos, xpos, base, image, direction, tickListen):
        self.devOverlay = 0
        self.ypos = ypos
        self.xpos = xpos

        if(base!= 0):
            self.base = self.load(base)
        else:
            self.base = 0

        if(image!=0):
            self.image = self.load(image)
        else:
            self.image = 0

        self.direction = direction
        self.highlighted = False
        self.tickListen = tickListen
        self.tickCount = 0
        self.inventory = 0

    def load(self, spriteID):
        stmt = 'sprites/'+spriteID+'.png'
        return pygame.image.load(stmt)

    def log(self):
        print('Clicked' + str(self.ypos) + str(self.xpos))

    def setPathDev(self,g,h,f):
        self.devOverlay = [g,h,f]


    def highlightAdd(self, direction):
        self.highlighted = True
        self.highlightedDirection = direction


    def highlight(self):
        directions = {
            0:'UP',
            1:'RI',
            2:'DO',
            3:'LF',
            4:'4'
        }
        pygame.draw.rect(settings.surface, (255,0,0), [self.xpos*5*settings.zoom,self.ypos*5*settings.zoom,5*settings.zoom,5*settings.zoom])

        settings.surface.blit(settings.devfont.render(directions[self.highlightedDirection], True, (255,255,255)), [self.xpos*5*settings.zoom,self.ypos*5*settings.zoom,5*settings.zoom,5*settings.zoom])

    def isPassible(self, entityid):
        if(entityid in self.passable):
            return True
        return False

    def tick(self):
        if(self.tickListen!=False):
            self.tickCount += 1
            for i in range(0, len(self.tickListen)):
                if (self.tickCount % self.tickListen[i] == 0):
                    self.doTick(i)
                    if(i==len(self.tickListen)):
                        self.tickCount = 0
            #print(self.tickCount)
            #TODO ticks not being reset

    def hasInventory(self):
        if(self.inventory!=0):
            return True