from item.metal.metalbase import metalBase

class metalbrass(metalBase):
    def __init__(self, **args):
        self.id = 'metalbrass'
        super(metalbrass, self).__init__()