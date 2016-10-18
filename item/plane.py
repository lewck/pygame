from item.base import base


class plane(base):

    def __init__(self, **args):
        self.id = 'plane'
        base.__init__(self)