from entity.vehicle.helper import helper as vehiclehelper

class helper:
    '''
    '   HELPER METHODS
    '''

    @staticmethod
    def veichleGetAvailable():
        return (vehiclehelper.getAvailable())

    @staticmethod
    def vehicleEvaluateBest(pos):
        return (vehiclehelper.evaluateBest(pos))