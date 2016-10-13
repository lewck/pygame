from object.base import base
import random

class empty(base):
    def __init__(self, **kwargs):
        print('initGrass')
        self.type = 'placeholder'
        self.title = 'empty'
        super(empty, self).setVars(image = 'empty', base='empty', **kwargs)

        self.passable = []

    def eventClick(self):
        pass

