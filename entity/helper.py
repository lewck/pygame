import settings

#--------------------------------------------------
#  Entity Helper
#--------------------------------------------------
class helper:
    @staticmethod
    def veichleGetAvailable():
        # Return a list of all vehicles that are not busy
        toReturn = []
        for id, each in settings.activeEntityDB.items():
            if (each.type == 'vehicle'):
                if (each.status == 0):
                    # Free
                    toReturn.append(id)

        return toReturn

    @staticmethod
    def vehicleEvaluateBest(pos):
        # Return first vehicle which is not claimed
        for each in helper.veichleGetAvailable():
            if (settings.activeEntityDB[each].claimed == False):
                settings.activeEntityDB[each].claimed = True
                return each