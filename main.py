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
from mapgenerator import mapgenerator

pygame.init()
settings.init()

settings.tick = tick()

settings.devfont = pygame.font.Font(None, 25)
log.create('Main Initiated')
car = 0


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

display_width = settings.xMax*50
display_height = (settings.yMax * 50)+50

#settings.surface = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
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

for key, value in settings.activeUI.items():
    settings.activeUI[key] = ui.create(key)


for y in range(0,settings.yMax):
    for x in range(0,settings.xMax):
        object.create(uid='empty', y=y, x=x, direction=1, dev=True)

object.create(uid='exports', y=0, x=9, direction=2, dev=True)

settings.player = player()

clock = pygame.time.Clock()
settings.zoom = 10

settings.surface.fill(white)
message = False


devInputBuffer = False
devInputKey = ''



mainMenu = False

print(settings.activeUI['defaultoverlay'])
settings.activeModelDB[settings.activeUI['defaultoverlay']].activate()


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

        for key, each in settings.activeEntityDB.items():
            if(each.status!=0):
                each.tick()
                each.draw()


        tickBuffer = []
        for key, each in settings.tick.getTicks().items():
            #Create buffer
            tickBuffer.append(each[2])

        for each in tickBuffer:
            '''
            print('DEBUG JOB DB: '+str(settings.activeJobDB))
            print('DEBUG EACH '+str(each))
            print('DEBUG ALL ITEMS'+str(settings.tick.getTicks().items()))
            '''
            try:
                eval(each)
            except KeyError:
                #the tick was unregistered mid buffer, this no longer exists
                pass


    pygame.display.update()
    clock.tick(120)

settings.logObject.close()
pygame.quit()
quit()