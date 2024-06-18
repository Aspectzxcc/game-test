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
move_interval = MOVE_INTERVAL

while running:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                move_piece_down(current_piece)  # Move the piece down
            elif event.key == pygame.K_UP:
                rotate_piece(current_piece)  # Rotate the piece
                pass 
            elif event.key == pygame.K_LEFT:
                move_piece_left(current_piece)  # Move left
            elif event.key == pygame.K_RIGHT:
                move_piece_right(current_piece) # Move right

    # Check if it's time to move the piece down automatically
    if current_time - last_move_time > move_interval:
        move_piece_down(current_piece)  # Move the piece down
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