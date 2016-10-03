import pygame
import settings

import util.uis.popups.welcome as popwelcome


class popup:

    @staticmethod
    def active(popupid):
        font = pygame.font.SysFont(None, 25)
        popupArray = [
            [
                [pygame.image.load('sprites/welcome.png'), [256, 128]],
                [font.render('Hello', True, (255, 0, 0)), [1024 / 2, 768 / 2]]
            ],
            [
                [pygame.image.load('sprites/welcome.png'), [256, 128]],
                [font.render('Hello', True, (255, 0, 0)), [1024 / 2, 768 / 2]]
            ]
        ]



        return popupArray