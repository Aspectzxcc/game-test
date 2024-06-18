import pygame
import sys
from src.settings import *
from src.screen import *
from src.tetromino import *

# Initialize Pygame
pygame.init()
    
# Create screen
screen = init_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

# Main game loop
clock = pygame.time.Clock()
running = True

current_piece = get_new_piece()

# Initialize the timer for moving the piece down
last_move_time = pygame.time.get_ticks()
move_interval = 1000  # Move the piece down every 1000 milliseconds (1 second)

while running:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                current_piece['position'][0] += 1  # Move down
            elif event.key == pygame.K_UP:
                # Typically used for piece rotation
                pass  # Replace with rotation logic if applicable
            elif event.key == pygame.K_LEFT:
                current_piece['position'][1] -= 1  # Move left
            elif event.key == pygame.K_RIGHT:
                current_piece['position'][1] += 1  # Move right

    # Check if it's time to move the piece down automatically
    if current_time - last_move_time > move_interval:
        current_piece['position'][0] += 1  # Move the piece down
        last_move_time = current_time  # Reset the last move time

    # Fill the background
    screen.fill(SCREEN_BG)

    # Game logic goes here
    draw_grid_2(screen)
    draw_piece(screen, current_piece)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FRAME_RATE)

pygame.quit()
sys.exit()

pygame.quit()
sys.exit()