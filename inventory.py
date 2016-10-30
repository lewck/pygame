from item.factory import factory as item
import settings
'''
'
'
'''

class node():
    def __init__(self, size, type):
        self.inventory = []
        self.size = size
        self.type = type

    def addItem(self, itemID, quantity):
        count = 0

        while (len(self.inventory) < self.size):
            if(count < quantity):
                self.inventory.extend(item.create(item=itemID))
                count += 1
            else:
                return 'INVFULL'

    def removeItem(self, itemID, quantity):
        count = 0
        delBuffer = []

        for i in range(0,len(self.inventory)):
            if(self.inventory[i].id == itemID):
                if(count < quantity):
                    delBuffer.append(i)
                    count += 1
                else:
                    break

        modifier = 0
        for each in delBuffer:
            del self.inventory[each+modifier]
            modifier += -1

    def takeItem(self, itemID, quantity):
        count = 0
        delBuffer = []
        for i in range(0, len(self.inventory)):
            if(count < quantity):
                if(self.inventory[i].id == itemID):
                    delBuffer.append(i)
            else:
                break
            count += 1

        modifier = 0
        toReturn = []
        for each in delBuffer:
            toReturn.append(self.inventory[i + modifier])
            del self.inventory[i + modifier]
            modifier += -1

        return toReturn

    def isFull(self):
        if(len(self.inventory) == self.size):
            return True
        return False

    def has(self, itemID, quantity):
        count = 0
        for each in self.inventory:
            if(each.id==itemID):
                count += 1
                if(count == quantity):
                    return True

        return False




class inventory:
    def __init__(self, size, type='item'):
        self.size = size
        self.type = type

        self.inventory = {'all': node(size, type)}

    #Private Function
    def verifySegregation(self, id):
        if(id in self.inventory):
            return True
        return False
    
    def addItem(self, itemID, quantity = 1):

        if('all' in self.inventory):
            print('add')
            self.inventory['all'].addItem(itemID, quantity)
        else:
            # Use segregations
            # Verify exists
            if (self.verifySegregation(itemID)):
                self.inventory[itemID].addItem(itemID, quantity)
                return True
            return False

    def buildItem(self, id):
        toRemove = settings.itemDB[id]['required']
        print(toRemove)

        for key, quantity in toRemove.items():
            self.removeItem(id=key, quantity=quantity)

        #TODO update to add variable quantity
        self.addItem(id, 1)

    def removeItem(self, **kwargs):
        if ('id' in kwargs):

            if ('all' in self.inventory):
                self.inventory['all'].removeItem(kwargs['id'], kwargs['quantity'])
            else:
                # Use Segregations
                if (self.verifySegregation(kwargs['id'])):
                    return self.inventory[kwargs['id']].removeItem(kwargs['id'], kwargs['quantity'])



    def getInventory(self, segregation='all'):
        if(self.verifySegregation(segregation)):
            return (self.inventory[segregation].inventory)


    def loadItem(self, itemBuffer):
        if (len(self.segregations) == 0):
            if(len(itemBuffer)< (self.size - (len(self.inventory.inventory)-1))):
                self.inventory.inventory.extend(itemBuffer)
                return True
            else:
                return False
        else:
            #Use segregations
            for each in itemBuffer:
                if(each.id in self.segregations):
                    if(self.segregations[each.id][0] > (self.segregations[each.id][1])):
                        self.inventory.append(each)
                        self.segregations[each.id][1] += 1

    def segregate(self, segregations):
        # Divide the invnetory space do item specific chunks
        # ['id', 'id2']
        perSeg = int(self.size / len(segregations))  # Use int to round down, this may loose slots

        self.inventory = {}

        for each in segregations:
            self.inventory[each] = node(perSeg, each)

        self.segregated = True

    def takeItem(self, itemID, quantity):
        ##
        #   Removes selected items, returns list of removed items
        ##
        if (quantity == 'all'):
            quantity = len(self.inventory[itemID].inventory)

        if('all' in self.inventory):
            return (self.inventory['all'].takeItem(itemID, quantity))
        else:
            return (self.inventory[itemID].takeItem(itemID, quantity))


    def isFull(self, itemID = 'all'):
        return self.inventory[itemID].isFull()


    def has(self, id, quantity):
        if('all' in self.inventory):
            return self.inventory['all'].has(id, quantity)
        else:
            return self.inventory[id].has(id, quantity)

    def hasAny(self, itemID):
        if(self.has(itemID, 1)):
            return True

