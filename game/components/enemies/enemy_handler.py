from game.components.enemies.ship import Ship
from game.components.enemies.navy import Navy
from game.components.enemies.ovni import Ovni
from game.components.enemies.enemy_end import Astro

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.enemies_destroyed = 0 

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_visible or not enemy.is_alive:
                self.remove_enemy(enemy)
            if not enemy.is_alive:
                self.enemies_destroyed += 1

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 3:
           self.enemies.append(Ship())
        if len(self.enemies) < 5:
            self.enemies.append(Navy())
        if len(self.enemies) < 8:
            self.enemies.append(Ovni())
        if len(self.enemies) < 11:
            self.enemies.append(Astro())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def reset(self):
        self.enemies = []
        self.enemies_destroyed = 0