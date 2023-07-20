import pygame
from game.components.enemies.enemi import Enemy
from game.utils.constants import ENEMY_3


class Ovni(Enemy):
    WIDTH = 160
    HEIGHT = 240
    SPEED_X = 25
    SPEED_Y = 4  
    LIFES = 3
    

    def __init__(self):
        self.image = ENEMY_3
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
