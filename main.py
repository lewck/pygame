import pygame

import settings
from dev.log import log
from engine.input import input
from engine.render import render
from engine.tick import tick
from entity.factory import factory as entity
from engine.userinteract.ui import ui
from object.factory import factory as object
from player.player import player
from util.grid import grid

pygame.init()
settings.init()

settings.tick = tick()

settings.devfont = pygame.font.Font(None, 25)
log.create('Main Initiated')
car = 0


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

display_width = 1024
display_height = 768

settings.surface = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Title')

settings.fonts = {
    'primaryFont':{
        10: pygame.font.SysFont(None, 10),
        20: pygame.font.SysFont(None, 20),
        30: pygame.font.SysFont(None, 30),
        40: pygame.font.SysFont(None, 40),
        50: pygame.font.SysFont(None, 50),
        60: pygame.font.SysFont(None, 60),
    },
}

gameExit = False
x = 0
lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0

settings.grid = grid.createEmpty(settings.yMax, settings.xMax)



for y in range(0,settings.yMax):
    for x in range(0,settings.xMax):
        object.create(uid='empty', y=y, x=x, direction=1, dev=True)

settings.player = player()

clock = pygame.time.Clock()
settings.zoom = 10

settings.surface.fill(white)
message = False

settings.activeEntityDB.append(entity.create(uid='car'))
devInputBuffer = False
devInputKey = ''

val = ui.create('menufactorybuy')



mainMenu = False

while not settings.gameExit:
    '''
    '   Check for main menu
    '''
    if(mainMenu == True):


        render.render()
    else:
        '''
        '
        '   Listen for any events
        '
        '''
        input.listenForEvent()

        render.render()

        for each in settings.activeEntityDB:
            if(each.status!=0):
                each.tick()
                each.draw()


        for y in range(0, len(settings.grid)):
            for x in range(0, len(settings.grid[y])):
                settings.grid[y][x].tick()

        for each in settings.tick.getTicks():
            eval(each[1])


    pygame.display.update()
    clock.tick(60)

settings.logObject.close()
pygame.quit()
quit()