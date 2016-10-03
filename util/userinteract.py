from random import randint
import settings

class messageObject():
    def __init__(self, **kwargs):
        self.attribute = {}
        for key, value in kwargs.items():
            setattr(self, key, value)

    def addAttrs(self, attrs):
        for key, value in attrs.items():
            self.attribute[key] = value


class userInteract:
    def __init__(self):
        self.activeOutput = []
        self.activeInput = []
        print('init')
        self.priority = randint(1,10)
        self.popup()
        self.register()

    def register(self):

        for each in self.activeOutput:
            print('registered')
            settings.activeOutputDB.append(each)

    def popup(self):

        self.activeOutput.append(messageObject(pos=[0,0], type='shape', priority=1))
        self.activeOutput[0].addAttrs({
            'dim': [50,150],
            'color': (randint(0, 255), randint(0, 255), randint(0, 255))
        })

        self.activeOutput.append(messageObject(pos=[0, 100], type='shape', priority=0))
        self.activeOutput[1].addAttrs({
            'dim': [50, 150],
            'color': (randint(0,255), randint(0,255), randint(0,255))
        })

        self.activeOutput.append(messageObject(pos=[0, 0], type='image', priority=5))
        self.activeOutput[2].addAttrs({
            'uid': 'welcome',
            'scale': 0.5
        })


    '''
    def createPopup(self, popupid):
        result = popup.active(popupid)

        self.activeOutput.append(result[0])
        self.activeInput.append(result[1])

        #return ((len(self.activeOutput)-1), results)

    def bufferOutput(self):
        return self.activeOutput

    def bufferInput(self):
        return self.activeInput

    '''