from random import randint

import settings
from item.helper import helper as itemhelper
from pathfind import pathFind

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
    def checkIfProcessorWaiting(identifier, apos):
        locations = helper.findObjectByUid('factory_' + identifier, True)

        for position in locations:
            # Get Interact Position
            positionInteract = helper.getInteractPosition(position[0], position[1], position[2])
            print('pi')
            print(positionInteract)
            path = pathFind(apos[0], apos[1], positionInteract[0], positionInteract[1], 5)
            if (path.find()):
                return positionInteract

        return False

    @staticmethod
    def evaluateBestStorage(objectAPos, type='item', uid=None):
        # Provide real-cordinates, not interact pos

        objectAPos = helper.getInteractPosition(objectAPos[0], objectAPos[1], objectAPos[2])

        possible = []

        # First check if a job is waiting for it
        for key, each in settings.activeJobsetDB.items():
            if(each.typ == 'waitForItems'):
                if(each.needsItem(uid)):
                    possible.append(helper.getInteractPosition(each.pos[0], each.pos[1], settings.grid[each.pos[0]][each.pos[1]].direction))

        # return first one that is reachable
        if (len(possible) != 0):
            for each in possible:
                path = pathFind(objectAPos[0], objectAPos[1], each[0], each[1], 5)
                if(path.find()):
                    return each


        # Attempt to find factory components needing
        for key, each in settings.processingDB.items():
            if(uid in each['transformations']):
                if('produces' in each['transformations'][uid]):
                    # Non compound
                    temp = helper.checkIfProcessorWaiting(key, objectAPos)
                    if(temp):
                        return temp

                else:
                    # Compound, iterate through subs
                    for keySub, eachSub in each['transformations'][uid]['type'].items():
                        temp = helper.checkIfProcessorWaiting(key, objectAPos)
                        if (temp):
                            return temp


        parents = itemhelper.findItemParents(uid)

        if(not parents):
            selected = helper.findObjectByUid('exports')[0]
            return helper.getInteractPosition(selected[0],selected[1], settings.grid[selected[0]][selected[1]].direction)


        possible = helper.getEmptyStorage(type)[0]
        if (len(possible) != 0):
            return possible[0]


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
    def findObjectByUid(uid, getDir = False):
        results = []
        for y in range(0, len(settings.grid)):
            for x in range(0, len(settings.grid[y])):
                if(settings.grid[y][x].title == uid):
                    pos = [y,x]

                    if(getDir):
                        # Extend with direction if required
                        pos.extend([settings.grid[y][x].direction])

                    results.append(pos)

        return results