import settings


#--------------------------------------------------
#  Factory Class
#--------------------------------------------------
class factory:
    @staticmethod
    def create(**kwargs):
        # Return object of UID

        if(not kwargs['type']):
            return eval(kwargs['item']+'()')

        # Generate object with a type
        items = eval(kwargs['item']+'()')
        items.type = kwargs['type']

        return items


#--------------------------------------------------
#  Base Class
#--------------------------------------------------
class base:
    def __init__(self):
        self.itemDetails = settings.itemDB[self.id]

#===========================================================================
#  METAL ITEMS
#===========================================================================------------------------------
#  Metal Brass
#--------------------------------------------------
class metalbrass(base):
    def __init__(self, **args):
        self.id = 'metalbrass'
        super(metalbrass, self).__init__()

#--------------------------------------------------
#  Metal Bronze
#--------------------------------------------------
class metalbronze(base):
    def __init__(self, **args):
        self.id = 'metalbronze'
        super(metalbronze, self).__init__()

#--------------------------------------------------
#  Metal Copper
#--------------------------------------------------
class metalcopper(base):
    def __init__(self, **args):
        self.id = 'metalcopper'
        super(metalcopper, self).__init__()

#--------------------------------------------------
#  Metal Tin
#--------------------------------------------------
class metaltin(base):
    def __init__(self, **args):
        self.id = 'metaltin'
        super(metaltin, self).__init__()

#--------------------------------------------------
#  Metal Zinc
#--------------------------------------------------
class metalzinc(base):
    def __init__(self, **args):
        self.id = 'metalzinc'
        super(metalzinc, self).__init__()


class compoundBase(base):
    def setVars(self):
        self.itemDetails = settings.itemDB[self.id]['type'][self.type]

class plate(compoundBase):
    def __init__(self, **args):
        self.id = 'plate'

    def setType(self, type):
        self.type = type
        compoundBase.setVars(self)


class strip(compoundBase):
    def __init__(self, **args):
        self.id = 'strip'

    def setType(self, type):
        self.type = type
        compoundBase.setVars(self)

