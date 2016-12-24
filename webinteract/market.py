from webinteract.base import base
import settings


class market(base):
    def __init__(self):
        # Init parent
        super(market, self).__init__()

    def get(self, sortby = None):
        return self.requestCall('getmarketdemand', {'sortby':sortby, 'session_id': settings.gameData['session_id']})

    def verifyCache(self):
        if(self.requestCall('verifymarketcache', {'session_id': settings.gameData['session_id']})):
            return True
        else:
            # Get new cache
            settings.marketCache = self.get()
            return True

    def getDemand(self):
        self.verifyCache()
        return settings.marketCache

    def reduceDemand(self, itemID, quantity):
        self.requestCall('reduceMarketDemand', {'game_id': settings.gameData['game_id'], 'item_id': itemID, 'quantity':quantity})