import pygame

class helper():
    @staticmethod
    def loadImage(spriteID):
        stmt = 'sprites/' + str(spriteID) + '.png'
        return pygame.image.load(stmt)