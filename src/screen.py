import pygame
from src.settings import *
import sys

def init_screen(screen_width, screen_height):
    # Create window
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Game-Test: A Pygame Tetris Clone')
    
    return screen

def render_grid(screen):
    draw_grid(screen)
    draw_grid_cells(screen)
    draw_grid_borders(screen)

def draw_grid(screen):
    for y, row in enumerate(GAME_GRID):
        for x, cell in enumerate(row):
            if cell:  # If the cell is not empty, draw it
                pygame.draw.rect(screen, cell, pygame.Rect(
                    x * GRID_OPTIONS['cell_size'] + GRID_OPTIONS['origin'][0],
                    y * GRID_OPTIONS['cell_size'] + GRID_OPTIONS['origin'][1],
                    GRID_OPTIONS['cell_size'], GRID_OPTIONS['cell_size']))
                
# draw grid cell borders
def draw_grid_cells(screen):
    cell_size = GRID_OPTIONS['cell_size']
    columns = GRID_OPTIONS['columns']
    rows = GRID_OPTIONS['rows']
    origin_x, origin_y = GRID_OPTIONS['origin']

    for row in range(rows):
        for col in range(columns):
            cell_x = origin_x + col * cell_size
            cell_y = origin_y + row * cell_size
            pygame.draw.rect(screen, GRID_OPTIONS['color'], pygame.Rect(cell_x, cell_y, cell_size, cell_size), 1)

# draw grid borders
def draw_grid_borders(screen):
    # Calculate the total width and height of the grid
    grid_width = GRID_OPTIONS['columns'] * GRID_OPTIONS['cell_size']
    grid_height = GRID_OPTIONS['rows'] * GRID_OPTIONS['cell_size']
    
    # Create a rectangle for the entire grid
    grid_rect = pygame.Rect(GRID_OPTIONS['origin'][0], GRID_OPTIONS['origin'][1], grid_width, grid_height)
    
    # Draw the rectangle
    pygame.draw.rect(screen, GRID_OPTIONS['color'], grid_rect, GRID_OPTIONS['border_thickness'])  # Drawing the grid with border thickness 1 pixel
    
def draw_piece(screen, piece):
    shape = TETROMINOS[piece['shape']]['shape']
    color = piece['color']
    position = piece['position']
    cell_size = GRID_OPTIONS['cell_size']
    border_thickness = GRID_OPTIONS['border_thickness']

    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                # Adjust position by adding border_thickness to account for the grid border
                pygame.draw.rect(screen, color, pygame.Rect(
                    (position[1] + x) * cell_size + GRID_OPTIONS['origin'][0] + border_thickness,
                    (position[0] + y) * cell_size + GRID_OPTIONS['origin'][1] + border_thickness,
                    cell_size - border_thickness*2,  # Subtract border_thickness*2 to maintain cell size inside borders
                    cell_size - border_thickness*2))
    
def display_game_over_screen(screen):
    # Set the game over message
    game_over_text = "Game Over"
    instructions_text = "Press any key to restart"

    # Set the font: You can adjust the font and size as needed
    font = pygame.font.Font(None, 74)
    instructions_font = pygame.font.Font(None, 36)

    # Render the text
    game_over_surface = font.render(game_over_text, True, (255, 0, 0))  # Red color
    instructions_surface = instructions_font.render(instructions_text, True, (255, 255, 255))  # White color

    # Get the text rectangle
    game_over_rect = game_over_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    instructions_rect = instructions_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))

    # Fill the screen with a black background
    screen.fill((0, 0, 0))

    # Draw the text on the screen
    screen.blit(game_over_surface, game_over_rect)
    screen.blit(instructions_surface, instructions_rect)

    # Update the display
    pygame.display.flip()

    # Wait for a key press to restart or exit
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                waiting_for_input = False
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()