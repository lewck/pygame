import settings

#--------------------------------------------------
#  Helper Class
#--------------------------------------------------
class helper:
    @staticmethod
    def findItemParents(uid):
        parents = []
        for key, each in settings.itemDB.items():

            if('required' in each):
                if('uid' in each['required']):
                    parents.append(each.title)

        if(len(parents)!=0):
            return parents

        return False