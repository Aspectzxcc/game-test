import pygame
import sys
from settings import *
from screen import *

# Initialize Pygame
pygame.init()
    
# Create screen
screen = init_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(SCREEN_BG)

    # Game logic goes here
    draw_grid(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FRAME_RATE)

pygame.quit()
sys.exit()