import settings
import pygame

class render:

    @staticmethod
    def render():
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