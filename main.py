import pygame
import sys
from settings import *
from screen import init_screen, draw_grid

# Initialize Pygame
pygame.init()
    
# Create screen
screen = init_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

# Create the game grid
game_grid = [[0 for _ in range(GRID_OPTIONS['columns'])] for _ in range(GRID_OPTIONS['rows'])]

clock = pygame.time.Clock()
running = True

# Main game loop
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