import pygame

# Screen dimensions
screen_width = 800
screen_height = 600

# Define Grid Size
grid_rows = 20 # Number of rows
grid_columns = 10 # Number of columns
cell_size = 25  # Size of each cell in pixels
grid_origin = (70, 50)  # Move grid X and Y pixels from the top left corner of the screen
grid_border_thickness = 5

# Define colors
grid_color = (50, 50, 50)  # Color for the grid lines or cells

def init_screen():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Game-Test: A Pygame Tetris Clone')

    return screen

def draw_grid(screen):
    # Calculate the total width and height of the grid
    grid_width = grid_columns * cell_size
    grid_height = grid_rows * cell_size
    
    # Create a rectangle for the entire grid
    grid_rect = pygame.Rect(grid_origin[0], grid_origin[1], grid_width, grid_height)
    
    # Draw the rectangle
    pygame.draw.rect(screen, grid_color, grid_rect, grid_border_thickness)  # Drawing the grid with border thickness 1 pixel