from object.base import base
from inventory import inventory

class exports(base):
    def __init__(self, **kwargs):
        print('init exports')
        self.type = 'exports'
        self.title = 'exports'
        super(exports, self).setVars(image=self.title, **kwargs)
        self.passable = []
        self.inventory = inventory(25)
        self.price = 500

    def eventClick(self):
        super(exports, self).log()