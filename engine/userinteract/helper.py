import settings

class helper:
    @staticmethod
    def toggleModel(uid):
        if(settings.activeModelDB[settings.activeUI[uid]].active == False):
            print('TOGGLE')
            settings.activeModelDB[settings.activeUI[uid]].activate()
        else:
            settings.activeModelDB[settings.activeUI[uid]].close()