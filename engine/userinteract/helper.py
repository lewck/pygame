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
    def toggleModel(uid, reload=False):
        model = helper.getModel(uid)
        if (model.active == False):
            if (reload):
                helper.reloadModel(model.id)

            model.activate()
        else:
            model.close()

    @staticmethod
    def reloadModel(modelID):

        settings.activeModelDB[modelID].close()

        # Remove output interfaces
        settings.activeModelDB[modelID].deleteInterface('output', 'all')
        # Remove Input Interface
        settings.activeModelDB[modelID].deleteInterface('input', 'all')

        settings.activeModelDB[modelID].reload()

        for out in settings.activeModelDB[modelID].input:
            # Register with event handler
            try:
                eid = event.create(modelID=modelID, data=out, trigger=out['attribute']['event'],
                                   args=out['attribute']['eventArgs'])
            except KeyError:
                # Assume no event arguments
                eid = event.create(modelID=modelID, data=out, trigger=out['attribute']['event'], args=0)

        # Register Outputs
        for out in settings.activeModelDB[modelID].output:
            # Register with out handler
            eid = outObj.create(modelID, out)

        settings.activeModelDB[modelID].activate()

    @staticmethod
    def updateAttribute(modelID, att, val):
        setattr(settings.activeModelDB[settings.activeUI[modelID]], att, val)

    @staticmethod
    def closeModel(uid):
        if (settings.activeModelDB[settings.activeUI[uid]].active == True):
            settings.activeModelDB[settings.activeUI[uid]].close()
