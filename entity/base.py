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

    def assign(self, jobID):
        print('Assignining to '+str(jobID))
        self.job = settings.activeJobDB[0]
        self.path = settings.pathDB[settings.activeJobDB[0].path]
        print('---')
        print(self.path)
        self.x = self.job.startPosition[1]*50
        self.y = self.job.startPosition[0]*50
        self.direction = 1
        self.jobID = jobID

        print(self.job)

        print('ASSIGNDEBUG')
        print(self.x)
        print(self.y)

    def tick(self):
        if(self.tickListen!=False):
            self.tickCount += 1
            for i in range(0, len(self.tickListen)):
                if (self.tickCount % self.tickListen[i] == 0):
                    self.doTick(i)
                    if(i==len(self.tickListen)):
                        self.tickCount = 0
            #print(self.tickCount)