from webinteract.game import game
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
        if(shop.canPurchase(price)):
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

            # Check if balance objective is met
            print(settings.gameData['objectives'])
            if (settings.gameData['objectives'][0] == '1'):
                if (settings.player.balance > int(settings.gameData['objectives'][1])):
                    settings.winStatus = True
                    settings.currentScreen = 'gameCompleted'
                    gamewebinteract = game()
                    gamewebinteract.markCompleted(settings.gameData['game_id'], settings.gameData['session_id'])
