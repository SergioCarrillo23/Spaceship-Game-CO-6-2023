import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT  

class Spaceship:
    WIDTH = 40
    HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect  = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS 
        self.is_alive = True
    
    def update(self, game_speed, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left(game_speed)

        if user_input[pygame.K_RIGHT]:
            self.move_right(game_speed)

        if user_input[pygame.K_UP]:
            self.move_up(game_speed)

        if user_input[pygame.K_DOWN]:
            self.move_down(game_speed)

        if user_input[pygame.K_LEFT] and user_input[pygame.K_UP]:
            self.move_left_up(game_speed)
        
        if user_input[pygame.K_LEFT] and user_input[pygame.K_DOWN]:
            self.move_left_down(game_speed)

        if user_input[pygame.K_RIGHT] and user_input[pygame.K_UP]:
            self.move_right_up(game_speed)

        if user_input[pygame.K_RIGHT] and user_input[pygame.K_DOWN]:
            self.move_right_down(game_speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self, game_speed):
        if self.rect.left > 0:
            self.rect.x -= game_speed
        else:
            self.rect.right = SCREEN_WIDTH

    def move_right(self, game_speed):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += game_speed
        else:
            self.rect.left = 0 

    def move_up(self, game_speed):
        if self.rect.top > SCREEN_HEIGHT // 2: 
            self.rect.y -= game_speed 
        #else: 
        #    self.rect.bottom = SCREEN_HEIGHT

    def move_down(self, game_speed):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += game_speed
        #else: 
        #    self.rect.top = SCREEN_HEIGHT // 2
        
    def move_left_up(self, game_speed):
        if self.rect.left > 0 and self.rect.top > SCREEN_HEIGHT // 2:
            self.rect.x -= game_speed
            self.rect.y -= game_speed
        #else:
        #    self.rect.top = SCREEN_WIDTH
        #    self.rect.bottom = SCREEN_HEIGHT

    def move_left_down(self, game_speed):
        if self.rect.left > 0 and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.x -= game_speed
            self.rect.y += game_speed
        #else:
        #    self.rect.right = SCREEN_WIDTH
        #    self.rect.top = SCREEN_HEIGHT // 2 

    def move_right_up(self, game_speed):
        if self.rect.right < SCREEN_WIDTH and self.rect.top > SCREEN_HEIGHT // 2:
            self.rect.x += game_speed
            self.rect.y -= game_speed
        #else:
        #    self.rect.left = 0
        #    self.rect.bottom = SCREEN_HEIGHT

    def move_right_down(self, game_speed):
        if self.rect.right < SCREEN_WIDTH and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.x += game_speed
            self.rect.y += game_speed
        #else:
        #    self.rect.left = 0
        #    self.rect.top = SCREEN_HEIGHT // 2