import settings
from util.tool import tool

# Jobs are things awating to be completed by entities or alike

class base:
    def __init__(self, **kwargs):
        self.isClaimed = False
        self.initialVarsSet = False
        self.initVars(**kwargs)
        self.taskClaimed = False
        self.jobSetID = kwargs['parent']


        for each in self.tickListen:
            self.ticks = settings.tick.register(each, 'settings.activeJobDB["'+str(self.jobID)+'"].tick()', self.jobID)

    def initVars(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def eventTaskComplete(self):
        # Called by entity when job is compled
        self.taskCurrent += 1

    def close(self):
        # Unset Ticks
        settings.tick.remove(identifier=self.jobID)
        del settings.activeJobDB[self.jobID]

    def complete(self):
        settings.activeJobsetDB[self.jobSetID].eventTaskComplete()
        self.jobSpecificComplete()
        self.close()