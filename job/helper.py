import settings

class helper:
    @staticmethod
    def complete(jobID):
        print(settings.activeJobDB)
        for i in range(0, len(settings.activeJobDB)):
            if (settings.activeJobDB[i].jobID == jobID):
                print('found at ' + str(i))
                settings.activeJobDB[i].eventTaskComplete()
