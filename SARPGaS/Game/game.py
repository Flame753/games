import pygame
import random
from SARPGaS.Player.player import Player
from SARPGaS.Game.constance import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK, WHITE, BLUE, RED, GREEN

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SARPGaS")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


def ControllerTick():
    # Handle Input Events
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            return False
    return True


def ViewTick(pressed_keys):
    # Draw Everything
    # Update
    # Update the player sprite based on user keypresses
    player.update(pressed_keys)
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
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
