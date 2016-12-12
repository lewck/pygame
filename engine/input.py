import pygame

import settings
from dev.testmap import testmap as devmap
from jobset import factory as jobset
import object
from util.tool import tool
from engine.userinteract.ui import ui
import entity
from engine.userinteract.helper import helper as uihelper
from engine.inputbuffer import inputbuffer
from engine.event import event as eventObject
from util.map import map


class input():
    @staticmethod
    def listenForEvent():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings.gameExit = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Assume mouse click event
                clickUsed = False
                x = event.pos[0]
                y = event.pos[1]

                # Int rounds down to nearest tile always
                xTile = (int(x / 50))
                yTile = (int(y / 50))

                if(event.button == 1):
                    # Left Click
                    '''
                      Buffer used because some events change size of activeEventDB (for example an event that closes
                      itself). Every event is added to a buffer then performed after the loop is completed in order.
                    '''

                    if (not inputbuffer.isClick()):
                        # No buffer found
                        buffer = []
                        for id, each in eventObject.getActive().items():
                            if(each.data['attribute']['click']==1):
                                if ((each.data['attribute']['pos'][0] < y <
                                     each.data['attribute']['pos'][0] + each.data['attribute']['dim'][0])&
                                    (each.data['attribute']['pos'][1] < x <
                                     each.data['attribute']['pos'][1] + each.data['attribute']['dim'][1])):

                                    # A listener was waiting for this event
                                    clickUsed = True
                                    buffer.append(id)

                        for each in buffer:
                            settings.activeEventDB[each].doEvent()

                        if(clickUsed == False):
                            if(yTile < settings.yMax) & (xTile < settings.xMax):
                                settings.grid[int(yTile)][int(xTile)].eventClick()

                    elif(inputbuffer.getClick()==1):
                        # Has Left Click Buffer
                        object.factory.create(uid=inputbuffer.getObject(), y=yTile, x=xTile, direction=2)
                        inputbuffer.clear()

                elif (event.button == 3):
                    object.factory.create(uid='road', y=yTile, x=xTile, direction=0, dev=True)

            elif (event.type == pygame.KEYDOWN):
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

                if (event.key == pygame.K_F1):
                    devmap.create(2)
                if (event.key == pygame.K_F2):
                    devmap.create(0)
                if (event.key == pygame.K_F3):
                    devmap.create(1)
                if (event.key == pygame.K_F4):
                    object.factory.create(uid='factory_press', y=5, x=5, direction=0)
                if (event.key == pygame.K_F5):
                    settings.webinteractmarket.reduceDemand('metalzinc', 5)
                if(event.key == pygame.K_F9):
                    uihelper.toggleModel('menuvehiclebuy')
                if (event.key == pygame.K_F11):
                    entityID = entity.factory.create(uid='car')
