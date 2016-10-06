from engine.ui.uis.ioobject import ioobject

class base():
    def __init__(self, **kwargs):
        self.activeOutput = []
        self.activeInput = []

        for key, value in kwargs.items():
            setattr(self, key, value)

    def addOutput(self, **kwargs):
        self.activeOutput.append(ioobject(**kwargs, parent=self.getSubClassName()))

    def addOutputAttrs(self, args):
        self.activeOutput[len(self.activeOutput)-1].addAttrs(args)

    def addInput(self, **kwargs):
        self.activeInput.append(ioobject(**kwargs, parent=self.getSubClassName()))

    def addInputAttrs(self, args):
        self.activeInput[len(self.activeInput)-1].addAttrs(args)