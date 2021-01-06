import pygame
import random
from SARPGaS.Player.player import Player
from SARPGaS.Game.constance import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK, WHITE, BLUE, RED, GREEN
from SARPGaS.Game.projectile import Projectile

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SARPGaS")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


def ControllerTick():
    # Handle Input Events
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == pygame.KEYDOWN:
            # Was it the Space bar key? Shot a projectile.
            if event.key == pygame.K_SPACE:
                projectile = Projectile(player.rect.x, player.rect.y, player.facing)
                all_sprites.add(projectile)
                projectiles.add(projectile)
        # check for closing window
        elif event.type == pygame.QUIT:
            return False
    return True


def ViewTick(pressed_keys):
    # Draw Everything
    # Update
    player.update(pressed_keys)
    projectiles.update()
    # Draw / render
    screen.fill(BLACK)

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # *after* drawing everything, flip the display
    pygame.display.flip()


def Main():
    # Game loop
    running = True
    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()

        # Process input (event)
        if not ControllerTick():
            break

        ViewTick(pressed_keys)

    pygame.quit()


Main()
