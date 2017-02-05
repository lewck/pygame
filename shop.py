from webinteract.game import game
import settings

class shop:
    @staticmethod
    def canPurchase(price):
        # Return true if price less than balance
        if(price <= settings.player.balance):
            return True
        else:
            return False

    @staticmethod
    def purchase(price):
        # Deduct price from balance if can afford
        if(shop.canPurchase(price)):
            settings.player.balance += -price
            return True
        return False

    @staticmethod
    def sell(items):
        # Sell items
        for each in items:
            # Check if cache needs to be busted for the item

            settings.webinteract['market'].verifyCache()
            itemUsed = False
            for cache in settings.marketCache:
                # Items with updated cache
                if(cache['itemid'] == each.id):
                    # Sell
                    itemUsed = True
                    settings.player.balance += settings.itemDB[each.id]['sellPrice'] * cache['current_demand_addition']

                    # Update demands
                    settings.webinteract['market'].reduceDemand(each.id, 1)

                    break

            if(not itemUsed):
                # No cache, sell
                if('discovered' in settings.itemDB[each.id]):
                    # Non Compound
                    settings.player.balance += settings.itemDB[each.id]['sellPrice']
                else:
                    # Compound
                    settings.player.balance += settings.itemDB[each.id]['type'][each.type]['sellPrice']

            # Check if balance objective is met
            if (int(settings.gameData['objectives'][0]) == 1):
                # Balance Objective
                if (settings.player.balance > int(settings.gameData['objectives'][1])):

                    # Set winstatus, change to win screen, send web confirmation
                    settings.winStatus = True
                    settings.currentScreen = 'gameCompleted'
                    gamewebinteract = game()
                    gamewebinteract.markCompleted(settings.gameData['game_id'], settings.gameData['session_id'])
