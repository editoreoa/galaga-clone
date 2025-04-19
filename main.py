import pygame
import sys

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Init
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Galaga Clone")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    clock.tick(FPS)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logic update here

    # Draw
    screen.fill((0, 0, 0))  # Black background

    # Drawing code here

    pygame.display.flip()

pygame.quit()
sys.exit()
