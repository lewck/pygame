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
        self.segregations = {}
    
    def addItem(self, itemID, quantity = 1):

        if(len(self.segregations) == 0):
            #Ignore Segregations
            if((len(self.inventory))+quantity <= self.size):

                for i in range(0,quantity):
                    self.inventory.extend(item.create(item=itemID))
                return True

            else:
                print('NOT COMPLETELT FULL')
                if((len(self.inventory))<= self.size):
                    #Not completely full
                    toFill = self.size-(len(self.inventory))
                    for i in range(0, toFill):
                        self.inventory.extend(item.create(item=itemID))
                    return 'INVFULL'
                else:
                    #Completely full
                    return 'INVFULL'

        else:
            #Use segregations
            print('USING SEGREGATIONS')
            if(not itemID in self.segregations):
                return False

            while(self.segregations[itemID][0] > (self.segregations[itemID][1])):

                self.inventory.extend(item.create(item=itemID))
                self.segregations[itemID][1] += 1




    def buildItem(self, id):
        print('build trigger')
        toRemove = settings.itemDB[id]['required']
        print(toRemove)

        for key, quantity in toRemove.items():
            self.removeItem(id= key, quantity=quantity)

        self.addItem(id,1)


    def loadItem(self, itemBuffer):
        if (len(self.segregations) == 0):
            if(len(itemBuffer)< (self.size - (len(self.inventory)-1))):
                self.inventory.extend(itemBuffer)
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
        ##
        if(quantity == 'all'):
            quantity = len(self.inventory)

        if(type=='all'):
            if(len(self.inventory)-1>= quantity):
                #Scrape from top of inventory
                toReturn = self.inventory[0:(quantity)-1]

                for i in range(0, quantity):
                    print(i)
                    self.removeItem(position=0)

                print('returning')
                return(toReturn)

            else:
                #IDK
                print('TORET TRIGGERED')
                toRet = list(self.inventory)

                print('ret'+str(toRet))

                for i in range(0, len(self.inventory)):
                    self.removeItem(position=0)

                print('inv')
                print(self.inventory)
                print('ss'+str(toRet))
                return toRet

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

    def hasAny(self):
        if(len(self.inventory) != 0):
            return True
        return False

    def segregate(self, segregations):
        #Divide the invnetory space do item specific chunks
        perSeg = int( self.size / len(segregations) ) #Use int to round down, this may loose slots

        for each in segregations:
            self.segregations[each] = [perSeg, 0]

        print(self.segregations)

