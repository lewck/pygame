import pygame
import settings


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