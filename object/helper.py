from random import randint

import settings
from item.helper import helper as itemhelper


class helper:
    @staticmethod
    def getEmptyStorage(type):
        store = []
        # Extract items with inventory
        for y in range(0, len(settings.grid)):
            for x in range(0, len(settings.grid[y])):
                if (settings.grid[y][x].hasInventory()):
                    # Has invntory
                    if (not settings.grid[y][x].inventory.isFull()) & (settings.grid[y][x].inventory.type == type):
                        # Not full, correct type
                        if(not hasattr(settings.grid[y][x], 'inventoryOutput')):
                            store.append(helper.getInteractPosition(y, x, settings.grid[y][x].direction))

    @staticmethod
    def getEmptyStorageAll(type):
        store = []
        # Extract items with inventory
        for y in range(0, len(settings.grid)):
            for x in range(0,len(settings.grid[y])):
                if(settings.grid[y][x].hasInventory()):
                    # Has invntory
                    if(not settings.grid[y][x].inventory.isFull()) & (settings.grid[y][x].inventory.type==type):
                        #Not full, correct type

                        store.append(helper.getInteractPosition(y,x,settings.grid[y][x].direction))

        return store

    @staticmethod
    def evaluateBestStorage(objectAPos, type='item', uid='null'):
        possible = []

        # First check if a job is waiting for it
        if(uid!='null'):
            for key, each in settings.activeJobsetDB.items():
                if(each.typ == 'waitForItems'):
                    if(each.needsItem(uid)):
                        possible.append(helper.getInteractPosition(each.pos[0], each.pos[1], settings.grid[each.pos[0]][each.pos[1]].direction))

            if (len(possible) != 0):
                return possible[randint(0,len(possible)-1)]

            # Not found with job


            '''
            #Check if end of the line
            parents = itemhelper.findItemParents(uid)
            parentPositions = []
            if(parents):
                for each in parents:
                    parentPositions.append(helper.getInteractPosition())

            return parents[0]
            '''

            # Nobody waiting for it, no parents, must sell
            #TODO PICK BEST
            parents = itemhelper.findItemParents(uid)

            if(not parents):
                selected = helper.findObjectByUid('exports')[0]

                return helper.getInteractPosition(selected[0],selected[1], settings.grid[selected[0]][selected[1]].direction)



            possible = helper.getEmptyStorage(type)[0]
            if (len(possible) != 0):
                return possible[0]


        return False

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


    @staticmethod
    def findObjectByUid(uid):
        results = []
        for y in range(0, len(settings.grid)):
            for x in range(0, len(settings.grid[y])):
                if(settings.grid[y][x].title == uid):
                    results.append([y,x])

        return results