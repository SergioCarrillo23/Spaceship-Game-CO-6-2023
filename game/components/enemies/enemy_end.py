import pygame
from game.components.enemies.enemi import Enemy
from game.utils.constants import ENEMY_4


class Astro(Enemy):
    WIDTH = 160
    HEIGHT = 240
    SPEED_X = 20
    SPEED_Y = 0    
    LIFES = 5

    def __init__(self):
        self.image = ENEMY_4
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)