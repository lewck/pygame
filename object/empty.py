from object.base import base
import random

class empty(base):
    def __init__(self, y, x, direction):
        print('initGrass')

        if(random.randint(0,1)==1):
            val='grass'
        else:
            val='grass1'

        super(empty, self).setVars(y,x,val,0,direction, False)

        self.passable = []

    def eventClick(self):
        super(empty, self).log()

