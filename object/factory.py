import settings
from shop import shop

from object.generichouse import genericHouse
from object.empty import empty
from object.road import road
from object.farm_1 import farm_1
from object.market import market
from object.garage import garage



class factory:
    @staticmethod
    def getObject(**kwargs):
        results = eval(kwargs['uid'] + '(kwargs["y"],kwargs["x"],kwargs["direction"])')

        if results.base == 0:
            results.base = settings.grid[kwargs['y']][kwargs['x']].base

        return results

    @staticmethod
    def create(**kwargs):
        result = factory.getObject(**kwargs)
        if 'dev' in kwargs:
            #Force Create
            settings.grid[kwargs['y']][kwargs['x']] = result
        else:
            #Check balance etc
            if (shop.purchase(result.price)):
                settings.grid[kwargs['y']][kwargs['x']] = result

