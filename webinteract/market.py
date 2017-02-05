from webinteract.base import base
import settings


class market(base):
    def __init__(self):
        # Init parent
        super(market, self).__init__()

    def get(self, sortby = None):
        # Call 'getmarketdemand' request to web server, return the result
        return self.requestCall('getmarketdemand', {'sortby':sortby, 'session_id': settings.gameData['session_id']})

    def verifyCache(self):
        # Call 'verifymarketcache' request to web server
        if(self.requestCall('verifymarketcache', {'session_id': settings.gameData['session_id']})):
            # Cache is up to date
            return True
        else:
            # Cash is old, call another web request to get updated cache
            settings.marketCache = self.get()
            return True

    def getDemand(self):
        # Verify the cache, return the cache after verification
        self.verifyCache()
        return settings.marketCache

    def reduceDemand(self, itemID, quantity):
        # Call 'reduceMarketCommand' request to web server, no response needed
        self.requestCall('reduceMarketDemand', {'game_id': settings.gameData['game_id'], 'item_id': itemID, 'quantity':quantity})