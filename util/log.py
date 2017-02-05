from time import strftime
import settings


class log:
    def __init__(self, text, type):
        # Setup and init first log message
        self.logmode = 1
        self.file = self.openFile()
        self.add(text, type)

    def close(self):
        # Called upon programme closure
        self.add('Program Terminated Gracefully', 0)
        self.file.close()

    def openFile(self):
        file = open('logs/'+strftime("%Y-%m-%d")+"-log.txt", "a")
        return file

    def getDatePrefix(self):
        return strftime("%Y-%m-%d %H:%M:%S")

    def getLevelPrefix(self, type):
        # Return prefix based on below dict
        levels = {
            0: 'GENERAL',
            1: 'DEBUG',
            2: 'ERROR',
            4: 'CRITICAL'
        }

        return levels[type]

    def add(self, text, type):
        # Add new log entry
        if(self.logmode == 0):
            # Mode 0, only log in file
            self.file.write('['+self.getDatePrefix()+'] '+'['+self.getLevelPrefix(type)+'] '+text+'\n')
        elif(self.logmode ==1):
            # Mode 1, log in file and in console
            print('[' + self.getDatePrefix() + '] ' + '[' + self.getLevelPrefix(type) + '] ' + text + '\n')
            self.file.write('[' + self.getDatePrefix() + '] ' + '[' + self.getLevelPrefix(type) + '] ' + text + '\n')
        elif (self.logmode == 2):
            # Mode 2, log in console only
            print('[' + self.getDatePrefix() + '] ' + '[' + self.getLevelPrefix(type) + '] ' + text + '\n')

    @staticmethod
    def create(text, type=0):
        # Check if log already inited, then call log add.
        if(settings.log==True):
            settings.logObject.add(text, type)
        else:
            settings.logObject = log(text, type)
            settings.log = True
