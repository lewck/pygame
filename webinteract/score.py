from webinteract.base import base

class score(base):
    def __init__(self):
        #Init parent
        super(score, self).__init__()

    def create(self, nameValue, scoreValue):
        return self.requestCall('score', {'name':nameValue, 'score':scoreValue})
