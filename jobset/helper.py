import settings

class helper:
    @staticmethod
    def complete(jobsetID):
        settings.activeJobsetDB[jobsetID].eventTaskComplete()
