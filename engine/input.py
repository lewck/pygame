import pygame

import settings
from jobset import factory as jobset
import object
from util.tool import tool
from engine.userinteract.ui import ui
import entity
from engine.userinteract.helper import helper as uihelper
from engine.inputbuffer import inputbuffer
from engine.event import event as eventObject
from util.map import map
from pathfind import pathFind
from object.helper import helper as objecthelper

class input():
    @staticmethod
    def listenForEvent():
        for event in pygame.event.get():

            # Check for quit event
            if event.type == pygame.QUIT:
                settings.gameExit = True

            # Check for mouse button event
            elif event.type == pygame.MOUSEBUTTONDOWN:

                clickUsed = False
                # Get position of click
                x = event.pos[0]
                y = event.pos[1]

                # Int rounds down to nearest tile always
                xTile = (int(x / 50))
                yTile = (int(y / 50))

                if(event.button == 1):
                    # Left Click
                    #
                    # Buffer used because some events change size of activeEventDB (for example an event that closes
                    # itself). Every event is added to a buffer then performed after the loop is completed in order.
                    #

                    if (not inputbuffer.isClick()):
                        # No buffer found
                        buffer = []
                        for id, each in eventObject.getActive().items():
                            if(each.data['attribute']['click']==1):
                                # Check if any events are waiting for this region to be clicked, stack all
                                if ((each.data['attribute']['pos'][0] < y <
                                     each.data['attribute']['pos'][0] + each.data['attribute']['dim'][0])&(
                                     each.data['attribute']['pos'][1] < x <
                                     each.data['attribute']['pos'][1] + each.data['attribute']['dim'][1])):

                                    clickUsed = True
                                    buffer.append(id)

                        for each in buffer:
                            # Do all events found
                            settings.activeEventDB[each].doEvent()

                        if(clickUsed == False):
                            # Click tile if an at least one event was not found
                            if(yTile < settings.yMax) & (xTile < settings.xMax):
                                # Call click function if exists
                                try:
                                    settings.grid[int(yTile)][int(xTile)].eventClick()
                                except AttributeError:
                                    pass

                    # Check for left click buffer
                    elif(inputbuffer.getClick()==1):
                        # Create an object at requested position
                        object.factory.create(uid=inputbuffer.getObject(), y=yTile, x=xTile, direction=2)
                        inputbuffer.clear()

                # Check for middle mouse click
                elif (event.button == 3):
                    # Create road at click position
                    object.factory.create(uid='road', y=yTile, x=xTile, direction=0)


            # Check for key event
            elif (event.type == pygame.KEYDOWN):

                # Check for key input buffer
                if(inputbuffer.isKey()):
                    if event.key in range(pygame.K_a, pygame.K_z + 1):
                        # Letter key detected
                        inputbuffer.addKey(event.unicode)
                    elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                        # Number key detected
                        inputbuffer.addKey(event.unicode)
                    elif event.key == (pygame.K_DELETE) or event.key == (pygame.K_BACKSPACE):
                        # Remove key detected
                        inputbuffer.delKey()
                    elif event.key == (pygame.K_RETURN):
                        # Send buffer
                        inputbuffer.complete()

                # Hotkeys
                if(event.key == pygame.K_F9):
                    uihelper.toggle('menuvehiclebuy')
