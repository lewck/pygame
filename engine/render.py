import settings
import pygame
from random import randint
from util.tool import tool
from util.userinteract import userInteract

class render:
    @staticmethod
    def renderGrid():
        xmod = 0
        ymod = 0
        for y in range(0, len(settings.grid)):
            for x in range(0, len(settings.grid[y])):

                if (settings.grid[y][x].highlighted == True):
                    settings.grid[y][x].highlight()
                else:
                    base = pygame.transform.scale(settings.grid[y][x].base, ((5 * settings.zoom), (5 * settings.zoom)))

                    # print(str(x)+''+str(y)+'blit')
                    settings.surface.blit(base, (xmod, ymod))

                    if (settings.grid[y][x].image != 0):
                        # print(str(x) + '' + str(y) + 'Image')
                        image = pygame.transform.scale(settings.grid[y][x].image,
                                                       ((5 * settings.zoom), (5 * settings.zoom)))

                        directionModifier = {
                            0: 180,
                            1: 90,
                            2: 0,
                            3: 270,
                        }

                        image = pygame.transform.rotate(image, directionModifier[settings.grid[y][x].direction])

                        settings.surface.blit(image, (xmod, ymod))

                    if (settings.grid[y][x].devOverlay != 0):
                        rendered = font.render('G:' + str(settings.grid[y][x].devOverlay[0]), True, (255, 0, 0))
                        settings.surface.blit(rendered, (xmod, ymod))
                        rendered = font.render('H:' + str(settings.grid[y][x].devOverlay[1]), True, (255, 0, 0))
                        settings.surface.blit(rendered, (xmod, ymod + 15))
                        rendered = font.render('F:' + str(settings.grid[y][x].devOverlay[2]), True, (255, 0, 0))
                        settings.surface.blit(rendered, (xmod, ymod + 30))

                xmod += 5 * settings.zoom
            ymod += 5 * settings.zoom
            xmod = 0

    @staticmethod
    def renderMenu():
        #Order by priority
        sorted = tool.bubbleSort(values=settings.activeOutputDB, localvariable='priority')
        print(sorted)

        for each in sorted:

            if('scale' in each.attribute):
                scale = each.attribute['scale']
            else:
                scale = 1

            if(each.type=='shape'):
                pygame.draw.rect(settings.surface, each.attribute['color'], (each.pos[1],each.pos[0],each.attribute['dim'][1]*scale,each.attribute['dim'][0]*scale), 0)

            elif (each.type == 'image'):

                img = pygame.image.load('sprites/welcome.png')

                if(scale!=1):
                    img = pygame.transform.scale(img, (200, 300))

                settings.surface.blit(img, (each.pos[1], each.pos[0]))

                print('shape')



    @staticmethod
    def render():
            render.renderGrid()
            render.renderMenu()