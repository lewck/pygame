import settings
from util.grid import grid
from util.tool import tool
import time



class pathFind():
    def __init__(self, y,x,y1,x1, entity):
        self.xbegin = x
        self.ybegin = y
        self.xend = x1
        self.yend = y1
        self.entity = entity
        self.closed = []
        self.open = []
        self.sets=[x,y,x1,y1]

    def isPassible(self, y, x):
        if (settings.grid[y][x].isPassible(self.entity)):
            return True

    def checkClosed(self,y,x):
        for each in self.closed:
            if(each[1]==x and each[0]==y):
                return True
        return False

    def isOpen(self,y,x):
        for each in self.open:
            if(each.x==x and each.y==y):
                return True
        return False

    def checkNeighbours(self):
        #Up
        if(self.current.y-1>=0):
            if(not self.checkClosed(self.current.y-1, self.current.x))and self.isPassible(self.current.y-1, self.current.x ) and (not(self.isOpen(self.current.y-1, self.current.x))):
                #print('checked'+str(self.current.y-1)+' '+str(self.current.x))
                self.open.append(node(self.current.y-1, self.current.x,[self.current.y, self.current.x,0,  self.current.parent], self.sets))
        #Left
        if (self.current.x - 1 >= 0):
            if (not self.checkClosed(self.current.y, self.current.x-1)) and self.isPassible(self.current.y, self.current.x-1) and (not(self.isOpen(self.current.y, self.current.x-1))):
                #print('checked' + str(self.current.y) + ' ' + str(self.current.x-1))
                self.open.append(node(self.current.y, self.current.x-1,[self.current.y, self.current.x,3, self.current.parent], self.sets))
        #Right
        if (self.current.x+1 <= settings.xMax -1):
            if (not self.checkClosed(self.current.y, self.current.x+1))and self.isPassible(self.current.y, self.current.x+1) and (not(self.isOpen(self.current.y, self.current.x+1))):
                #print('checked' + str(self.current.y) + ' ' + str(self.current.x-1))
                self.open.append(node(self.current.y, self.current.x+1,[self.current.y, self.current.x, 1,self.current.parent], self.sets))
        #Down
        if (self.current.y+1 <= settings.yMax -1):
            if (not self.checkClosed(self.current.y + 1, self.current.x))and self.isPassible(self.current.y+1, self.current.x) and (not(self.isOpen(self.current.y+1, self.current.x))):
                #print('checked'+str(self.current.y-1)+' '+str(self.current.x))
                self.open.append(
                    node(self.current.y+1, self.current.x, [self.current.y, self.current.x,2, self.current.parent],
                        self.sets))

    def lowestF(self):
        lowest = 0
        for i in range (0, len(self.open)-1):
            if self.open[i].fcost < self.open[lowest].fcost:
                lowest = i

        return lowest

    def close(self, y,x):
        self.closed.append([y,x])

    def find(self):
        self.current = node(self.ybegin, self.xbegin, [self.ybegin, self.xbegin], self.sets)
        self.close(self.ybegin, self.xbegin)
        self.checkNeighbours()
        #print('checking N')
        #print(self.open)

        cur = 0
        while self.open:
            #print(self.open)
            #print('Checking Open')
            pos = self.lowestF()
            self.current = self.open[pos]
            #print('Current = '+str(self.current.y)+' '+str(self.current.x))
            self.checkNeighbours()
            #print('Checking Neighbours')
            self.close(self.current.y,self.current.x)
            self.open.pop(pos)
            #print('Closed Self')

            if self.current.x==self.xend and self.current.y==self.yend:
                print('success path find')
                return(self.organise([[self.current.y, self.current.x, 4], self.current.parent]))


        return False

    def organise(self, check):
        store = []
        while True:
            #print(check)  # uncomment for sort debug
            if (check[0] == -1):
                break
            else:
                store.insert(0, [check[0][0], check[0][1], check[0][2]])
                check = check[1]

        for each in store:
            #print(each)
            settings.grid[each[0]][each[1]].highlightAdd(each[2]) #Highlight
            pass


        #print(store)
        pathID = tool.genRandomString()

        settings.pathDB[pathID] = ([[[0, 0], [9, 9]], [store]])

        return pathID

class node():
    def __init__(self,y,x,parent,sets):
        self.x = x
        self.y = y
        self.gcost = (abs(x - sets[0])) + (abs(y - sets[1]))
        self.hcost = (abs(x - sets[2])) + (abs(y - sets[3]))
        self.fcost = self.gcost + self.hcost
        if(len(parent)==2):
            self.parent = [-1]
        else:
            self.parent = [[parent[0],parent[1],parent[2]],parent[3]]
