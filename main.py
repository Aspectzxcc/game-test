import pygame
import sys
from screen import init_screen, draw_grid

# Initialize Pygame
pygame.init()

# Screen variables
screen_width = 800 # Screen X width
screen_height = 600 # Screen Y height
    
# Create screen
screen = init_screen(screen_width, screen_height)

# Define Grid Variables
grid_options = {
    'rows': 20,  # Number of rows
    'columns': 10,  # Number of columns
    'cell_size': 27,  # Size of each cell in pixels
    'origin': (70, 50),  # Move grid X and Y pixels from the top left corner of the screen
    'color': (50, 50, 50)  # Color for the grid lines or cells
}

# Create the game grid
game_grid = [[0 for _ in range(grid_options['columns'])] for _ in range(grid_options['rows'])]

# Game Variables
frame_rate = 30 # FPS
background_color = (10, 10, 10) # Dark background
clock = pygame.time.Clock()
running = True

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(background_color)

    # Game logic goes here
    draw_grid(screen, grid_options)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(frame_rate)

pygame.quit()
sys.exit()