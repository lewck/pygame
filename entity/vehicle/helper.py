import settings

class helper:
    @staticmethod
    def getAvailable():
        toReturn = []
        for i in range(0, len(settings.activeEntityDB)):
            if(settings.activeEntityDB[i].type == 'vehicle'):
                if(settings.activeEntityDB[i].status==0):
                    #Free
                    toReturn.append(i)

        return toReturn
