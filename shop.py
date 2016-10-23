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
        for each in items:
            settings.player.balance += settings.itemDB[each.id]['sellPrice']