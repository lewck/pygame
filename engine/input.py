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

            elif event.type == pygame.MOUSEBUTTONUP:
                '''
                '
                '   Handle Zoom
                '
                '''
                if (event.button == 5):
                    if(settings.zoom != 1):
                        settings.zoom -= 1
                elif (event.button == 4):
                    settings.zoom += 1

            elif event.type == pygame.MOUSEBUTTONDOWN:
                clickUsed = False
                print('MOUSE DOWN')
                '''
                '
                '   Handle Mouse Click
                '
                '''
                x = event.pos[0]
                y = event.pos[1]
                xTile = (int(x / (5 * settings.zoom)))
                yTile = (int(y / (5 * settings.zoom)))

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
                            print('INPUT BUFFER' +str(settings.inputBuffer))
                            object.create(uid=settings.inputBuffer[1], y=yTile, x=xTile, direction=2)
                            settings.inputBuffer = []

                elif(event.button == 3):
                    #Right Click
                    object.create(uid='road', y=yTile, x=xTile, direction=0, dev=True)
                elif(event.button == 2):
                    #Middle Mouse
                    object.create(uid='farm_1', y=yTile, x=xTile, direction=0, dev=True)

            elif (event.type == pygame.KEYDOWN):
                if (settings.devInputBuffer == False):
                    if (event.key == pygame.K_F1):
                        devmap.create(2)

                    if (event.key == pygame.K_F2):
                        devmap.create(0)
                    if (event.key == pygame.K_F3):
                        devmap.create(1)
                    if (event.key == pygame.K_F4):
                        print('spawn dev')
                        object.create(uid='garage', y=0, x=0, direction=0)

                    if(event.key == pygame.K_F9):
                        uihelper.toggleModel('menuvehiclebuy');

                    if (event.key == pygame.K_F10):
                        if (settings.activeUI['menustoragebuy'] == False):
                            settings.activeUI['menustoragebuy'] = ui.create('menustoragebuy')
                        else:
                            settings.activeModelDB[settings.activeUI['menustoragebuy']].close()
                            settings.activeUI['menustoragebuy'] = False

                    if (event.key == pygame.K_F11):
                        entityID = entity.create(uid='car')

                    if (event.key == pygame.K_SLASH):
                        devInputBuffer = True

                else:
                    if (not event.key == pygame.K_RETURN):
                        devInputKey += chr(event.key)
                        print(devInputKey)
                    else:
                        # Run Command
                        devInputBuffer = False
                        eval(devInputKey)