import pygame
import sys

# Initialize Pygame
pygame.init()

# Game Variables
screen_width = 800 # Screen X width
screen_height = 600 # Screen Y height
frame_rate = 30 # FPS
colors = {
    'background': (10, 10, 10),  # Dark background
    'tetrominoes': [(0, 255, 255), (255, 165, 0), (0, 0, 255), (255, 255, 0), (128, 0, 128), (0, 128, 0), (255, 0, 0)],  # Cyan, Orange, Blue, Yellow, Purple, Green, Red
}

# Create window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game-Test: A Pygame Tetris Clone')

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

# Assign colors to shapes
tetromino_colors = {
    'I': colors['tetrominoes'][0],
    'O': colors['tetrominoes'][1],
    'T': colors['tetrominoes'][2],
    'S': colors['tetrominoes'][3],
    'Z': colors['tetrominoes'][4],
    'J': colors['tetrominoes'][5],
    'L': colors['tetrominoes'][6]
}

def rotate_shape(shape):
    """Rotate the shape (a matrix) clockwise."""
    return [list(row) for row in zip(*shape[::-1])]

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(colors['background'])

    # Game logic goes here
    draw_grid(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(frame_rate)

pygame.quit()
sys.exit()