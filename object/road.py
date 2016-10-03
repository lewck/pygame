from object.base import base

class road(base):
    def __init__(self, y, x, direction):
        print('initRoad')
        super(road, self).setVars(y,x,'road',0,direction, False)
        self.passable = [5]

    def eventClick(self):
        super(road, self).log()