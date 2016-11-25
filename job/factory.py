from job.moveItem import moveItem
from job.movevehicle import movevehicle
from util.tool import tool
import settings

class factory():

    @staticmethod
    def create(**args):
        jobID = tool.genRandomString()

        settings.activeJobDB[jobID] = eval(args['typ'] + '(**args, jobID = jobID)')

        return jobID