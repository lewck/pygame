import settings

from item.vegetable.vegetableCarrot import vegetableCarrot
from item.body import body
from item.plane import plane

class factory:
    @staticmethod
    def create(**args):
        #Return object of UID
        results = []
        results.append(eval(args['item']+'()'))

        return results