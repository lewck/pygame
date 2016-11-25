from object.base import base
from inventory import inventory

class genericHouse(base):
    def __init__(self, **kwargs):
        self.type = 'storage'
        self.title = 'genericHouse'

        super(genericHouse, self).setVars(image = 'genericHouse', **kwargs)

        self.passable = []
        self.inventory = inventory(20)
        self.price = 200

    def eventClick(self):
        super(genericHouse, self).log()