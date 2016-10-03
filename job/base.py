import settings
from util.tool import tool

# Jobs are things awating to be completed by entities or alike

class base:
    def __init__(self, **kwargs):
        self.jobID = tool.genRandomString(20)
        print('Job created, id=' + str(self.jobID))
        self.isClaimed = False
        self.initialVarsSet = False
        self.initVars(**kwargs)
        self.taskClaimed = False
        self.jobSetID = kwargs['parent']
        for each in self.tickListen:
            settings.tick.register([[each, 'settings.activeJobDB['+str(self.jobIndex)+'].tick()']])
            print('registered tick')

    def initVars(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def eventTaskComplete(self):
        #Called by entity when job is completed
        print('Job completed')
        self.taskCurrent += 1