import settings

class helper:
    @staticmethod
    def complete(jobsetID):
        for i in range(0, len(settings.activeJobsetDB)):
            if (settings.activeJobsetDB[i].jobsetID == jobsetID):
                print('found at ' + str(i))
                settings.activeJobsetDB[i].eventTaskComplete()
