import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_SHIP, SPACESHIP_SHIELD, SHIELD_HEART, BULLET, HEART
from game.components.power_ups.shield import Shield
from game.components.power_ups.shoot_big import Shootbig

class Spaceship:
    WIDTH = 40
    HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500
    
    
    def __init__(self):
        self.time_delay = 0
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect  = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS 
        self.is_alive = True
        self.has_shield = False
        self.time_up = 0 

    def update(self, game_speed, user_input, bullet_handler):

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

        if user_input[pygame.K_SPACE]:
            self.shoot(bullet_handler)
        
        if self.has_shield:
            time_to_show = round((self.time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show < 0:
                self.deactivate_powert_up()

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

    def shoot(self, bullet_handler):
            bullet_handler.add_bullet(BULLET_SHIP, self.rect.center)

    def activate_power_up(self, power_up):
        self.time_up = power_up.time_up
        if type(power_up) == Shield:
            self.image = SPACESHIP_SHIELD
            self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGHT))
            self.has_shield = True
       
    def activate_power_shoot(self, power_up, bullet_handler):
        self.time_up = power_up.time_up
        if type(power_up) == Shootbig:
            # Agregar la nueva bala al bullet_handler
            bullet_handler.add_bullet(HEART, self.rect.center)

    def deactivate_powert_up(self):
        self.has_shield = False
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))

    def reset(self):
        self.time_delay = 0
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect  = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS 
        self.is_alive = True
        self.has_shield = False