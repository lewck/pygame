import pygame
import settings

import pygame
import settings

from util.log import log
from engine.input import input
from engine.render import render
from engine.tick import tick
from entity.factory import factory as entity
from engine.userinteract.ui import ui
from object.factory import factory as object
from player.player import player
from util.grid import grid
from webinteract.market import market
from dev.testmap import testmap
from engine.userinteract.helper import helper as uihelper

'''
'
'   BOOTSTRAP CODE
'
'''

#Initiate Depends
pygame.init()
settings.init()

#Begin startup logging
log.create('Main Initiated')

#Initiate Pygame-related vars
settings.tick = tick()
clock = pygame.time.Clock()

#Pre-load Fonts
settings.devfont = pygame.font.Font(None, 25)
settings.fonts = {
    'primaryFont': {
        10: pygame.font.SysFont(None, 10),
        20: pygame.font.SysFont(None, 20),
        30: pygame.font.SysFont(None, 30),
        40: pygame.font.SysFont(None, 40),
        50: pygame.font.SysFont(None, 50),
        60: pygame.font.SysFont(None, 60),
    },
    'monospacedFont': {
        10: pygame.font.SysFont('couriernew', 10),
        20: pygame.font.SysFont('couriernew', 20),
        30: pygame.font.SysFont('couriernew', 30),
        40: pygame.font.SysFont('couriernew', 40),
        50: pygame.font.SysFont('couriernew', 50),
        60: pygame.font.SysFont('couriernew', 60),
    },
}


#Calculate surface width
display_width = 1050
display_height = 550

#Create surface
#Uncomment for full screen settings.surface = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
settings.surface = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Game Title')

#Pre-load User Interfaces (inactive)
for key, value in settings.activeUI.items():
    settings.activeUI[key] = ui.create(key)

settings.currentScreen = 'menu'

'''
'
'   Start Menu
'
'''

settings.activeModelDB[settings.activeUI['menustart']].activate()

while settings.currentScreen=='menu' and not settings.gameExit:
    #Listen for events
    input.listenForEvent()

    #Render the screen
    render.render()


    #Finish frame
    pygame.display.update()
    clock.tick(120)
    

'''
'
'   Init Game
'
'''

#Generate grid
settings.grid = grid.createEmpty(settings.yMax, settings.xMax)

#Define player
settings.player = player()

#Fill grid with grass
for y in range(0,settings.yMax):
    for x in range(0,settings.xMax):
        object.create(uid='empty', y=y, x=x, direction=1, dev=True)


mainMenu = False

settings.activeModelDB[settings.activeUI['defaultoverlay']].activate()
testmap.create(3)

entity.create(uid='car')

#Assign web interacts
settings.webinteractmarket = market()
settings.marketCache = settings.webinteractmarket.get()


#Get market prices
for key, value in settings.gameExcluseUI.items():
    settings.activeUI[key] = ui.create(key)

settings.grid[5][5].highlightAdd(3)

'''
'
'   CORE GAME LOOP
'
'''

uihelper.closeModel('menuloading')
while (settings.currentScreen=='game') and (not settings.gameExit):
    #Listen for events
    input.listenForEvent()

    #Render the screen
    render.render()

    #Tick entities
    for key, each in settings.activeEntityDB.items():
        if(each.status!=0):
            each.tick()
            each.draw()

    #Tick everything else
    tickBuffer = []
    for key, each in settings.tick.getTicks().items():
        #Create buffer
        if(pygame.time.get_ticks()%each[1] == 0):
            tickBuffer.append(each[2])

    for each in tickBuffer:
        try:
            eval(each)
        except KeyError:
            #the tick was unregistered mid buffer, this no longer exists
            pass

    #Finish frame
    pygame.display.update()
    clock.tick(120)


#Game Over
settings.logObject.close()
pygame.quit()
quit()