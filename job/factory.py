from job.moveItem import moveItem
from job.movevehicle import movevehicle
import settings

class factory():

    @staticmethod
    def create(**args):
        length = len(settings.activeJobDB)  # No need to negate one as len starts counting at 1

        settings.activeJobDB.append(eval(args['typ'] + '(**args, jobIndex = length)'))


        return length