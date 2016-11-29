import pygame
from pygame.locals import Rect
import settings

from engine.tick import tick

class base:
    def setVars(self, **kwargs):
        # base, image, direction, tickListen
        # Load Vars
        provided = settings.objectDB[self.type][self.title]

        defaults = {
            'devOverlay': 0,
            'tickListen': [],
        }

        for key, value in provided.items():
            setattr(self, key, value)

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key, value in defaults.items():
            if not(hasattr(self, key)):
                #Set default
                setattr(self, key, value)

        self.image = self.load(self.image)

        if(hasattr(self, 'base')):
            self.base = self.load(self.base)


        # static
        self.highlighted = False
        self.tickCount = 0
        self.inventory = 0

        # Set tick vars
        if(hasattr(self, 'tickListen') & hasattr(self, 'y')):
            #Needs registered ticks, hasPosition
            self.registerTicks()

    def registerTicks(self):
        for each in self.tickListen:
            settings.tick.register(each, 'settings.grid[' + str(self.y) + '][' + str(self.x) + '].tick()')



    def load(self, spriteID):
        stmt = 'sprites/'+str(spriteID)+'.png'
        return pygame.image.load(stmt)

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
        pygame.draw.rect(settings.surface, (255,0,0), [self.x*50,self.y*50,50,50])
        settings.surface.blit(settings.fonts['primaryFont'][30].render(directions[self.highlightedDirection], True, (255,255,255)), [self.x*50,self.y*50,50,50])

    def isPassible(self, entityid):
        if(entityid in self.passable):
            return True
        return False

    def tick(self):
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

