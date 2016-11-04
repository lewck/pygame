from webinteract.base import base
import settings


class market(base):
    def __init__(self):
        #Init parent
        super(market, self).__init__()

    def get(self, sortby = 'null'):
        return False
        return self.requestCall('getmarketdemand', {'sortby':sortby})

    def verifyCache(self):
        if(self.requestCall('verifymarketcache')):
            return True
        else:
            #Get new cache
            settings.marketCache = self.get()
            return True
