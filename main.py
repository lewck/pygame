import pygame

import entity
import object
import settings
from dev.testmap import testmap
from engine.input import input
from engine.render import render
from engine.tick import tick
from engine.userinteract.helper import helper as uihelper
from engine.userinteract.ui import ui
from player import player
from util.grid import grid
from util.log import log
from webinteract.game import game
from webinteract.market import market
from util.map import map
import json


# Initial Setup & Housekeeping
# Initiate Depends
pygame.init()
settings.init()

# Begin startup logging
log.create('Main Initiated')

# Initiate Pygame-related vars
settings.tick = tick()
clock = pygame.time.Clock()


# Mix config with globals
try:
    f = open('config.json', 'r')
    try:
        config = json.loads(f.read())
        # Assign globals from settings
        settings.APIKEY = config['api_key']
        settings.remoteURL = config['server_url']
    except json.decoder.JSONDecodeError:
        log.create('JSON decode error')
        settings.gameExit = True
except FileNotFoundError:
    log.create('Config file could not be found')
    settings.gameExit = True



# Pre-load Fonts
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

# Create surface
settings.surface = pygame.display.set_mode(settings.canvasDimensions)
pygame.display.set_caption('Little Factory')

#TODO make this real icon
pygame.display.set_icon(pygame.image.load('sprites/favicon.png'))

# Pre-load User Interfaces (inactive)
for key, value in settings.activeUI.items():
    settings.activeUI[key] = ui.create(key)

# Open start menu UI
uihelper.toggleModel('menustart')

# Start Menu Loop
while settings.currentScreen=='menu' and not settings.gameExit:
    #Listen for events
    input.listenForEvent()

    #Render the screen
    render.render()

    #Finish frame
    pygame.display.update()
    clock.tick(30)

if(settings.currentScreen == 'game'):
    # Initiate Pre Game Variables
    # Generate grid
    settings.grid = grid.createEmpty(settings.yMax, settings.xMax)

    # Fill grid with grass
    for y in range(0, settings.yMax):
        for x in range(0, settings.xMax):
            object.factory.create(uid='empty', y=y, x=x, direction=1, dev=True)

    # Define player
    settings.player = player()

    # Pre game setup
    uihelper.toggleModel('defaultoverlay')
    map.create(0)
    entity.factory.create(uid='car')


    # Assign web interacts
    settings.webinteract['market'] = market()
    settings.marketCache = settings.webinteract['market'].get()
    settings.webinteract['game'] = game()

    # Get market prices
    for key, value in settings.gameExcluseUI.items():
        settings.activeUI[key] = ui.create(key)

    # Register periodic server ping tick event
    devTick = settings.tick.register(50000, "settings.webinteract['game'].checkCompleted()")

    # Close Loading overlay
    uihelper.closeModel('menuloading')


    # Core Game Loop
    while (settings.currentScreen=='game') and (not settings.gameExit):
        # Listen for events
        input.listenForEvent()

        # Render the screen
        render.render()

        # Tick entities
        for key, each in settings.activeEntityDB.items():
            if(each.status!=0):
                each.tick()
                each.draw()

        # Tick everything else
        tickBuffer = []
        for key, each in settings.tick.getAll().items():
            #Create buffer
            if(pygame.time.get_ticks()%each[1] == 0):
                tickBuffer.append(each[2])

        for each in tickBuffer:
            try:
                eval(each)
            except KeyError:
                # the tick was unregistered mid buffer, this no longer exists
                pass

        # Finish frame
        pygame.display.update()
        clock.tick(60)



# End Of Game
if(settings.currentScreen == 'gameCompleted'):
    # End game setup
    uihelper.updateAttribute('menugameend', 'winstatus', settings.winStatus)
    uihelper.toggleModel('menugameend', True)

    # End game loop
    while (settings.currentScreen=='gameCompleted') and (not settings.gameExit):
        # Listen for events
        input.listenForEvent()

        # Render the screen
        render.render()

        # Finish frame
        pygame.display.update()
        clock.tick(30)


# Game Over, cleanup
settings.logObject.close()
pygame.quit()
quit()