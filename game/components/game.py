import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, BG_IMAGE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.enemies.white_handler import WhiteHandler

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.white_handler = WhiteHandler()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(self.game_speed, user_input)
        self.enemy_handler.update()
        self.white_handler.update()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.back_image()
        self.draw_background()
        self.player.draw(self.screen)
        self.white_handler.draw(self.screen)
        self.enemy_handler.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

  
    def back_image(self):                 
        image = pygame.transform.scale(BG_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_width = image.get_width()
        image_height = image.get_height()

        x_pos_image = 0  # Ajusta la posición X deseada
        y_pos_image = 0  # Ajusta la posición Y deseada

        scale = 1.0
        scale_factor = 0.01
        running = True
        while running:
            #self.screen.fill((255, 255, 255))  # Limpia la pantalla en cada iteración
            scaled_image = pygame.transform.scale(image, (int(image_width * scale), int(image_height * scale)))
            image_rect = scaled_image.get_rect(center=(x_pos_image, y_pos_image))
            self.screen.blit(scaled_image, image_rect)
            break
            scale += scale_factor
            if scale >= 2.0 or scale <= 0.5:
                scale_factor *= -1

            pygame.display.update()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            break