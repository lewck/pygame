import settings
from pathfind import pathFind
from item.helper import helper as itemhelper

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
    def evaluateBestStorage(objectAPos, type='item', uid='null'):
        possible = []

        #First check if a job is waiting for it
        if(uid!='null'):
            for each in settings.activeJobsetDB:
                if(each.typ == 'waitForItems'):
                    if(each.needsItem(uid)):
                        possible.append(helper.getInteractPosition(each.pos[0], each.pos[1], settings.grid[each.pos[0]][each.pos[1]].direction))

            if (len(possible) != 1):
                return possible[0]

            #Check if end of the line
            parent = itemhelper.findItemParents(uid)
            if(parent):
                print('HAS A PARENT'+str(parent))

        #possible = helper.getEmptyStorage(type)



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