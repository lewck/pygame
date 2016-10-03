from jobset.collectfromobjecetandstore import collectFromObjectAndStore
import settings

class factory():

    @staticmethod
    def create(**args):
        length = len(settings.activeJobsetDB) #No need to negate one as len starts counting at 1

        settings.activeJobsetDB.append(eval(args['typ']+'(**args, jobsetindex = length)'))

        return length