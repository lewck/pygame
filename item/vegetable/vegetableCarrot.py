from item.base import base


class vegetableCarrot(base):

    def __init__(self, **args):
        self.id = 'vegetableCarrot'
        base.__init__(self)

    def eat(self):
        print('u eaten the carrot nice 1')
        print(self.itemID)