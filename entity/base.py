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

    def assign(self, jobID):
        print('Assignining to '+str(jobID))

        for each in settings.activeJobDB:
            if(each.jobID == jobID):
                self.job = each

        self.path = settings.pathDB[settings.activeJobDB[0].path]
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

    def tick(self):
        if(self.tickListen!=False):
            self.tickCount += 1
            for i in range(0, len(self.tickListen)):
                if (self.tickCount % self.tickListen[i] == 0):
                    self.doTick(i)
                    if(i==len(self.tickListen)):
                        self.tickCount = 0
            #print(self.tickCount)