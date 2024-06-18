import pygame
import sys
from screen import init_screen

# Initialize Pygame
pygame.init()

# Screen variables
screen_width = 800 # Screen X width
screen_height = 600 # Screen Y height
    
# Create screen
screen = init_screen(screen_width, screen_height)

# Define Grid Size
grid_rows = 20 # Number of rows
grid_columns = 10 # Number of columns
cell_size = 25  # Size of each cell in pixels
grid_origin = (70, 50)  # Move grid X and Y pixels from the top left corner of the screen
game_grid = [[0 for _ in range(grid_columns)] for _ in range(grid_rows)]

# Define colors
grid_color = (50, 50, 50)  # Color for the grid lines or cells

def draw_grid(screen):
    # Calculate the total width and height of the grid
    grid_width = grid_columns * cell_size
    grid_height = grid_rows * cell_size
    
    # Create a rectangle for the entire grid
    grid_rect = pygame.Rect(grid_origin[0], grid_origin[1], grid_width, grid_height)
    
    # Draw the rectangle
    pygame.draw.rect(screen, grid_color, grid_rect, 5)  # Drawing the grid with border thickness 1 pixel
    
# Tetromino Shapes
tetromino_shapes = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1],
          [1, 1]],
    'T': [[0, 1, 0],
          [1, 1, 1]],
    'S': [[0, 1, 1],
          [1, 1, 0]],
    'Z': [[1, 1, 0],
          [0, 1, 1]],
    'J': [[1, 0, 0],
          [1, 1, 1]],
    'L': [[0, 0, 1],
          [1, 1, 1]]
}

tetromino_colors = {
    'I': (0, 255, 255),  # Cyan
    'O': (255, 165, 0),  # Orange
    'T': (0, 0, 255),  # Blue
    'S': (255, 255, 0),  # Yellow
    'Z': (128, 0, 128),  # Purple
    'J': (0, 128, 0),  # Green
    'L': (255, 0, 0)  # Red

}

def rotate_shape(shape):
    """Rotate the shape (a matrix) clockwise."""
    return [list(row) for row in zip(*shape[::-1])]

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
    draw_grid(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(frame_rate)

pygame.quit()
sys.exit()