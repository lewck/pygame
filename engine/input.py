import pygame

import settings
from dev.testmap import testmap as devmap
from jobset.factory import factory as jobset
from legacy.ui.uis.helper import helper as uishelper
from object.factory import factory as object
from util.tool import tool


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
                    settings.zoom -= 5
                    settings.surface.fill(settings.color['white'])
                elif (event.button == 4):
                    settings.zoom += 5
                    settings.surface.fill(settings.color['white'])

            elif event.type == pygame.MOUSEBUTTONDOWN:
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
                    for each in settings.activeEventDB:
                        if(each.data['attribute']['click']==1):

                            if ((each.data['attribute']['pos'][0] < y < each.data['attribute']['dim'][0]) &
                                    (each.data['attribute']['pos'][1] < x < each.data['attribute']['dim'][1])):

                                each.doEvent()




                    sorted = tool.bubbleSort(values=settings.activeInputDB, localvariable='priority')
                    refined = uishelper.getInputWithLeftClick(sorted)

                    #Evaluate if in click range of any things
                    for each in refined:
                        print(x)
                        print(y)
                        if((each.attribute['pos'][0] < y < each.attribute['dim'][0] )&
                            (each.attribute['pos'][1] < x < each.attribute['dim'][1])):

                            eventhelper.call(each.attribute['eventID'])
                            #in x and y


                            print('TRUE')


                    settings.grid[int(yTile)][int(xTile)].eventClick()
                    object.create(uid='market', y=yTile, x=xTile, direction=2, dev=True)
                elif(event.button == 3):
                    #Right Click
                    object.create(uid='road', y=yTile, x=xTile, direction=0, dev=True)
                elif(event.button == 2):
                    #Middle Mouse
                    object.create(uid='farm_1', y=yTile, x=xTile, direction=0, dev=True)

            elif (event.type == pygame.KEYDOWN):
                if (settings.devInputBuffer == False):
                    if (event.key == pygame.K_F1):
                        jobset.create(typ='collectFromObjectAndStore', startPosition=[0,1,2])

                    if (event.key == pygame.K_F2):
                        devmap.create(0)
                    if (event.key == pygame.K_F3):
                        devmap.create(1)
                    if (event.key == pygame.K_F4):
                        print('spawn dev')
                        object.create(uid='garage', y=0, x=0, direction=0)
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