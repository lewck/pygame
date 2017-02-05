import settings

class grid:
    @staticmethod
    def createEmpty(y,x):
        toReturn = []
        # Generate 2d Array with 0's (fillers) of desired y/x
        for tmpy in range(0, y):
            toReturn.append([])
            for tmpx in range(0, x):
                toReturn[tmpy].append(0)

        return toReturn

    @staticmethod
    def clearGrid():
        # Reset global grid variable
        settings.grid = []

        return True