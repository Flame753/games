import pygame
import random
from SARPGaS.Game.constance import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK, WHITE, BLUE, RED, GREEN
from SARPGaS.Charactor.creatures import Spider
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)


class Player(pygame.sprite.Sprite, Spider):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((50, 50))
        self.surf.fill(GREEN)
        self.rect = self.surf.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.facing = None

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            self.facing = "top"
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            self.facing = "bottom"
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
            self.facing = "left"
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            self.facing = "right"

        # Keep player on thee screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
