from object.base import base
from inventory import inventory

class garage(base):
    def __init__(self, **kwargs):
        self.type = 'storageVehicles'
        self.title = 'garage'

        super(garage, self).setVars(image=self.title, **kwargs)

        self.passable = []
        self.inventory = inventory(10, 'vehicle')
        self.price = 50000


    def eventClick(self):
        pass