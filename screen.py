import pygame

def init_screen(screen_width, screen_height):
    # Create window
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Game-Test: A Pygame Tetris Clone')
    
    return screen

def draw_grid(screen, grid_options):
    # Calculate the total width and height of the grid
    grid_width = grid_options['columns'] * grid_options['cell_size']
    grid_height = grid_options['rows'] * grid_options['cell_size']
    
    # Create a rectangle for the entire grid
    grid_rect = pygame.Rect(grid_options['origin'][0], grid_options['origin'][1], grid_width, grid_height)
    
    # Draw the rectangle
    pygame.draw.rect(screen, grid_options['color'], grid_rect, 5)  # Drawing the grid with border thickness 1 pixel