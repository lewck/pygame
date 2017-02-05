import pygame
import settings
import re
from engine.out import out
from util.tool import tool


class render:
    @staticmethod
    def renderGrid():
        xmod = 0
        ymod = 0
        # Use a for inside for to iterate the 2d list
        for y in range(0, len(settings.grid)):
            for x in range(0, len(settings.grid[y])):

                # Show the path overlay if it has one
                if (settings.grid[y][x].highlighted == True):
                    settings.grid[y][x].highlight()
                else:
                    # No path on this cell, transform & render base image
                    base = pygame.transform.scale(settings.grid[y][x].base, (50, 50))
                    settings.surface.blit(base, (xmod, ymod))

                    if (settings.grid[y][x].image != 0):
                        # Transform & render overlay image if exists
                        image = pygame.transform.scale(settings.grid[y][x].image,((50,50)))

                        directionModifier = {
                            0: 180,
                            1: 90,
                            2: 0,
                            3: 270,
                        }

                        image = pygame.transform.rotate(image, directionModifier[settings.grid[y][x].direction])

                        settings.surface.blit(image, (xmod, ymod))

                # Change current position of cursor
                xmod += 50
            ymod += 50
            xmod = 0

    @staticmethod
    def renderMenu():
        sortedOutput = out.getActiveByPriority()

        for each in sortedOutput:
            # Scale output
            try:
                scale = each.data['attribute']['scale']

                if(type(each.data['attribute']['scale'])==int):
                    scaleType = 'relative'
                else:
                    # Assume tuple
                    scaleType = 'fixed'
            except KeyError:
                scaleType = 'none'
                scale = 1


            #--------------------------------------------------
            # Handle text data types
            #--------------------------------------------------
            if (each.data['type'] == 'text'):
                # Select font
                try:
                    font = settings.fonts[each.data['attribute']['font']][each.data['attribute']['size']]
                except KeyError:
                    # Use default font if none found
                    settings.logObject.add('Font not found', 2)
                    font = settings.fonts['primaryFont'][each.data['attribute']['size']]

                # Apply variable output string if attribute found
                if('variables' in each.data['attribute']):
                    for i in range(0, len(each.data['attribute']['variables'])):
                        # Iterate each variable, replace occurrence of ID with variable submitted

                        m = re.search('\{'+str(i)+'\}', each.data['attribute']['value'])

                        strStart = each.data['attribute']['value'][:m.start()]
                        strEnd = each.data['attribute']['value'][m.end():]

                        value = strStart+str(eval(each.data['attribute']['variables'][i]))+strEnd

                else:
                    value = each.data['attribute']['value']

                # Render at submitted coordinates
                rendered = font.render(value, True, (each.data['attribute']['color']))
                settings.surface.blit(rendered, (each.data['pos'][1], each.data['pos'][0]))

            #--------------------------------------------------
            # Handle image data types
            #--------------------------------------------------
            elif (each.data['type'] == 'image'):
                # NB scale rounds to nearest int, don't rely on pixel perfect rendering if using scale
                image = pygame.image.load('sprites/'+each.data['attribute']['uid']+'.png')
                w, h = image.get_size()
                if(scaleType=='relative'):
                    rendered = pygame.transform.scale(image, (int(w*scale), int(h*scale)))
                elif(scaleType=='fixed'):
                    rendered = pygame.transform.scale(image, (int(scale[1]), int(scale[0])))
                else:
                    # Assume no scale
                    rendered = image

                settings.surface.blit(rendered, (each.data['pos'][1], each.data['pos'][0]))

            #--------------------------------------------------
            # Handle shape render types
            #--------------------------------------------------
            elif (each.data['type'] == 'shape'):
                # Scale rounds to nearest int, don't rely on pixel perfect rendering if using scale
                if(each.data['attribute']['shape']=='rectangle'):
                    pygame.draw.rect(settings.surface, each.data['attribute']['color'], (each.data['pos'][1], each.data['pos'][0], each.data['attribute']['dim'][1], each.data['attribute']['dim'][0]))
            else:
                settings.logObject.add('Not Rendered type' + str(each.data['type']), 2)

    @staticmethod
    def render():
        # Flush screen
        settings.surface.fill((51, 51, 51))

        # Render components
        render.renderGrid()
        render.renderMenu()