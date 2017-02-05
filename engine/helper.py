import pygame

class helper():
    @staticmethod
    def loadImage(spriteID):
        # Fetch from sprite gallery, initiate with pygame
        stmt = 'sprites/' + str(spriteID) + '.png'
        return pygame.image.load(stmt)