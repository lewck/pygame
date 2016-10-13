from job.base import base
from pathfind import pathFind
from entity.helper import helper as entityhelper
from jobset.helper import helper as jobsethelper

import settings



class moveItem(base):

    '''
        typ='moveItem', startPosition=[1, 1, 0], endPosition=[3, 3, 2], items='all')
    '''

    def __init__(self, **kwargs):
        self.tickListen = [1, 10]
        super(moveItem, self).__init__(**kwargs)
        #begin task 1
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
            #Create path
            path = pathFind(self.startPosition[0], self.startPosition[1], self.endPosition[0], self.endPosition[1], 5)
            self.path = path.find()

            if(self.path):
                #Assign entity to path
                entities = entityhelper.veichleGetAvailable()
                if(entities):
                    self.entity = entities[0]
                    self.assign(entities[0])
                    self.taskCurrent += 1
                else:
                    #No Vehical
                    print('No Active Vehicals')
            else:
                print('waiting for path')


        if(self.taskCurrent == 2):
            #Move items from invA to invB
            if(self.startPosition[2]==0 or self.startPosition[2]==2):
                #Handle y change
                print('checking')

                if(settings.grid[self.startPosition[0]+options[self.startPosition[2]]][self.startPosition[1]]).hasInventory():
                    print('INVENTORY FOUND')
                    #TODO wait for full inventory
                    self.itemBuffer = settings.grid[self.startPosition[0] + options[self.startPosition[2]]][self.startPosition[1]].inventory.takeItem('all', settings.activeEntityDB[self.entity].inventory.size)
                    settings.activeEntityDB[self.entity].inventory.loadItem(self.itemBuffer)
                    self.taskCurrent += 1


            if(self.startPosition[2]==1 or self.startPosition[2]==3):
                pass
                #TODO COMPLETE

        if(self.taskCurrent == 3):
            #Move Vehical
            settings.activeEntityDB[self.entity].status = 1

        if(self.taskCurrent==4):
            #Move to new inventory
            if (self.endPosition[2] == 0 or self.endPosition[2] == 2):
                # Handle y change
                print('checking')
                print(self.endPosition[0])
                print(self.startPosition[1])
                if (settings.grid[self.endPosition[0] + options[self.endPosition[2]]][self.endPosition[1]]).hasInventory():
                    print('INVENTORY FOUND')
                    # TODO wait for full inventory

                    settings.grid[self.endPosition[0] + options[self.endPosition[2]]][self.endPosition[1]].inventory.loadItem(self.itemBuffer)
                    self.taskCurrent += 1

        if(self.taskCurrent==5):
            jobsethelper.complete(self.jobSetID)
            self.taskCurrent=6

    def tick(self):
        if (self.taskClaimed == False):
            # Not claimed
            self.task()