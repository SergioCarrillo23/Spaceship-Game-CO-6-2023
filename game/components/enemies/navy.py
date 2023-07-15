import pygame
from game.components.enemies.enemi_white import EnemyW 
from game.utils.constants import ENEMY_2


class Navy(EnemyW):
    WIDTH = 40
    HEIGHT = 60
    #SPEED_X = 15
    #SPEED_Y = 5
    

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
