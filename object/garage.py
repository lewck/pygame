from object.base import base
from inventory import inventory

class garage(base):
    def __init__(self, y, x, direction):
        print('initGarage')
        self.type = 'storageVehicles'
        self.title = 'garage'

        super(garage, self).setVars()

        self.passable = []
        self.inventory = inventory(10, 'vehicles')
        self.price = 50000


    def eventClick(self):
        super(garage, self).log()