from util.tool import tool
from engine.tick import tick
import settings

class base:
    def __init__(self, **kwargs):
        self.initVars(**kwargs)
        #Register ticks
        for each in self.tickListen:
            settings.tick.register([[each, 'settings.activeJobsetDB["'+str(self.jobsetID)+'"].tick()']])


    def initVars(self, **kwargs):
        #Set independent vars
        for key, value in kwargs.items():
            setattr(self, key, value)
        #Set control vars
        self.taskCurrent = 1
        self.status = 1

    def eventTaskComplete(self):
        #Called by entity when job is completed
        print('Job SET completed')
        self.status = 1
        self.taskCurrent += 1

    def tick(self):
        self.task()