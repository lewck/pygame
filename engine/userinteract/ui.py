from engine.userinteract.model.welcome import welcome
from engine.userinteract.model.menustoragebuy import menustoragebuy
from engine.userinteract.model.menuproducerbuy import menuproducerbuy
from engine.event import event
from engine.out import out as outObj
from util.tool import tool

import settings

class ui:
    @staticmethod
    def create(uid):
        model = []

        model.append(eval(uid+'()'))

        for each in model:
            #Register Model
            modelID = tool.genRandomString(16)

            settings.activeModelDB[modelID] = each

            each.id = modelID
            inReturn = []
            outReturn = []

            #Register Inputs
            for out in each.input:
                #Register with event handler
                try:
                    eid = event.create(modelID=modelID, data=out, trigger=out['attribute']['event'],  args=out['attribute']['eventArgs'])
                except KeyError:
                    #ASsume no event arguments
                    eid = event.create(modelid=modelID, data=out, trigger=out['attribute']['event'], args=0)
                inReturn.append([eid,out['title']])

            # Register Outputs
            for out in each.output:
                # Register with out handler
                eid = outObj.create(modelID, out)
                outReturn.append([eid,out['title']])

            each.addInterfaces(inReturn, outReturn)
        return modelID

    @staticmethod
    def reloadModel(modelID):
        # Register Inputs
        for out in settings.activeModelDB[modelID].input:
            # Register with event handler
            eid = event.create(modelID, out, out['attribute']['event'])

        # Register Outputs
        for out in settings.activeModelDB[modelID].output:
            # Register with out handler
            eid = outObj.create(modelID, out)