import pygame
import pickle

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE, BG_IMAGE, BG_IMAGE2, GAME, BG_IMAGE3
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components.power_ups.power_up_handler import PowerUpHandler
from game.utils import text_utils

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.bullet_hundler = BulletHandler()
        self.power_up_handler = PowerUpHandler()
        self.score = 0
        self.number_deaths = 0
        self.high_score = self.load_high_score() # Cargar el puntaje más alto almacenado

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                self.reset()
                self.playing = True

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(self.game_speed, user_input, self.bullet_hundler)
            self.enemy_handler.update(self.bullet_hundler)
            self.bullet_hundler.update(self.player, self.enemy_handler.enemies)
            self.power_up_handler.update(self.player)
            self.score = self.enemy_handler.enemies_destroyed
            if not self.player.is_alive:
                pygame.time.delay(300)
                self.playing = False
                self.number_deaths += 1
                self.update_high_score()  # Actualizar el puntaje más alto almacenado

    def draw(self):
        self.draw_background()
        if self.playing:
            self.draw_planet()
            self.draw_satur()
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_hundler.draw(self.screen)
            self.power_up_handler.draw(self.screen)
            self.draw_score()
        else:
            self.draw_background_meteoro()
            self.draw_title()
            self.draw_menu()
            self.draw_high_score()
            self.game_over()
        pygame.display.update()
        pygame.display.flip()
    
    def draw_satur(self):
        image = pygame.transform.scale(BG_IMAGE2, (SCREEN_WIDTH - 700, SCREEN_HEIGHT - 300))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg+700, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.y_pos_bg = 0
        elif self.y_pos_bg < 0:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg + image_height))
            self.y_pos_bg += self.game_speed

    def draw_planet(self):
        image = pygame.transform.scale(BG_IMAGE, (SCREEN_WIDTH - 700, SCREEN_HEIGHT- 300))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.y_pos_bg = 0
        elif self.y_pos_bg < 0:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg + image_height))
            self.y_pos_bg += self.game_speed  

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_background_meteoro(self):
        if self.number_deaths == 0:
            image = pygame.transform.scale(BG_IMAGE3, (SCREEN_WIDTH, SCREEN_HEIGHT))
            image_height = image.get_height()
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            if self.y_pos_bg >= SCREEN_HEIGHT:
                self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
                self.y_pos_bg = 0
            self.y_pos_bg += (self.game_speed - 13)

    def game_over(self):
        if self.number_deaths > 0:
            image = pygame.transform.scale(GAME, (SCREEN_WIDTH, SCREEN_HEIGHT-500))
            image_height = image.get_height()
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            if self.y_pos_bg >= SCREEN_HEIGHT:
                self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
                self.y_pos_bg = 0
            self.y_pos_bg += (self.game_speed - 15)

    def draw_title(self):
        if self.number_deaths == 0:
            text, text_rect = text_utils.get_message("GALAXIA GAME ", 50, WHITE, SCREEN_WIDTH // 2, 50)
            self.screen.blit(text, text_rect)
            
            line1 = "Instruction: "
            line1_text, line1_rect = text_utils.get_message(line1, 25, WHITE, 100, 180)
            self.screen.blit(line1_text, line1_rect)

            line2 = "The movement the ship is by pressing the Keys: ARROWS"
            line2_text, line2_rect = text_utils.get_message(line2, 20, WHITE, 310, 230)
            self.screen.blit(line2_text, line2_rect)

            line3 = "To shoot is whit key: SPACE"
            line3_text, line3_rect = text_utils.get_message(line3, 20, WHITE, 161, 280)
            self.screen.blit(line3_text, line3_rect)
        
    def draw_menu(self):
        if self.number_deaths == 0:
            text, text_rect = text_utils.get_message("Press any Key to start", 30, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = text_utils.get_message("Press any key to Restart", 30, WHITE)
            score, score_reset = text_utils.get_message(f'Your score is: {self.score}', 30, WHITE, height=SCREEN_HEIGHT//2+50)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_reset)

    def draw_score(self):
        score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 20, WHITE, 1000, 40)
        self.screen.blit(score, score_rect)

    def draw_high_score(self):
        if self.number_deaths > 0:
            high_score_text, high_score_rect = text_utils.get_message("High Score: " + str(self.high_score), 30, WHITE, SCREEN_WIDTH // 2, 200)
            self.screen.blit(high_score_text, high_score_rect)

    def load_high_score(self):
        try:
            with open("high_score.pkl", "rb") as file:
                high_score = pickle.load(file)
        except FileNotFoundError:
            high_score = 0
        return high_score

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.pkl", "wb") as file:
                pickle.dump(self.high_score, file)

    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_hundler.reset()
        self.score = 0
        self.high_score = self.load_high_score()  # Cargar el puntaje más alto almacenado
        self.power_up_handler.reset()
