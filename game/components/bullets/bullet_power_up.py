import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import HEART


class BulletPower(Bullet):
    WIDTH = 24
    HEIGHT = 90
    SPEED = 30

    def __init__(self, center):
        self.image = HEART
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center)

    def update(self, enemy):
        if self.rect.bottom < 0:
            self.is_visible = False
        self.rect.y -= self.SPEED
        super().update(enemy)
