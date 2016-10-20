import settings

class helper:
    @staticmethod
    def getAvailable():
        toReturn = []

        for id, each in settings.activeEntityDB.items():
            if(each.type == 'vehicle'):
                if(each.status==0):
                    #Free
                    toReturn.append(id)

        return toReturn

    @staticmethod
    def evaluateBest(pos):
        return helper.getAvailable()[-1]
