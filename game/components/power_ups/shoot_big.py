import math, pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SHIELD_HEART


class Shootbig(PowerUp):

    def __init__(self):
        self.image = SHIELD_HEART
        super().__init__(self.image)
        self.initial_x = self.rect.x
        self.amplitude = -250  # Rango del movimiento lateral
        self.frequency = 0.04  # Velocidad del movimiento lateral (ajusta este valor para cambiar la velocidad)
        self.time = 2
  
    def update(self, player):
        self.time += 1
        displacement = self.amplitude * math.cos(2 * math.pi * self.frequency * self.time)
        self.rect.x = self.initial_x + displacement
        self.rect.y += self.SPEED
        if self.rect.colliderect(player.rect):
            self.is_visible = False
            self.is_used = True
            self.time_up = pygame.time.get_ticks() + self.DURATION