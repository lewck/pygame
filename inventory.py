from item.factory import factory as item
import settings
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
    
    def addItem(self, itemID, quantity = 1):

        if(self.currentSize+quantity <= self.size):
            for i in range(0,quantity):
                self.inventory.extend(item.create(item=itemID, quantity=quantity))
                self.currentSize += 1
            return True
        else:
            if(self.currentSize<= self.size):
                #Not completely full
                toFill = self.size-self.currentSize
                for i in range(0, toFill):
                    self.inventory.extend(item.create(item=itemID, quantity=quantity))
                    self.currentSize += 1
                return 'INVFULL'
            else:
                #Completely full
                return 'INVFULL'

    def buildItem(self, id):
        print('build trigger')
        toRemove = settings.itemDB[id]['required']
        print(toRemove)

        for key, quantity in toRemove.items():
            self.removeItem(id= key, quantity=quantity)

        self.addItem(id,1)


    def loadItem(self, itemBuffer):
        print(self.inventory)
        if(len(itemBuffer)<self.size - len(self.inventory)):
            print('---')
            self.inventory.extend(itemBuffer)
            print(self.inventory)

    def removeItem(self, **kwargs):

        if('position' in kwargs):
            #Assume inter-class method
            del self.inventory[kwargs['position']]

        if('id' in kwargs):
            count = 0
            deleteBuffer = []
            for i in range(0, len(self.inventory)):
                if(self.inventory[i].id == kwargs['id']) & (count < kwargs['quantity']):
                    deleteBuffer.append(i)
                    count+= 1

            mod = 0
            for i in range(0, len(deleteBuffer)):
                del self.inventory[i-mod]
                mod += 1

    def takeItem(self, type, quantity):
        #
        #   Removes selected items, returns list of removed items
        #
        if(type=='all'):
            if(len(self.inventory)>= quantity):
                #Scrape from top of inventory
                toReturn = self.inventory[0:(quantity)]

                for i in range(0, quantity):
                    print(i)
                    self.removeItem(position=0)

                print('returning')
                return(toReturn)

            else:
                #IDK
                toReturn = self.inventory
                print('ret')
                print(toReturn)
                for i in range(0, len(self.inventory)):
                    self.removeItem(position=0)

                print(self.inventory)
                return toReturn

    def isFull(self):
        if (len(self.inventory) == self.size):
            return True
        return False

    def has(self, id, quantity):
        count = 0
        for each in self.inventory:
            if (each.id == id):
                count += 1

        if(count>=quantity):
            return True

        return False
