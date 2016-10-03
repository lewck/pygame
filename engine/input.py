import pygame
import settings
from object.factory import factory as object
from entity.factory import factory as entity
from pathfind import pathFind
from util.grid import grid
from dev.log import log
from dev.testmap import testmap as devmap
from job.factory import factory as job
from engine.tick import tick
from jobset.factory import factory as jobset
from engine.render import render

class input():
    @staticmethod
    def listenForEvent():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings.gameExit = True
            elif event.type == pygame.MOUSEBUTTONUP:
                # print(event.button)
                if (event.button == 5):
                    settings.zoom -= 5
                    settings.surface.fill(white)
                elif (event.button == 4):
                    settings.zoom += 5
                    settings.surface.fill(white)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                xTile = (int(x / (5 * settings.zoom)))
                yTile = (int(y / (5 * settings.zoom)))
                if (event.button == 1):
                    print('x' + str(xTile))
                    print('y' + str(yTile))
                    settings.grid[int(yTile)][int(xTile)].eventClick()

                    object.create('market', yTile, xTile, 2)
                if (event.button == 3):
                    object.create('road', yTile, xTile, 0)
                if (event.button == 2):
                    object.create('farm_1', yTile, xTile, 0)

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
                        object.create('garage', 0, 0, 0)
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