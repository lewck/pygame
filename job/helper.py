import settings

class helper:
    @staticmethod
    def complete(jobID):
        print(settings.activeJobDB)
        settings.activeJobDB[jobID].eventTaskComplete()
