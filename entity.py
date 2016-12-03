import pygame
import settings
from job.helper import helper as jobhelper
from inventory import inventory
from util.tool import tool
from object.helper import helper as objecthelper

#----------------------------------------------------------------------------
#  Factory Class
#----------------------------------------------------------------------------
class factory:
    @staticmethod
    def create(**args):
        id = tool.genRandomString(16)

        uid = args['uid']
        result = (eval(uid+'(**args, id=id)'))

        if(result.type=='vehicle'):
            # Find suitable storage
            storage = objecthelper.getEmptyStorageAll('vehicle')[0]
            print(storage)

            result.pos = [storage[0], storage[1]]

        settings.activeEntityDB[id] = result

        return id



#----------------------------------------------------------------------------
#  Base Class
#----------------------------------------------------------------------------
class base:
    def __init__(self):
        self.setVars()


    def setVars(self):
        self.tickCount = 0
        self.status = 0
        self.firstMove = True
        pos = []
        self.claimed = False

    def assign(self, jobID):
        self.job = settings.activeJobDB[jobID]

        self.path = settings.pathDB[settings.activeJobDB[jobID].path]
        self.x = self.job.startPosition[1]*50
        self.y = self.job.startPosition[0]*50
        self.direction = 1
        self.jobID = jobID

    def unassign(self):
        self.job = 0
        self.path = 0
        self.x = 0
        self.y = 0
        self.direction = 0
        self.jobID = 0
        self.status = 0
        self.claimed = False


    def tick(self):
        if(self.tickListen!=False):
            self.tickCount += 1
            for i in range(0, len(self.tickListen)):
                if (self.tickCount % self.tickListen[i] == 0):
                    self.doTick(i)
                    if(i==len(self.tickListen)):
                        self.tickCount = 0


    def doMove(self):
        if (self.status == 1):
            xTile = (int(self.x /50))
            yTile = (int(self.y /50))


            for i in range(0, len(self.path[1])):
                for o in range(0, len(self.path[1][i])):
                    if (self.y / 50 == self.path[1][i][o][0] and self.x / 50 == self.path[1][i][o][1]):
                        if (self.direction == 4):
                            # Here
                            self.status = 3
                            jobhelper.complete(self.jobID)

                        currDirection = self.direction
                        self.direction = self.path[1][i][o][2]

            # update location tick
            if (self.direction == 0):
                self.y += -10
            elif (self.direction == 1):
                self.x += 10
            elif (self.direction == 2):
                self.y += 10
            elif (self.direction == 3):
                self.x += -10

        if (self.status == 3):
            # idle
            pass

    def place(self):
        settings.surface.blit(self.image, (self.x*50, self.y*50))

    def draw(self):
        directionRotation = {
            0: 0,
            1: 270,
            2: 180,
            3: 90
        }
        base = pygame.transform.scale(self.image, (50, 50))
        base1 = base

        if(self.direction!=4):
            base1 = pygame.transform.rotate(base, directionRotation[self.direction])

        settings.surface.blit(base1, (self.x, self.y))

    def loadItems(self):
        self.inventory.addItem()


#----------------------------------------------------------------------------
#  Entity > Car
#----------------------------------------------------------------------------
class car(base):
    def __init__(self, **args):
        self.type = 'vehicle'
        super(car, self).setVars()
        self.image = pygame.image.load('sprites/car.png')
        self.tickListen = [5]
        self.inventory = inventory(5)

    def doTick(self, tickID):
        if(tickID==0):
            self.doMove()

#----------------------------------------------------------------------------
#  Entity > Van
#----------------------------------------------------------------------------
class van(base):
    def __init__(self, **args):
        self.type = 'vehicle'
        super(van, self).setVars()
        self.image = pygame.image.load('sprites/van.png')
        self.tickListen = [5]
        self.inventory = inventory(30)

    def doTick(self, tickID):
        if(tickID==0):
            self.doMove()

#----------------------------------------------------------------------------
#  Entity > Lorry
#----------------------------------------------------------------------------
class lorry(base):
    def __init__(self, **args):
        self.type = 'vehicle'
        super(lorry, self).setVars()
        self.image = pygame.image.load('sprites/lorry.png')
        self.tickListen = [5]
        self.inventory = inventory(50)

    def doTick(self, tickID):
        if(tickID==0):
            self.doMove()

