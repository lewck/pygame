import settings

class helper:
    @staticmethod
    def complete(jobID):
        settings.activeJobDB[jobID].eventTaskComplete()

    @staticmethod
    def close(jobID):
        settings.activeJobDB[jobID].close()
