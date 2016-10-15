from item.factory import factory as item

'''
'
'
'''
class inventory:
    def __init__(self, size, type='item'):
        self.size = size
        self.inventory = []
        self.currentSize = 0
        self.type = type
    
    def addItem(self, itemID, quantity):

        if(self.currentSize+quantity <= self.size):
            for i in range(0,quantity):
                self.inventory.append(item.create(item=itemID, quantity=quantity))
                self.currentSize += 1
            return True
        else:
            if(self.currentSize<= self.size):
                #Not completely full
                toFill = self.size-self.currentSize
                for i in range(0, toFill):
                    self.inventory.append(item.create(item=itemID, quantity=quantity))
                    self.currentSize += 1
                return 'INVFULL'
            else:
                #Completely full
                return 'INVFULL'


    def loadItem(self, itemBuffer):
        if(len(itemBuffer)<self.size - len(self.inventory)):
            self.inventory.append(itemBuffer)

    def removeItem(self, **kwargs):
        if(kwargs['position']):
            #Assume inter-class method
            del self.inventory[kwargs['position']]

    def takeItem(self, type, quantity):
        #
        #   Removes selected items, returns list of removed items
        #
        if(type=='all'):
            if(len(self.inventory)>= quantity):
                #Scrape from top of inventory
                toReturn = self.inventory[0:quantity]
                for i in range(0, quantity):
                    self.removeItem(position=5)

                return(toReturn)

    def isFull(self):
        if (len(self.inventory) == self.size):
            return True
        return False

