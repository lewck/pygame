from job.base import base
from pathfind import pathFind
from entity.helper import helper as entityhelper
from jobset.helper import helper as jobsethelper


import settings



class movevehicle(base):
    def __init__(self, **kwargs):
        self.tickListen = [1, 10]
        super(movevehicle, self).__init__(**kwargs)
        # Begin task 1
        self.taskCurrent = 1

    def assign(self, entityID):
        settings.activeEntityDB[entityID].assign(self.jobID)

    def task(self):
        options = {
            0: -1,
            1: 1,
            2: 1,
            3: -1
        }

        if(self.taskCurrent == 1):
            # Create path
            self.startPosition = settings.activeEntityDB[self.entityID].pos

            path = pathFind(self.startPosition[0], self.startPosition[1], self.endPosition[0], self.endPosition[1], 5)
            self.path = path.find()


            if(self.path):
                # Assign entity to path
                self.assign(self.entityID)
                self.taskCurrent += 1
            else:
                # Waiting for a path
                pass


        if(self.taskCurrent == 2):
            # Move Vehical
            settings.activeEntityDB[self.entityID].status = 1

        if(self.taskCurrent==3):
            jobsethelper.complete(self.jobSetID)
            self.taskCurrent=6

    def tick(self):
        if (self.taskClaimed == False):
            # Not claimed
            self.task()