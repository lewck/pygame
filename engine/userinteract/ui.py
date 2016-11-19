from engine.userinteract.model.welcome import welcome
from engine.userinteract.model.menustoragebuy import menustoragebuy
from engine.userinteract.model.menuproducerbuy import menuproducerbuy
from engine.userinteract.model.defaultoverlay import defaultoverlay
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

import engine.userinteract.model

from engine.event import event
from engine.out import out as outObj
from util.tool import tool

import settings

class ui:
    @staticmethod
    def create(uid):
        modelID = tool.genRandomString(16)

        model = eval(uid+'(id = modelID)')

        #Register Model


        settings.activeModelDB[modelID] = model


        inReturn = []
        outReturn = []


        #Register Inputs
        for out in model.input:
            #Register with event handler
            try:
                eid = event.create(modelID=modelID, data=out, trigger=out['attribute']['event'],  args=out['attribute']['eventArgs'])
            except KeyError:
                #ASsume no event arguments
                eid = event.create(modelID=modelID, data=out, trigger=out['attribute']['event'], args=0)

            inReturn.append([eid,out['title']])

        # Register Outputs
        for out in model.output:
            # Register with out handler
            eid = outObj.create(modelID, out)
            outReturn.append([eid,out['title']])

        model.addInterfaces(inReturn, outReturn)
        return modelID