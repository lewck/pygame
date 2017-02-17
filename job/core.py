from util.tool import tool
import settings


#--------------------------------------------------
#  Factory Class
#--------------------------------------------------
class factory():
    @staticmethod
    def create(**args):
        # Generate random ID
        jobID = tool.genRandomString()

        # Create instance of job
        settings.activeJobDB[jobID] = eval(args['typ'] + '(**args, jobID = jobID)')

        return jobID

#--------------------------------------------------
#  Base Class
#--------------------------------------------------
class base:
    def __init__(self, **kwargs):
        # Set initial common variables
        self.isClaimed = False
        self.initialVarsSet = False
        self.initVars(**kwargs)
        self.taskClaimed = False
        self.jobSetID = kwargs['parent']

        # Register ticks with handler
        for each in self.tickListen:
            self.ticks = settings.tick.register(each, 'settings.activeJobDB["' + str(self.jobID) + '"].tick()',
                                                self.jobID)

    def initVars(self, **kwargs):
        # Set variables based of dict input
        for key, value in kwargs.items():
            setattr(self, key, value)

    def eventTaskComplete(self):
        # Called by entity when job is completed
        self.taskCurrent += 1

    def close(self):
        # Unset Ticks
        settings.tick.remove(identifier=self.jobID)
        del settings.activeJobDB[self.jobID]

    def complete(self):
        # Call job complete, close job
        settings.activeJobsetDB[self.jobSetID].eventTaskComplete()
        self.jobSpecificComplete()
        self.close()

#===========================================================================
#  Subsidory Classes
#==============================================================
#  Move Item Job
#--------------------------------------------------
class moveItem(base):
    def __init__(self, **kwargs):
        # Initiate job specific vars
        self.tickListen = [1, 10]
        super(moveItem, self).__init__(**kwargs)
        # Begin task 1
        self.taskCurrent = 1
        self.assigned = False


    def task(self):
        options = {
            0: -1,
            1: 1,
            2: 1,
            3: -1
        }

        # Check first stage
        if(self.taskCurrent == 1):
            self.taskCurrent += 1
            # Assign Entity
            settings.activeEntityDB[self.entityID].assign(self.jobID)

        # Check second stage, Move items from invA to invB
        if(self.taskCurrent == 2):
            # Change in Y direction
            if(self.startPosition[2]==0 or self.startPosition[2]==2):

                # Check neighbour has inventory
                if(settings.grid[self.startPosition[0]+options[self.startPosition[2]]][self.startPosition[1]]).hasInventory():
                    # Take the items from inventory
                    self.itemBuffer = settings.grid[self.startPosition[0] + options[self.startPosition[2]]][self.startPosition[1]].inventoryOutput.takeItem(
                        'all',
                        settings.activeEntityDB[self.entityID].inventory.size
                    )

                    # Load items into entity, increment to next task
                    settings.activeEntityDB[self.entityID].inventory.loadItem(self.itemBuffer)
                    self.taskCurrent += 1

            # Change in X direction
            if(self.startPosition[2]==1 or self.startPosition[2]==3):

                if (settings.grid[self.startPosition[0]][self.startPosition[1]+options[self.startPosition[2]]]).hasInventory():
                    self.itemBuffer = settings.grid[self.startPosition[0]][self.startPosition[1] + options[self.startPosition[2]]].inventoryOutput.takeItem(
                        'all',
                        settings.activeEntityDB[self.entityID].inventory.size
                    )

                    settings.activeEntityDB[self.entityID].inventory.loadItem(self.itemBuffer)
                    self.taskCurrent += 1

        if(self.taskCurrent == 3):
            # Move Vehicle and set assigned variable. This prevents the vehicles status being continuously updated
            if(self.assigned == False):
                settings.activeEntityDB[self.entityID].status = 1
                self.assigned = True

        if(self.taskCurrent==4):
            # Move to new inventory
            if (self.endPosition[2] == 0 or self.endPosition[2] == 2):
                # Handle y change
                if (settings.grid[self.endPosition[0] + options[self.endPosition[2]]][self.endPosition[1]]).hasInventory():
                    # Load item, increment task
                    settings.grid[self.endPosition[0] + options[self.endPosition[2]]][self.endPosition[1]].inventory.loadItem(self.itemBuffer)
                    self.taskCurrent += 1

            if (self.endPosition[2] == 1 or self.endPosition[2] == 3):
                # Handle x change

                if (settings.grid[self.endPosition[0]][self.endPosition[1]+ options[self.endPosition[2]]]).hasInventory():
                    # Load item, increment task
                    settings.grid[self.endPosition[0]][self.endPosition[1]+ options[self.endPosition[2]]].inventory.loadItem(self.itemBuffer)
                    self.taskCurrent += 1

        if(self.taskCurrent==5):
            # Complete task
            self.complete()
            self.taskCurrent=6

    def tick(self):
        if (self.taskClaimed == False):
            # Not claimed, do task
            self.task()

    def jobSpecificComplete(self):
        # Undo everything done specific to this job
        # Unassign Entity
        settings.activeEntityDB[self.entityID].unassign()

#-------------------------------------------------
#  Move Vehicle Job
#-------------------------------------------------
class movevehicle(base):
    def __init__(self, **kwargs):
        # Initiate job specific vars
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