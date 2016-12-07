from util.tool import tool
import settings



class factory():

    @staticmethod
    def create(**args):
        jobID = tool.genRandomString()

        settings.activeJobDB[jobID] = eval(args['typ'] + '(**args, jobID = jobID)')

        return jobID

class base:
    def __init__(self, **kwargs):
        self.isClaimed = False
        self.initialVarsSet = False
        self.initVars(**kwargs)
        self.taskClaimed = False
        self.jobSetID = kwargs['parent']

        for each in self.tickListen:
            self.ticks = settings.tick.register(each, 'settings.activeJobDB["' + str(self.jobID) + '"].tick()',
                                                self.jobID)

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

class moveItem(base):

    '''
        typ='moveItem', startPosition=[1, 1, 0], endPosition=[3, 3, 2], items='all')
    '''

    def __init__(self, **kwargs):
        self.tickListen = [1, 10]
        super(moveItem, self).__init__(**kwargs)
        # Begin task 1
        self.taskCurrent = 1
        self.assigned = False


    def unassign(self):
        settings.activeEntityDB[self.entityID].unassign()

    def task(self):
        options = {
            0: -1,
            1: 1,
            2: 1,
            3: -1
        }

        if(self.taskCurrent == 1):
            # Assign entity to pat
            self.taskCurrent += 1
            # Assign Entity
            settings.activeEntityDB[self.entityID].assign(self.jobID)


        if(self.taskCurrent == 2):
            # Move items from invA to invB

            if(self.startPosition[2]==0 or self.startPosition[2]==2):
                # Handle y change

                if(settings.grid[self.startPosition[0]+options[self.startPosition[2]]][self.startPosition[1]]).hasInventory():
                    # TODO wait for full inventory
                    self.itemBuffer = settings.grid[self.startPosition[0] + options[self.startPosition[2]]][self.startPosition[1]].inventoryOutput.takeItem(
                        'all',
                        settings.activeEntityDB[self.entityID].inventory.size
                    )

                    settings.activeEntityDB[self.entityID].inventory.loadItem(self.itemBuffer)
                    self.taskCurrent += 1


            if(self.startPosition[2]==1 or self.startPosition[2]==3):

                if (settings.grid[self.startPosition[0]][self.startPosition[1]+options[self.startPosition[2]]]).hasInventory():
                    # TODO wait for full inventory
                    self.itemBuffer = settings.grid[self.startPosition[0]][self.startPosition[1] + options[self.startPosition[2]]].inventoryOutput.takeItem(
                        'all',
                        settings.activeEntityDB[self.entityID].inventory.size
                    )

                    settings.activeEntityDB[self.entityID].inventory.loadItem(self.itemBuffer)
                    self.taskCurrent += 1

        if(self.taskCurrent == 3):
            # Move Vehical
            if(self.assigned == False):
                settings.activeEntityDB[self.entityID].status = 1
                self.assigned = True

        if(self.taskCurrent==4):
            # Move to new inventory
            if (self.endPosition[2] == 0 or self.endPosition[2] == 2):
                # Handle y change
                if (settings.grid[self.endPosition[0] + options[self.endPosition[2]]][self.endPosition[1]]).hasInventory():
                    settings.grid[self.endPosition[0] + options[self.endPosition[2]]][self.endPosition[1]].inventory.loadItem(self.itemBuffer)
                    self.taskCurrent += 1

            if (self.endPosition[2] == 1 or self.endPosition[2] == 3):
                # Handle x change

                if (settings.grid[self.endPosition[0]][self.endPosition[1]+ options[self.endPosition[2]]]).hasInventory():
                    settings.grid[self.endPosition[0]][self.endPosition[1]+ options[self.endPosition[2]]].inventory.loadItem(self.itemBuffer)
                    self.taskCurrent += 1

        if(self.taskCurrent==5):
            self.complete()
            self.taskCurrent=6

    def tick(self):
        if (self.taskClaimed == False):
            # Not claimed
            self.task()

    def jobSpecificComplete(self):
        # Undo everything done specific to this job
        self.unassign()


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