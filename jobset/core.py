import settings
from util.tool import tool
from object.helper import helper as objecthelper
from pathfind import pathFind
from entity.helper import helper as entityhelper
from job import factory as job

#--------------------------------------------------
#  Factory Class
#--------------------------------------------------
class factory():
    @staticmethod
    def create(**args):
        jobsetID = tool.genRandomString(16)
        jobsetID = tool.genUniqueID(settings.activeJobsetDB, 16)

        settings.activeJobsetDB[jobsetID] = eval(args['typ']+'(**args, jobsetID = jobsetID)')

        return jobsetID

#--------------------------------------------------
#  Base Class
#--------------------------------------------------
class base:
    def __init__(self, **kwargs):
        self.initVars(**kwargs)
        #Register ticks
        for each in self.tickListen:
            settings.tick.register(each, 'settings.activeJobsetDB["'+str(self.jobsetID)+'"].tick()', self.jobsetID)

    def initVars(self, **kwargs):
        #Set independent vars
        for key, value in kwargs.items():
            setattr(self, key, value)
        #Set control vars
        self.taskCurrent = 1
        self.status = 1

    def eventTaskComplete(self):
        #Called by entity when job is completed
        self.status = 1
        self.taskCurrent += 1

    def tick(self):
        self.task()

    def close(self):
        settings.tick.remove(identifier = self.jobsetID)
        del settings.activeJobsetDB[self.jobsetID]

#===========================================================================
#  Subsidiary Classes
#==============================================================
#  Collect From Object And Store Jobset
#--------------------------------------------------
class collectFromObjectAndStore(base):
    def __init__(self, **kwargs):
        self.tickListen = [10]
        super(collectFromObjectAndStore, self).__init__(**kwargs)

    def doEvent(self, eventID):
        if (eventID == 'pathnotfound'):
            settings.activeJobDB[str(self.jobID)].close()
            self.close()
            self.taskCurrent = 3

    def task(self):
        if (self.taskCurrent == 1):
            # Determine best storage
            self.pathEnd = objecthelper.evaluateBestStorage([1, 1], 'item', self.itemID)

            if (self.pathEnd!=False):
                # Storage Not Found
                print('DOING')
                return False

            self.pathStart = objecthelper.getInteractPosition(self.startPosition[0], self.startPosition[1],
                                                              self.startPosition[2])

            # Determine best vehicle
            self.vehicleID = entityhelper.vehicleEvaluateBest(self.pathStart)

            if (self.vehicleID):
                path = pathFind(self.pathStart[0], self.pathStart[1], self.pathEnd[0], self.pathEnd[1],
                                5)

                self.pathID = path.find()

                if (self.pathID):
                    self.taskCurrent += 1

            if (self.taskCurrent == 1):
                self.close()

        if (self.taskCurrent == 2):
            # Begin
            # Collect, move, deposit
            if (self.status == 1):
                self.jobID = job.create(typ='moveItem', startPosition=self.pathStart, endPosition=self.pathEnd,
                                        items='all',
                                        parent=self.jobsetID, entityID=self.vehicleID, path=self.pathID)

                self.status = 0

        if (self.taskCurrent == 3):
            # Callback from entity, job completed
            # Send car back to storage
            # Find nearest garage
            self.close()
            pass

#--------------------------------------------------
#  Wait Fot Items Jobset
#--------------------------------------------------
class waitForItems(base):
    def __init__(self, **kwargs):
        self.tickListen = [10]
        super(waitForItems, self).__init__(**kwargs)
        self.pos = kwargs['position']
        self.items = kwargs['items']

    def task(self):
        pass

    def needsItem(self, itemID):
        for id, qty in self.items.items():
            if(id==itemID):
                return True
        return False