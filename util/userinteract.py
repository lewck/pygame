from util.uis.popup import popup

class userInteract:
    def __init__(self):
        self.activeOutput = []
        self.activeInput = []
        print('init')

    def createPopup(self, popupid):
        result = popup.active(popupid)

        self.activeOutput.append(result[0])
        self.activeInput.append(result[1])

        #return ((len(self.activeOutput)-1), results)

    def bufferOutput(self):
        return self.activeOutput

    def bufferInput(self):
        return self.activeInput