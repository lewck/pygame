from legacy.ui.uis.base import base

'''
'   Generates output to the user, no input required other than close message function
'
'''
class popup(base):
    def __init__(self, **kwargs):
        #init
        super(popup, self).__init__(**kwargs)
        self.active()

    def active(self):
        self.subObject = eval(self.subType+'()')
        self.inout = self.subObject.active()
        self.activeOutput = self.inout[0]
        self.activeInput = self.inout[1]

    def close(self):
        self.activeOutput = []
        self.activeInput = []