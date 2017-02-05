import settings

#--------------------------------------------------
#  Helper Class
#--------------------------------------------------
class helper:
    @staticmethod
    def findItemParents(uid):
        # Find items which are used in other items
        parents = []
        for key, each in settings.itemDB.items():

            if('required' in each):
                if('uid' in each['required']):
                    parents.append(each.title)

        if(len(parents)!=0):
            return parents

        return False

    @staticmethod
    def getPrice(uid, type = None):
        # Return the price of compound/noral items
        if (not type):
            unlockPrice = settings.itemDB[uid]['unlockPrice']
        else:
            # Compound Item
            unlockPrice = settings.itemDB[uid]['type'][type]['unlockPrice']
        return True

    @staticmethod
    def discover(uid, type=None):
        # Set discovered attribute to true
        if (not type):
            settings.itemDB[uid]['discovered'] = True
        else:
            # Compound Item
            settings.itemDB[uid]['type'][type]['discovered'] = True

        return True