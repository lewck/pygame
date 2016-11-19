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
        self.tickListen = [10]
        super(collectFromObjectAndStore, self).__init__(**kwargs)

    def doEvent(self, eventID):
        if(eventID == 'pathnotfound'):
            settings.activeJobDB[str(self.jobID)].close()
            self.close()
            self.taskCurrent = 3

    def task(self):
        if(self.taskCurrent==1):
            #Decide best vehicle

            #print('entityDB:')
            #print(settings.activeEntityDB)
            
            # decide best storage
            tmp = objecthelper.evaluateBestStorage([1, 1], 'item', self.itemID)

            if (tmp):
                self.pathEnd = tmp
            else:
                # Could not find storage
                pass

            self.pathStart = objecthelper.getInteractPosition(self.startPosition[0], self.startPosition[1],
                                                              self.startPosition[2])


            self.vehicleID = entityhelper.vehicleEvaluateBest(self.pathStart)

            if(self.vehicleID):

                path = pathFind(self.pathStart[0], self.pathStart[1], self.pathEnd[0], self.pathEnd[1],
                                5)

                self.pathID = path.find()

                if(self.pathID):
                    self.taskCurrent += 1


            if(self.taskCurrent == 1):
                self.close()


        if(self.taskCurrent==2):
            # Begin
            # Collect, move, deposit
            if (self.status == 1):

                self.jobID = job.create(typ='moveItem', startPosition=self.pathStart, endPosition=self.pathEnd, items='all',
                           parent=self.jobsetID, entityID = self.vehicleID, path = self.pathID)

                self.status = 0

        if(self.taskCurrent==3):
            # Callback from entity, job completed
            # Send car back to storage
            # Find nearest garage
            self.close()
            pass