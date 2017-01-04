import settings
import object

class testmap:
    def __init__(self, tid):
        eval('self.loadmap'+str(tid)+'()')

    def loadmap0(self):
        # Map for testing pathfinding
        object.factory.create(uid='genericHouse', y=0, x=1, direction=0, dev=True)
        object.factory.create(uid='genericHouse', y=1, x=1, direction=0, dev=True)
        object.factory.create(uid='genericHouse', y=2, x=1, direction=0, dev=True)
        object.factory.create(uid='genericHouse', y=3, x=1, direction=0, dev=True)
        object.factory.create(uid='genericHouse', y=4, x=1, direction=0, dev=True)
        object.factory.create(uid='genericHouse', y=5, x=1, direction=0, dev=True)
        object.factory.create(uid='genericHouse', y=6, x=1, direction=0, dev=True)
        object.factory.create(uid='genericHouse', y=7, x=1, direction=0, dev=True)
        object.factory.create(uid='genericHouse', y=8, x=1, direction=0, dev=True)

        object.factory.create(uid='genericHouse', y=1, x=3, direction=0, dev=True)
        object.factory.create(uid='genericHouse', y=2, x=3, direction=0, dev=True)
        object.factory.create(uid='genericHouse', y=3, x=3, direction=0, dev=True)
        object.factory.create(uid='genericHouse', y=4, x=3, direction=0, dev=True)
        object.factory.create(uid='genericHouse', y=5, x=3, direction=0, dev=True)
        object.factory.create(uid='genericHouse', y=6, x=3, direction=0, dev=True)
        object.factory.create(uid='genericHouse', y=7, x=3, direction=0, dev=True)
        object.factory.create(uid='genericHouse', y=8, x=3, direction=0, dev=True)
        object.factory.create(uid='genericHouse', y=9, x=3, direction=0, dev=True)

    def loadmap1(self):
        # Map for testing
        object.factory.create(uid='road', y=1, x=1, direction=0, dev=True)
        object.factory.create(uid='road', y=1, x=2, direction=0, dev=True)
        object.factory.create(uid='road', y=1, x=3, direction=0, dev=True)
        object.factory.create(uid='garage', y=1, x=4, direction=3, dev=True)
        object.factory.create(uid='road', y=2, x=3, direction=0, dev=True)

        object.factory.create(uid='road', y=3, x=3, direction=0, dev=True)
        object.factory.create(uid='road', y=4, x=3, direction=0, dev=True)
        object.factory.create(uid='road', y=5, x=3, direction=0, dev=True)
        object.factory.create(uid='road', y=6, x=3, direction=0, dev=True)
        object.factory.create(uid='road', y=6, x=2, direction=0, dev=True)
        object.factory.create(uid='genericHouse', y=5, x=2, direction=2, dev=True)
        object.factory.create(uid='factory_parts', y=2, x=1, direction=2, dev=True, part='body')
        object.factory.create(uid='exports', y=0, x=3, direction=2, dev=True)

    def loadmap2(self):
        object.factory.create(uid='garage', y=0, x=4, direction=2, dev=True)

    def loadmap3(self):
        # Map for testing new game spawns
        object.factory.create(uid='garage', y=0, x=4, direction=2, dev=True)
        object.factory.create(uid='factory_parts', y=0, x=1, direction=2, dev=True)
        object.factory.create(uid='road', y=1, x=1, direction=0, dev=True)
        object.factory.create(uid='road', y=1, x=2, direction=0, dev=True)
        object.factory.create(uid='road', y=1, x=3, direction=0, dev=True)
        object.factory.create(uid='road', y=1, x=4, direction=0, dev=True)

        object.factory.create(uid='exports', y=0, x=9, direction=2, dev=True)


    @staticmethod
    def create(tid):
        return testmap(tid)