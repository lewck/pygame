import settings
from object.factory import factory as object

class testmap:
    def __init__(self, tid):
        eval('self.loadmap'+str(tid)+'()')

    def loadmap0(self):
        print('loading')
        object.create('genericHouse', 0,1,0)
        object.create('genericHouse', 1,1,0)
        object.create('genericHouse', 2,1,0)
        object.create('genericHouse', 3,1,0)
        object.create('genericHouse', 4,1,0)
        object.create('genericHouse', 5,1,0)
        object.create('genericHouse', 6,1,0)
        object.create('genericHouse', 7,1,0)
        object.create('genericHouse', 8,1,0)

        object.create('genericHouse', 1, 3, 0)
        object.create('genericHouse', 2, 3, 0)
        object.create('genericHouse', 3, 3, 0)
        object.create('genericHouse', 4, 3, 0)
        object.create('genericHouse', 5, 3, 0)
        object.create('genericHouse', 6, 3, 0)
        object.create('genericHouse', 7, 3, 0)
        object.create('genericHouse', 8, 3, 0)
        object.create('genericHouse', 9, 3, 0)

    def loadmap1(self):
        print('loading')
        object.create('road', 1,1,0)
        object.create('road', 1,2,0)
        object.create('road', 1,3,0)
        #object.create('garage', 1,4,3)
        object.create('road', 2,3,0)
        object.create('road', 3,3,0)
        object.create('genericHouse', 3,2,2)

        object.create('farm_1', 0, 1, 2)


    @staticmethod
    def create(tid):
        return testmap(tid)