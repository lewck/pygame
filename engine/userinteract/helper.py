from engine.event import event
from engine.out import out as outObj
import settings


class helper:
    @staticmethod
    def getModel(uid):
        # Get instance of model if in activeUI, or get direct from modelDB
        if (uid in settings.activeUI):
            return settings.activeModelDB[settings.activeUI[uid]]


        return settings.activeModelDB[uid]

    @staticmethod
    def toggleModel(modelID, reload=False):

        model = helper.getModel(modelID)

        if (model.active == False):
            if (reload):
                helper.reloadModel(model.id)
            model.activate()
        else:
            model.close()

    @staticmethod
    def reloadModel(modelID):
        model = helper.getModel(modelID)

        model.close()

        # Remove output interfaces
        model.deleteInterface('output')
        # Remove Input Interface
        model.deleteInterface('input')

        model.reload()

        for out in model.input:
            # Register with event handler
            try:
                eid = event.create(modelID=modelID, data=out, trigger=out['attribute']['event'],
                                   args=out['attribute']['eventArgs'])
            except KeyError:
                # Assume no event arguments
                eid = event.create(modelID=modelID, data=out, trigger=out['attribute']['event'], args=0)

        # Register Outputs
        for out in model.output:
            # Register with out handler
            eid = outObj.create(modelID, out)

        model.activate()

    @staticmethod
    def updateAttribute(modelID, att, val):
        model = helper.getModel(modelID)
        setattr(model, att, val)

    @staticmethod
    def closeModel(modelID):
        model = helper.getModel(modelID)
        if (model.active == True):
            model.close()
