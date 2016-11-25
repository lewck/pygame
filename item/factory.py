import settings

from item.metal.metalbrass import metalbrass
from item.metal.metalcopper import metalcopper
from item.metal.metalzinc import metalzinc
from item.metal.metaltin import metaltin
from item.metal.metalbronze import metalbronze
from item.brass.brassnails import brassnails
from item.brass.brassdagger import brassdagger
from item.bronze.bronzecoin import bronzecoin


class factory:
    @staticmethod
    def create(**args):
        #Return object of UID
        results = []
        results.append(eval(args['item']+'()'))

        return results