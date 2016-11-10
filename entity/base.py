import pygame
import settings
from job.helper import helper as jobhelper

###
# 0 status = idle
# 1 status = busy
###
class base:
    def __init__(self):
        self.setVars()


    def setVars(self):
        self.tickCount = 0
        self.status = 0
        self.firstMove = True
        pos = []
        self.claimed = False

    def assign(self, jobID):
        print('Assignining to '+str(jobID))

        self.job = settings.activeJobDB[jobID]

        self.path = settings.pathDB[settings.activeJobDB[jobID].path]
        print('---')
        print(self.path)
        self.x = self.job.startPosition[1]*50
        self.y = self.job.startPosition[0]*50
        self.direction = 1
        self.jobID = jobID

        print(self.job)

        print('ASSIGN DEBUG')
        print(self.x)
        print(self.y)

    def unassign(self):
        self.job = 0
        self.path = 0
        self.x = 0
        self.y = 0
        self.direction = 0
        self.jobID = 0
        self.status = 0
        self.claimed = False


    def tick(self):
        if(self.tickListen!=False):
            self.tickCount += 1
            for i in range(0, len(self.tickListen)):
                if (self.tickCount % self.tickListen[i] == 0):
                    self.doTick(i)
                    if(i==len(self.tickListen)):
                        self.tickCount = 0
            #print(self.tickCount)


    def doMove(self):
        if (self.status == 1):

            xTile = (int(self.x /50))
            yTile = (int(self.y /50))


            for i in range(0, len(self.path[1])):
                for o in range(0, len(self.path[1][i])):
                    if (self.y / 50 == self.path[1][i][o][0] and self.x / 50 == self.path[1][i][o][1]):
                        if (self.direction == 4):
                            # Here
                            self.status = 3
                            jobhelper.complete(self.jobID)

                        currDirection = self.direction
                        self.direction = self.path[1][i][o][2]
                        print(self.direction)

            # update location tick
            if (self.direction == 0):
                self.y += -10
            elif (self.direction == 1):
                self.x += 10
            elif (self.direction == 2):
                self.y += 10
            elif (self.direction == 3):
                self.x += -10
                # print(matches)
        if (self.status == 3):
            # idle
            pass

    def place(self):
        settings.surface.blit(self.image, (self.x*50, self.y*50))

    def draw(self):
        directionRotation = {
            0: 0,
            1: 270,
            2: 180,
            3: 90
        }
        base = pygame.transform.scale(self.image, (50, 50))
        base1 = base

        if(self.direction!=4):
            base1 = pygame.transform.rotate(base, directionRotation[self.direction])

        settings.surface.blit(base1, (self.x, self.y))

    def loadItems(self):
        self.inventory.addItem()