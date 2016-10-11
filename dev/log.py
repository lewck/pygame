from time import strftime
import settings


class log:
    def __init__(self, text, type):
        self.file = self.openFile()
        self.add(text, type)

    def close(self):
        self.add('Program Terminated Gracefully',0)
        self.file.close()

    def openFile(self):
        file = open('logs/'+strftime("%Y-%m-%d")+"-log.txt", "a")
        return file

    def getDatePrefix(self):
        return strftime("%Y-%m-%d %H:%M:%S")

    def getLevelPrefix(self, type):
        levels = {
            0: 'GENERAL',
            1: 'DEBUG',
            2: 'ERROR',
            4: 'CRITICAL'
        }

        return levels[type]

    def add(self, text, type):
        self.file.write('['+self.getDatePrefix()+'] '+'['+self.getLevelPrefix(type)+'] '+text+'\n')

    @staticmethod
    def create(text, type=0):
        if(settings.log==True):
            settings.logObject.add(text, type)
        else:
            settings.logObject = log(text, type)
            settings.log = True
