import settings


#--------------------------------------------------
#  Factory Class
#--------------------------------------------------
class factory:
    @staticmethod
    def create(**args):
        # Return object of UID
        results = []
        results.append(eval(args['item']+'()'))

        return results

#--------------------------------------------------
#  Base Class
#--------------------------------------------------
class base:
    def __init__(self):
        self.setVars()

    def setVars(self):
        self.itemDetails = settings.itemDB[self.id]
        pass

#===========================================================================
#  METAL ITEMS
#===========================================================================
class metalBase(base):
    def __init__(self):
        super(metalBase, self).__init__()

#--------------------------------------------------
#  Metal Brass
#--------------------------------------------------
class metalbrass(metalBase):
    def __init__(self, **args):
        self.id = 'metalbrass'
        super(metalbrass, self).__init__()

#--------------------------------------------------
#  Metal Bronze
#--------------------------------------------------
class metalbronze(metalBase):
    def __init__(self, **args):
        self.id = 'metalbronze'
        super(metalbronze, self).__init__()

#--------------------------------------------------
#  Metal Copper
#--------------------------------------------------
class metalcopper(metalBase):
    def __init__(self, **args):
        self.id = 'metalcopper'
        super(metalcopper, self).__init__()

#--------------------------------------------------
#  Metal Tin
#--------------------------------------------------
class metaltin(metalBase):
    def __init__(self, **args):
        self.id = 'metaltin'
        super(metaltin, self).__init__()

#--------------------------------------------------
#  Metal Zinc
#--------------------------------------------------
class metalzinc(metalBase):
    def __init__(self, **args):
        self.id = 'metalzinc'
        super(metalzinc, self).__init__()

#===========================================================================
#  BRASS ITEMS
#===========================================================================
class brassBase(base):
    def __init__(self):
        super(brassBase, self).__init__()

#--------------------------------------------------
#  Brass Dagger
#--------------------------------------------------
class brassdagger(brassBase):
    def __init__(self, **args):
        self.id = 'brassdagger'
        super(brassdagger, self).__init__()

#--------------------------------------------------
#  Brass Nails
#--------------------------------------------------
class brassnails(brassBase):
    def __init__(self, **args):
        self.id = 'brassnails'
        super(brassnails, self).__init__()


#===========================================================================
#  BRONZE ITEMS
#===========================================================================
class bronzebase(base):
    def __init__(self):
        super(bronzebase, self).__init__()

#--------------------------------------------------
#  Bronze Coin
#--------------------------------------------------
class bronzecoin(bronzebase):
    def __init__(self, **args):
        self.id = 'brassdagger'
        super(bronzecoin, self).__init__()

#--------------------------------------------------
#  Copper Plate
#--------------------------------------------------
class copperplate(base):
    def __init__(self, **args):
        self.id = 'copperplate'
        super(copperplate, self).__init__()
