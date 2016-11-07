import pygame

import settings
from dev.testmap import testmap as devmap
from jobset.factory import factory as jobset
from object.factory import factory as object
from util.tool import tool
from engine.userinteract.ui import ui
from entity.factory import factory as entity
from engine.userinteract.helper import helper as uihelper

class input():
    @staticmethod
    def listenForEvent():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings.gameExit = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                #Handle all mouse clicks
                clickUsed = False
                x = event.pos[0]
                y = event.pos[1]
                #Int rounds down to nearest tile always
                xTile = (int(x / 50))
                yTile = (int(y / 50))

                if(event.button == 1):
                    #Left Click
                    '''
                    '
                    '   Buffer used because some events change size of activeEventDB (for example an event that closes
                    '   itself). Every event is added to a buffer then performed after the loop is completed in order.
                    '
                    '''
                    if(settings.inputBuffer == []):
                        buffer = []
                        for id, each in settings.activeEventDB.items():
                            if(each.active == True):
                                print('--ide')
                                print(id)
                                print(each)
                                if(each.data['attribute']['click']==1):
                                    if ((each.data['attribute']['pos'][0] < y < each.data['attribute']['pos'][0] +each.data['attribute']['dim'][0]) &
                                            (each.data['attribute']['pos'][1] < x < each.data['attribute']['pos'][1] + each.data['attribute']['dim'][1])):

                                        clickUsed = True
                                        buffer.append(id)

                        for each in buffer:
                            settings.activeEventDB[each].doEvent()

                        if(clickUsed == False):
                            settings.grid[int(yTile)][int(xTile)].eventClick()
                    else:
                        if(settings.inputBuffer[0] == 'setObject'):
                            object.create(uid=settings.inputBuffer[1], y=yTile, x=xTile, direction=2)
                            settings.inputBuffer = []

                elif(event.button == 3):
                    #Right Click
                    object.create(uid='road', y=yTile, x=xTile, direction=0, dev=True)
                elif(event.button == 2):
                    #Middle Mouse
                    object.create(uid='empty', y=yTile, x=xTile, direction=0, dev=True)

            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_F1):
                    devmap.create(2)
                if (event.key == pygame.K_F2):
                    devmap.create(0)
                if (event.key == pygame.K_F3):
                    devmap.create(1)
                if (event.key == pygame.K_F4):
                    object.create(uid='garage', y=0, x=0, direction=0)
                if(event.key == pygame.K_F9):
                    uihelper.toggleModel('menuvehiclebuy')
                if (event.key == pygame.K_F11):
                    entityID = entity.create(uid='car')
