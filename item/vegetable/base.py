class base:
    def __init__(self):
        self.setVars()

    def setVars(self):
        self.itemDetails = settings.itemDB[self.itemID]
        pass