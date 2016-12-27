import settings
import object

class map:
    def __init__(self, tid):
        eval('self.loadmap'+str(tid)+'()')

    def loadmap0(self):
        # New Game Map
        object.factory.create(uid='garage', y=0, x=4, direction=2, dev=True)
        object.factory.create(uid='factory_parts', y=0, x=1, direction=2, dev=True)
        object.factory.create(uid='road', y=1, x=1, direction=0, dev=True)
        object.factory.create(uid='road', y=1, x=2, direction=0, dev=True)
        object.factory.create(uid='road', y=1, x=3, direction=0, dev=True)
        object.factory.create(uid='road', y=1, x=4, direction=0, dev=True)
        object.factory.create(uid='exports', y=0, x=9, direction=2, dev=True)
        object.factory.create(uid='factory_press', y=2, x=9, direction=2, dev=True)
        object.factory.create(uid='factory_puncher', y=8, x=9, direction=2, dev=True)
        object.factory.create(uid='factory_miner', y=5, x=9, direction=2, dev=True)

    def loadmap1(self):
        # Alternative Game Map
        object.factory.create(uid='garage', y=0, x=4, direction=2, dev=True)
        object.factory.create(uid='factory_parts', y=0, x=1, direction=2, dev=True)
        object.factory.create(uid='road', y=1, x=1, direction=0, dev=True)
        object.factory.create(uid='road', y=1, x=2, direction=0, dev=True)
        object.factory.create(uid='road', y=1, x=3, direction=0, dev=True)
        object.factory.create(uid='road', y=1, x=4, direction=0, dev=True)
        object.factory.create(uid='exports', y=0, x=9, direction=2, dev=True)

    @staticmethod
    def create(tid):
        return map(tid)