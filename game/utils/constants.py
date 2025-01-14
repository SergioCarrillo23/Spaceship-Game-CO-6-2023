import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

BG_IMAGE = pygame.image.load(os.path.join(IMG_DIR, 'Other/jupiter.png'))

BG_IMAGE2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/saturnff.png'))

BG_IMAGE3 = pygame.image.load(os.path.join(IMG_DIR, "Other/lluvimeteoro2.png"))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Bullet/shoot_big.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
SHIELD_HEART = pygame.image.load(os.path.join(IMG_DIR, "Other/SmallHeart.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/navy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/ovni_1.png"))
ENEMY_4 = pygame.image.load(os.path.join(IMG_DIR, "Other/astro.png"))
GAME = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))

FONT_STYLE = 'freesansbold.ttf'

LEFT = 'left'
RIGHT = 'right'

BULLET_ENEMY_TYPE = "enemy"
BULLET_SHIP = "player"
WHITE = (255, 255, 255)
