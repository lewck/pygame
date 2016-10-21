import settings

class helper:
    @staticmethod
    def findItemParents(uid):
        for key, each in settings.itemDB.items():
            if('uid' in each['required']):
                return each.title