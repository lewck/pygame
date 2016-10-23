from jobset.collectfromobjecetandstore import collectFromObjectAndStore
from jobset.waitForItems import waitForItems
import settings
from util.tool import tool

class factory():

    @staticmethod
    def create(**args):
        jobsetID = tool.genRandomString()

        settings.activeJobsetDB[jobsetID] = eval(args['typ']+'(**args, jobsetID = jobsetID)')

        return jobsetID