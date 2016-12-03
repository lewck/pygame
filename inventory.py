from item import factory as item
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

    def hasAny(self):
        if(len(self.inventory)>0):
            return True
        return False

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
                if(self.inventory[i].id == itemID or itemID == 'all'):
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
        if(len(self.inventory) >= self.size):
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

    def loadItem(self, itemBuffer):
        if (len(itemBuffer) < (self.size - (len(self.inventory) - 1))):
            self.inventory.extend(itemBuffer)
            return True
        else:
            return False




class inventory:
    def __init__(self, size, type='item'):
        self.size = size
        self.type = type

        self.inventory = {'all': node(size, type)}

    def verifySegregation(self, id):
        # Private Function
        #
        if(id in self.inventory):
            return True
        return False
    
    def addItem(self, itemID, quantity = 1):
        if('all' in self.inventory):
            self.inventory['all'].addItem(itemID, quantity)
        else:
            # Use segregations
            # Verify exists
            if (self.verifySegregation(itemID)):
                self.inventory[itemID].addItem(itemID, quantity)
                return True
            return False

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
        # Import items from a buffer
        if ('all' in self.inventory):
            self.inventory['all'].loadItem(itemBuffer)
        else:
            # Use segregations
            for each in itemBuffer:
                if(each.id in self.inventory):
                    self.inventory[each.id].loadItem([each])

    def segregate(self, segregations):
        # Divide the inventory space do item specific chunks
        # ['id', 'id2']
        perSeg = int(self.size / len(segregations))  # Use int to round down, this may loose slots

        self.inventory = {}

        for each in segregations:
            self.inventory[each] = node(perSeg, each)

        self.segregated = True

    def takeItem(self, itemID, quantity):
        # Removes selected items, returns list of removed items
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

    def hasAny(self):
        for key, each in self.inventory.items():
            if(each.hasAny()):
                return True
        return False
