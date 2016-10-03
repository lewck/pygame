import settings

from item.vegetableCarrot import vegetableCarrot


class factory:
    @staticmethod
    def create(**args):
        #Return object of UID
        results = []
        results.append(eval(settings.itemIDName[args['itemID']][0]+'()'))

        return results