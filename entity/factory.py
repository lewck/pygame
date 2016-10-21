import settings
from entity.car import car
from util.tool import tool

from object.helper import helper as objecthelper


class factory:
    @staticmethod
    def create(**args):
        id = tool.genRandomString(16)

        uid = args['uid']
        result = (eval(uid+'(**args, id=id)'))

        if(result.type=='vehicle'):
            #Find suitable storage
            storage = objecthelper.getEmptyStorageAll('vehicle')[0]
            print(storage)

            result.pos = [storage[0], storage[1]]

        settings.activeEntityDB[id] = result

        return id


