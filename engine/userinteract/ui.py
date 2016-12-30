from engine.userinteract.model.welcome import welcome
from engine.userinteract.model.menustoragebuy import menustoragebuy
from engine.userinteract.model.menuproducerbuy import menuproducerbuy
from engine.userinteract.model.defaultoverlay import defaultoverlay
from engine.userinteract.model.factoryminermenu import factoryminermenu
from engine.userinteract.model.factorypartsmenu import factorypartsmenu
from engine.userinteract.model.factorypartsselectpart import factorypartsselectpart
from engine.userinteract.model.menuvehiclebuy import menuvehiclebuy
from engine.userinteract.model.menumarketstatus import menumarketstatus
from engine.userinteract.model.menuunlock import menuunlock
from engine.userinteract.model.menustart import menustart
from engine.userinteract.model.menustartonlinegame import menustartonlinegame
from engine.userinteract.model.menuloading import menuloading
from engine.userinteract.model.menustart import menustart
from engine.userinteract.model.gamesettings import gamesettings
from engine.userinteract.model.menugameend import menugameend
from engine.userinteract.model.menujoingame import menujoingame
from engine.userinteract.model.menufactorybuy import menufactorybuy
import engine.userinteract.model

from engine.event import event
from engine.out import out as outObj
from util.tool import tool

import settings

class ui:
    @staticmethod
    def make(uid):
        # private method for initiating a model
        modelID = tool.genRandomString(16)

        try:
            model = eval(uid + '(id = modelID)')
        except NameError:
            # Model not defined/imported, exit
            settings.logObject.add('Model "' + str(uid) + '" failed to initiate', 2)
            return False

        inReturn = []
        outReturn = []

        # Register Inputs
        for out in model.input:
            # Register with event handler
            try:
                eid = event.create(modelID=modelID, data=out, trigger=out['attribute']['event'],
                                   args=out['attribute']['eventArgs'])
            except KeyError:
                # Assume no event arguments
                eid = event.create(modelID=modelID, data=out, trigger=out['attribute']['event'], args=0)

            inReturn.append([eid, out['title']])

        # Register Outputs
        for out in model.output:
            # Register with out handler
            eid = outObj.create(modelID, out)
            outReturn.append([eid, out['title']])

        model.addInterfaces(inReturn, outReturn)

        return (modelID, model)

    @staticmethod
    def create(uid):
        # Make
        try:
            modelID, model = ui.make(uid)
        except TypeError:
            # Assume received bool (false)
            return False

        # Register Model
        settings.activeModelDB[modelID] = model

        return modelID

    def getInstance(self):
        # Use to get an instance of the model, opposed to a globally assigned
        pass