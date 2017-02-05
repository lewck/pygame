from item import factory as item
import settings

class node():
    def __init__(self, size, type):
        # set initial vars
        self.inventory = []
        self.size = size
        self.type = type

    def hasAny(self):
        # return true if ANY items in inventory
        if(len(self.inventory)>0):
            return True
        return False

    def addItem(self, itemID, quantity, type):
        # Continue to add items until full, return INVFULL callback when full
        count = 0
        while (len(self.inventory) < self.size):
            if(count < quantity):
                self.inventory.extend([item.create(item=itemID, type=type)])
                count += 1
            else:
                return 'INVFULL'


    def removeItem(self, itemID, quantity):
        # Remove until quantity reached or none left
        count = 0
        delBuffer = []

        for i in range(0,len(self.inventory)):
            # check if id is selected id
            if(self.inventory[i].id == itemID):
                # append to remove buffer until count is complete, then break
                if(count < quantity):
                    delBuffer.append(i)
                    count += 1
                else:
                    break

        modifier = 0
        # Delete from remove buffer
        for each in delBuffer:
            del self.inventory[each+modifier]
            modifier += -1

        # Buffer used as changing size of inventory during iteration produces error.

    def takeItem(self, itemID, quantity):
        # Read comments from remove, changes are commented here
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
            # Append item to list before removing
            toReturn.append(self.inventory[i + modifier])
            del self.inventory[i + modifier]
            modifier += -1

        # Return list of removed items
        return toReturn

    def isFull(self):
        if(len(self.inventory) >= self.size):
            return True
        return False

    def has(self, itemID, quantity, type):
        count = 0
        for each in self.inventory:
            # Check if iterated id is item id
            if(each.id==itemID):

                # Verify if type also matches (if provided type required), increment count
                if(type):
                    if(each.type == type):
                        count += 1
                else:
                    count += 1

                if(count == quantity):
                    # return true if quantity of items is met
                    return True

        return False

    def loadItem(self, itemBuffer):
        # Extend current inventory with provided buffer if it fits
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
        # check if has segregation for specified id
        if(id in self.inventory):
            return True
        return False
    
    def addItem(self, **kwargs):
        # Require name (id)
        # Optional : quantity(quantity), type(type)
        # Set quantity to 1 if not provided
        if(not 'quantity' in kwargs):
            kwargs['quantity'] = 1

        # Set type to none if none provided
        if (not 'type' in kwargs):
            kwargs['type'] = None

        # Don't use segregations
        if('all' in self.inventory):
            self.inventory['all'].addItem(kwargs['id'], kwargs['quantity'], kwargs['type'])
        else:
            # Use segregations
            # Verify exists
            if (self.verifySegregation(kwargs['id'])):
                # Has segregation for item, add item
                self.inventory[kwargs['id']].addItem(kwargs['id'], kwargs['quantity'], kwargs['type'])
                return True
            return False

    def removeItem(self, **kwargs):
        # Remove item from inventory, reuqired ID
        # Set quantity to 1 if not provided
        if (not 'quantity' in kwargs):
            kwargs['quantity'] = 1

        if ('all' in self.inventory):
            # Don't use segregations
            self.inventory['all'].removeItem(kwargs['id'], kwargs['quantity'])
        else:
            # Use Segregations
            if (self.verifySegregation(kwargs['id'])):
                return self.inventory[kwargs['id']].removeItem(kwargs['id'], kwargs['quantity'])


    def getInventory(self, segregation='all'):
        # Return inventory node items for specified segregation
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
        # example args = ['id', 'id2']
        perSeg = int(self.size / len(segregations))  # Use int to round down, this may loose slots

        self.inventory = {}

        # Init, save node for each segregation
        for each in segregations:
            self.inventory[each] = node(perSeg, each)

        self.segregated = True

    def takeItem(self, itemID, quantity):
        # Removes selected items, returns list of removed items
        if (quantity == 'all'):
            # Take all
            quantity = len(self.inventory[itemID].inventory)

        if('all' in self.inventory):
            # Don't use segregations
            return (self.inventory['all'].takeItem(itemID, quantity))
        else:
            # Use segregations
            return (self.inventory[itemID].takeItem(itemID, quantity))


    def isFull(self, itemID = 'all'):
        # Return true if full inventory
        return self.inventory[itemID].isFull()


    def has(self, id, quantity, type = None):
        # Check if inventory has quantity of item
        if('all' in self.inventory):
            return self.inventory['all'].has(id, quantity, type)
        else:
            return self.inventory[id].has(id, quantity, type)

    def hasAny(self):
        # Check if inventory has any of items
        for key, each in self.inventory.items():
            if(each.hasAny()):
                return True
        return False
