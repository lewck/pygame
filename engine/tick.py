'''
'
'   Tick class handles registering, and calling ticking
'
'''
class tick:
    def __init__(self):
        self.tick = []

    def register(self, array):
        self.tick.extend(array)

    def getTicks(self):
        return self.tick