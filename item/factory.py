import settings

from item.vegetable.vegetableCarrot import vegetableCarrot
from item.body import body
from item.plane import plane
from item.metal.metalbrass import metalbrass
from item.metal.metalcopper import metalcopper
from item.metal.metalzinc import metalzinc
from item.brass.brassnails import brassnails


class factory:
    @staticmethod
    def create(**args):
        #Return object of UID
        results = []
        print(args['item'])
        results.append(eval(args['item']+'()'))

        return results