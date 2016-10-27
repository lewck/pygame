import settings

class helper:
    @staticmethod
    def complete(jobsetID, jobid):
        #Close Job
        settings.activeJobsetDB[jobsetID].eventTaskComplete()
