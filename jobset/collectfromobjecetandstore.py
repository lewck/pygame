import settings
from job.factory import factory as job
from jobset.base import base
from object.helper import helper as objecthelper
from entity.helper import helper as entityhelper
from pathfind import pathFind
from entity.factory import factory as entity

'''
'   Required Params:
'   startPosition [y,x,dir]:
'       Position of first OBJECT, we invert this to find pathStart
'''
class collectFromObjectAndStore(base):
    def __init__(self, **kwargs):
        self.tickListen = [5,10]
        super(collectFromObjectAndStore, self).__init__(**kwargs)


    def task(self):
        if(self.taskCurrent==1):
            if (self.status == 1):
                entity.create(uid='car')
                #Get car from garage
                self.vehicleID = entityhelper.vehicleEvaluateBest([1, 1])

                pathStart = objecthelper.getInteractPosition(self.startPosition[0], self.startPosition[1],
                                                                  self.startPosition[2])

                job.create(typ='movevehicle', parent=self.jobsetID, entityID=self.vehicleID, endPosition = [pathStart[0], pathStart[1]])

                self.status = 0


        if(self.taskCurrent==2):
            # decide best storage
            tmp = objecthelper.evaluateBestStorage([1, 1], 'item')
            if (tmp):
                self.pathEnd = tmp
            else:
                # Could not find storage
                pass

            self.pathStart = objecthelper.getInteractPosition(self.startPosition[0], self.startPosition[1],
                                                              self.startPosition[2])

            self.taskCurrent += 1


        if(self.taskCurrent==3):
            # Begin
            # Collect, move, deposit
            if (self.status == 1):
                job.create(typ='moveItem', startPosition=self.pathStart, endPosition=self.pathEnd, items='all',
                           parent=self.jobsetID, entityID = self.vehicleID)
                self.status = 0

        if(self.taskCurrent==4):
            # Callback from entity, job completed
            # Send car back to storage
            # Find nearest garage

            pass