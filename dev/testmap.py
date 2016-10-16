import settings
from object.factory import factory as object

class testmap:
    def __init__(self, tid):
        eval('self.loadmap'+str(tid)+'()')

    def loadmap0(self):
        print('loading')
        object.create(uid='genericHouse', y=0, x=1, direction=0, dev=True)
        object.create(uid='genericHouse', y=1, x=1, direction=0, dev=True)
        object.create(uid='genericHouse', y=2, x=1, direction=0, dev=True)
        object.create(uid='genericHouse', y=3, x=1, direction=0, dev=True)
        object.create(uid='genericHouse', y=4, x=1, direction=0, dev=True)
        object.create(uid='genericHouse', y=5, x=1, direction=0, dev=True)
        object.create(uid='genericHouse', y=6, x=1, direction=0, dev=True)
        object.create(uid='genericHouse', y=7, x=1, direction=0, dev=True)
        object.create(uid='genericHouse', y=8, x=1, direction=0, dev=True)

        object.create(uid='genericHouse', y=1, x=3, direction=0, dev=True)
        object.create(uid='genericHouse', y=2, x=3, direction=0, dev=True)
        object.create(uid='genericHouse', y=3, x=3, direction=0, dev=True)
        object.create(uid='genericHouse', y=4, x=3, direction=0, dev=True)
        object.create(uid='genericHouse', y=5, x=3, direction=0, dev=True)
        object.create(uid='genericHouse', y=6, x=3, direction=0, dev=True)
        object.create(uid='genericHouse', y=7, x=3, direction=0, dev=True)
        object.create(uid='genericHouse', y=8, x=3, direction=0, dev=True)
        object.create(uid='genericHouse', y=9, x=3, direction=0, dev=True)

    def loadmap1(self):
        print('loading')
        object.create(uid='road', y=1, x=1, direction=0, dev=True)
        object.create(uid='road', y=1, x=2, direction=0, dev=True)
        object.create(uid='road', y=1, x=3, direction=0, dev=True)
        object.create(uid='garage', y=1, x=4, direction=3, dev=True)
        #object.create('garage', 1,4,3)
        object.create(uid='road', y=2, x=3, direction=0, dev=True)
        object.create(uid='road', y=3, x=3, direction=0, dev=True)
        object.create(uid='road', y=4, x=3, direction=0, dev=True)
        object.create(uid='road', y=5, x=3, direction=0, dev=True)
        object.create(uid='road', y=6, x=3, direction=0, dev=True)
        object.create(uid='road', y=6, x=2, direction=0, dev=True)
        object.create(uid='genericHouse', y=5, x=2, direction=2, dev=True)
        object.create(uid='farm_1', y=0, x=1, direction=2, dev=True)

    def loadmap2(self):
        print('loading')


        for i in range(1,10):
            object.create(uid='genericHouse', y=1, x=i, direction=2, dev=True)
            object.create(uid='road', y=2, x=i, direction=0, dev=True)

        object.create(uid='genericHouse', y=2, x=0, direction=1, dev=True)
        object.create(uid='genericHouse', y=3, x=0, direction=1, dev=True)
        object.create(uid='genericHouse', y=4, x=0, direction=1, dev=True)
        object.create(uid='genericHouse', y=5, x=0, direction=1, dev=True)

        object.create(uid='road', y=3, x=1, direction=0, dev=True)
        object.create(uid='road', y=4, x=1, direction=0, dev=True)
        object.create(uid='road', y=5, x=1, direction=0, dev=True)

        object.create(uid='road', y=3, x=9, direction=0, dev=True)
        object.create(uid='road', y=4, x=9, direction=0, dev=True)

        for i in range(1,10):
            object.create(uid='genericHouse', y=6, x=i, direction=0, dev=True)
            object.create(uid='road', y=5, x=i, direction=0, dev=True)

        object.create(uid='genericHouse', y=2, x=10, direction=3, dev=True)
        object.create(uid='road', y=2, x=10, direction=0, dev=True)
        object.create(uid='road', y=2, x=11, direction=0, dev=True)
        object.create(uid='genericHouse', y=4, x=10, direction=3, dev=True)
        object.create(uid='genericHouse', y=5, x=10, direction=3, dev=True)


    @staticmethod
    def create(tid):
        return testmap(tid)