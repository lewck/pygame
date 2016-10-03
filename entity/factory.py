import settings
from entity.car import car

class factory:
    @staticmethod
    def create(**args):
        print(args)
        #Return object of UID
        results = []
        print(args)
        uid = args['uid']
        print(uid)

        result = (eval(uid+'(**args)'))

        return result


