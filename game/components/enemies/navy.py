import pygame
from game.components.enemies.enemi import Enemy
from game.utils.constants import ENEMY_2


class Navy(Enemy):
    WIDTH = 40
    HEIGHT = 60
    SPEED_X = 15
    SPEED_Y = 3    

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
