from random import randint
import settings

class node():
    def __init__(self, pos, entryDir):
        self.pos = pos
        self.entryDir = entryDir
        settings.grid[pos[0]][pos[1]].highlightAdd(entryDir)

class mapgenerator():
    #Generate main paths
    def __init__(self):
        self.generate()

    def generate(self):
        #Make paths
        currentPos = [5,5]
        self.open = []

        while True:
            #Check UP
            if(currentPos[0]-1 >= 0):
                self.open.append(node([currentPos[0] -1, currentPos[1]],0))

            if (currentPos[0] + 1 >= 0):
                self.open.append(node([currentPos[0] + 1, currentPos[1]], 2))

            if (currentPos[1] - 1 >= 0):
                self.open.append(node([currentPos[0], currentPos[1]-1], 3))

            if (currentPos[1] + 1 >= 0):
                self.open.append(node([currentPos[0], currentPos[1]+1], 1))

            if(not (self.open == [])):
                for i in range(0, len(self.open)):
                    if (each.pos[0] - 1 >= 0):

                        if(randint(0,5)>=1) &(self.isOpen([each.pos[0] + 1, each.pos[1]])==False):
                            self.open.append(node([each.pos[0] - 1, each.pos[1]], 0))


                    if (each.pos[0] + 1 >= 0)&(self.isOpen([each.pos[0] + 1, each.pos[1]])==False):

                        if (randint(0, 5) >= 1):
                            self.open.append(node([each.pos[0] + 1, each.pos[1]], 2))



            break

    def isOpen(self, pos):
        for each in self.open:
            if(each.pos == pos):
                return True
        return False
