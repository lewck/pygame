from engine.event import event
from engine.out import out as outObj
import settings


class helper:
    @staticmethod
    def toggleModel(uid, reload=False):
        if(settings.activeModelDB[settings.activeUI[uid]].active == False):
            if(reload):
                helper.reloadModel(settings.activeModelDB[settings.activeUI[uid]].id)

            settings.activeModelDB[settings.activeUI[uid]].activate()
        else:
            settings.activeModelDB[settings.activeUI[uid]].close()

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

        print('reloaded')

    @staticmethod
    def updateAttribute(modelID, att, val):
        setattr(settings.activeModelDB[settings.activeUI[modelID]], att, val)

    @staticmethod
    def closeModel(uid):
        if (settings.activeModelDB[settings.activeUI[uid]].active == True):
            print('TOGGLE OFF')
            settings.activeModelDB[settings.activeUI[uid]].close()