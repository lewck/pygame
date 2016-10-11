import pygame

import settings
from legacy.ui.uis.helper import helper as uishelper
from util.tool import tool


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

        sorted = tool.bubbleSort(values=settings.activeInputDB, localvariable='priority')
        refined = uishelper.getInputWithLeftClick(sorted)

        # Evaluate if in click range of any things
        for each in refined:
            # in x and y
            pygame.draw.rect(settings.surface, settings.color['red'], (
                each.attribute['pos'][1], each.attribute['pos'][0], each.attribute['dim'][1],
                each.attribute['dim'][0]), 0)

    @staticmethod
    def renderMenu():
        #Order by priority
        sor = tool.bubbleSort(values=settings.activeOutDB, localvariable='priority')


        for each in sor:

            try:
                scale = each.data['attribute']['scale']
            except KeyError:
                scale = 1


            if (each.data['type'] == 'text'):
                try:
                    font = settings.fonts[each.data['attribute']['font']][each.data['attribute']['size']]
                except KeyError:
                    settings.logObject.add('Font not found', 2)
                    font = settings.fonts['primaryFont'][20]

                rendered = font.render(each.data['attribute']['value'], True, (each.data['attribute']['color']))
                settings.surface.blit(rendered, (each.data['pos'][1], each.data['pos'][0]))

            elif (each.data['type'] == 'image'):
                #NB scale rounds to nearest int, don't rely on pixel perfect rendering if using scale

                image = pygame.image.load('sprites/'+each.data['attribute']['uid']+'.png')
                w, h = image.get_size()
                rendered = pygame.transform.scale(image, (int(w*scale), int(h*scale)))
                settings.surface.blit(rendered, (each.data['pos'][1], each.data['pos'][0]))

            elif (each.data['type'] == 'shape'):
                #NB scale rounds to nearest int, don't rely on pixel perfect rendering if using scale
                if(each.data['attribute']['shape']=='rectangle'):
                    pygame.draw.rect(settings.surface, each.data['attribute']['color'], (each.data['pos'][1], each.data['pos'][0], each.data['attribute']['dim'][1], each.data['attribute']['dim'][0]))


            else:
                settings.logObject.add('Not Rendered type' + str(each.data['type']), 2)


        # legacy






    @staticmethod
    def render():
        #Flush screen
        settings.surface.fill((255, 255, 255))

        #Render components
        render.renderGrid()
        render.renderMenu()