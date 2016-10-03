import settings

from object.generichouse import genericHouse
from object.empty import empty
from object.road import road
from object.farm_1 import farm_1
from object.market import market
from object.garage import garage


class factory:

    @staticmethod
    def create(uid,y,x,direction):
        #Return object of UID
        results = eval(uid+'(y,x,direction)')

        if results.base==0:
            results.base = settings.grid[y][x].base

        settings.grid[y][x] = results