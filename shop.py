import settings

class shop:
    @staticmethod
    def canPurchase(price):
        if(price <= settings.player.balance):
            return True
        else:
            return False

    @staticmethod
    def purchase(price):
        settings.player.balance += -price

    @staticmethod
    def sell(items):
        #Check if cache needs to be busted


        for each in items:
            settings.webinteractmarket.verifyCache()
            itemUsed = False
            for cache in settings.marketCache:
                if(cache['itemid'] == each.id):
                    # Sell
                    itemUsed = True
                    settings.player.balance += settings.itemDB[each.id]['sellPrice'] + cache['current_demand_addition']

                    # Update demands
                    settings.webinteractmarket.reduceDemand(each.id, 1)
                    break

            if(not itemUsed):
                settings.player.balance += settings.itemDB[each.id]['sellPrice']
