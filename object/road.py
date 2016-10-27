from object.base import base

class road(base):
    def __init__(self, **kwargs):
        self.type = 'transport'
        self.title = 'road'
        super(road, self).setVars(image='road', **kwargs)
        self.passable = [5]

    def eventClick(self):
        pass