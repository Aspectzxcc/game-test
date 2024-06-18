import pygame
from src.settings import *

def init_screen(screen_width, screen_height):
    # Create window
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Game-Test: A Pygame Tetris Clone')
    
    return screen

# draw grid without cell borders
def draw_grid(screen):
    # Calculate the total width and height of the grid
    grid_width = GRID_OPTIONS['columns'] * GRID_OPTIONS['cell_size']
    grid_height = GRID_OPTIONS['rows'] * GRID_OPTIONS['cell_size']
    
    # Create a rectangle for the entire grid
    grid_rect = pygame.Rect(GRID_OPTIONS['origin'][0], GRID_OPTIONS['origin'][1], grid_width, grid_height)
    
    # Draw the rectangle
    pygame.draw.rect(screen, GRID_OPTIONS['color'], grid_rect, 5)  # Drawing the grid with border thickness 1 pixel
    
# draw grid with cell borders
def draw_grid_2(screen):
    cell_size = GRID_OPTIONS['cell_size']
    columns = GRID_OPTIONS['columns']
    rows = GRID_OPTIONS['rows']
    origin_x, origin_y = GRID_OPTIONS['origin']

    for row in range(rows):
        for col in range(columns):
            cell_x = origin_x + col * cell_size
            cell_y = origin_y + row * cell_size
            pygame.draw.rect(screen, GRID_OPTIONS['color'], pygame.Rect(cell_x, cell_y, cell_size, cell_size), 1)
    
def draw_piece(screen, piece):
    shape = TETRONIMOS[piece['shape']]['shape']
    color = piece['color']
    position = piece['position']
    cell_size = GRID_OPTIONS['cell_size']
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, color, pygame.Rect(
                    (position[1] + x) * cell_size + GRID_OPTIONS['origin'][0],
                    (position[0] + y) * cell_size + GRID_OPTIONS['origin'][1],
                    cell_size, cell_size))
    