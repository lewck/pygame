import settings

#----------------------------------------------------------------------------
#  Entity > Helper
#----------------------------------------------------------------------------
class helper:
    @staticmethod
    def veichleGetAvailable():
        toReturn = []
        for id, each in settings.activeEntityDB.items():
            if (each.type == 'vehicle'):
                if (each.status == 0):
                    # Free
                    toReturn.append(id)

        return toReturn

    @staticmethod
    def vehicleEvaluateBest(pos):
        for each in helper.veichleGetAvailable():
            if (settings.activeEntityDB[each].claimed == False):
                settings.activeEntityDB[each].claimed = True
                return each