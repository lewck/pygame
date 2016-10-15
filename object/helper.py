import settings
from pathfind import pathFind

class helper:

    @staticmethod
    def getEmptyStorage(type):
        store = []
        #Extract items with inventory
        for y in range(0, len(settings.grid)):
            for x in range(0,len(settings.grid[y])):
                if(settings.grid[y][x].hasInventory()):
                    #Has invntory
                    if(not settings.grid[y][x].inventory.isFull()) & (settings.grid[y][x].inventory.type==type):
                        #Not full, correct type
                        store.append(helper.getInteractPosition(y,x,settings.grid[y][x].direction))

        return store

    @staticmethod
    def getAvailableVehicles(type):
        vehicles = []
        for id, each in settings.activeEntityDB.items():
            if(each.status == 0):
                pass

        return vehicles

    @staticmethod
    def evaluateBestStorage(objectAPos, type='item'):
        empty = helper.getEmptyStorage(type)
        if(len(empty)>=1):
            return empty[0]
        return False

        #TODO evalate based on other things
        '''
        if(mode=='distance'):
            #Find closest
            for each in empty:
                path = pathFind(objectAPos[0], objectAPos[1], each[0], each[1], 5)
                if(path.find()):
                    print('pathFound')
        '''

    @staticmethod
    def getInteractPosition(y,x,direction):
        positionModifier = {
            0: -1,
            1: 1,
            2: 1,
            3: -1
        }

        directionModifier = {
            0:2,
            1:3,
            2:0,
            3:1
        }

        if(direction in [0,2]):
            return([y+positionModifier[direction], x, directionModifier[direction]])
        if (direction in [1, 3]):
            return ([y, x+positionModifier[direction], directionModifier[direction]])