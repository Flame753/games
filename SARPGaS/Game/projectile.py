import pygame
from SARPGaS.Game.constance import SCREEN_WIDTH, SCREEN_HEIGHT, RED


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, facing):
        super().__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect()
        self.rect.center = (x, y)
        self.player_facing = facing
        self.speed = 7

    def update(self):
        if self.player_facing == "top":
            self.rect.move_ip(0, -1 * self.speed)
        elif self.player_facing == "bottom":
            self.rect.move_ip(0, self.speed)
        elif self.player_facing == "right":
            self.rect.move_ip(self.speed, 0)
        else:
            self.rect.move_ip(-1 * self.speed, 0)

        if (self.rect.left > SCREEN_WIDTH) or (self.rect.right < 0) or (self.rect.top >= SCREEN_HEIGHT) or (self.rect.bottom <= 0):
            self.kill()

