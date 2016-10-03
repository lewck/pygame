
class grid:

    @staticmethod
    def createEmpty(y,x):
        toReturn = []

        for tmpy in range(0, y):
            toReturn.append([])
            for tmpx in range(0, x):
                toReturn[tmpy].append(0)

        return toReturn