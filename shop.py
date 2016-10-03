import settings

class shop:
    @staticmethod
    def purchase(price):
        if(price <= settings.player.balance):
            return True
        else:
            return False