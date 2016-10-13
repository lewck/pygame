import settings

from item.vegetable.vegetableCarrot import vegetableCarrot

class factory:
    @staticmethod
    def create(**args):
        #Return object of UID
        results = []
        results.append(eval(args['item']+'()'))

        return results