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
from engine.input import input
from player.player import player


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

font = pygame.font.SysFont(None, 25)

gameExit = False
x = 0
lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0

from pygame.locals import *

settings.grid = grid.createEmpty(settings.yMax, settings.xMax)



for y in range(0,settings.yMax):
    for x in range(0,settings.xMax):
        object.create('empty', y, x, 1)

settings.player = player()

clock = pygame.time.Clock()
settings.zoom = 10

settings.surface.fill(white)
message = False

settings.activeEntityDB.append(entity.create(uid='car'))
devInputBuffer = False
devInputKey = ''


while not settings.gameExit:
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

pygame.quit()
quit()