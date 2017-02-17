# Test-bench for code before implementation to the game

from job import factory
import pygame
import settings
import engine.tick
settings.init()
settings.surface = pygame.display.set_mode([100,100])
clock = pygame.time.Clock()

engine.tick.register(5, 'print("Tick!")')

while True:
    print(str(pygame.time.get_ticks()))
    pygame.display.update()
    clock.tick(10)

    for key, each in settings.tick.getAll().items():
        # Create buffer
        if (pygame.time.get_ticks() % each[1] == 0):
            tickBuffer.append(each[2])