from jobset.collectfromobjecetandstore import collectFromObjectAndStore
from jobset.waitForItems import waitForItems
import settings
from util.tool import tool

class factory():

    @staticmethod
    def create(**args):
        jobsetID = tool.genRandomString(16)
        jobsetID = tool.genUniqueID(settings.activeJobsetDB, 16)

        settings.activeJobsetDB[jobsetID] = eval(args['typ']+'(**args, jobsetID = jobsetID)')

        return jobsetID