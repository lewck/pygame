import settings
from shop import shop

from object.generichouse import genericHouse
from object.empty import empty
from object.road import road
from object.farm_1 import farm_1
from object.exports import exports
from object.garage import garage
from object.factory_parts import factory_parts



class factory:
    @staticmethod
    def getObject(**kwargs):
        results = eval(kwargs['uid'] + '(**kwargs)')
        return results

    @staticmethod
    def create(**kwargs):
        if('obj' in kwargs):
            result = kwargs['obj']
        else:
            result = factory.getObject(**kwargs)

        if 'y' in kwargs:
            if not (hasattr(result, 'base')):
                #Use existing base
                result.base = settings.grid[kwargs['y']][kwargs['x']].base

            #Assume needs plot
            if 'dev' in kwargs:
                #Force Create
                settings.grid[kwargs['y']][kwargs['x']] = result
                return True

            else:
                #Check balance etc
                if (shop.canPurchase(result.price)):
                    shop.purchase(result.price)
                    settings.grid[kwargs['y']][kwargs['x']] = result
                    return True


        else:
            #Assume wants object
            if (shop.canPurchase(result.price)):
                return result

        return False


