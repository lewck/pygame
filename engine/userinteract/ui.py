from engine.userinteract.model.welcome import welcome
from engine.event import event
from engine.out import out as outObj
from util.tool import tool

import settings

class ui:
    @staticmethod
    def create(uid):
        model = []

        if(uid==1):
            model.append(welcome())

        for each in model:
            #Register Model
            modelID = tool.genRandomString(16)

            settings.activeModelDB[modelID] = each

            #Register Inputs
            for out in each.input:
                #Register with event handler
                eid = event.create(modelID, out, out['attribute']['event'])

            # Register Outputs
            for out in each.output:
                # Register with out handler
                eid = outObj.create(modelID, out)