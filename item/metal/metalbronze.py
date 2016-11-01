from item.metal.metalbase import metalBase

class metalbronze(metalBase):
    def __init__(self, **args):
        self.id = 'metalbronze'
        super(metalbronze, self).__init__()