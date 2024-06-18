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

# Initialize the current piece
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
            if event.key in KEY_STATES:
                KEY_STATES[event.key] = True
            elif event.key == pygame.K_UP:
                rotate_piece(current_piece)
        elif event.type == pygame.KEYUP:
            if event.key in KEY_STATES:
                KEY_STATES[event.key] = False

    # Continuous movement handling
    for key, pressed in KEY_STATES.items():
        if pressed:
            if key == pygame.K_UP:  
                rotate_piece(current_piece) # Rotation is not continuous
            else:
                if current_time - MOVE_TIMERS.get(key, 0) > MOVE_DELAY:
                    if key == pygame.K_DOWN:
                        move_piece_down(current_piece)
                    elif key == pygame.K_LEFT:
                        move_piece_left(current_piece)
                    elif key == pygame.K_RIGHT:
                        move_piece_right(current_piece)
                    MOVE_TIMERS[key] = current_time

    # Automatic piece movement down
    if current_time - last_move_time > move_interval:
        move_piece_down(current_piece)
        last_move_time = current_time

    # Fill the background, game logic, and update display
    screen.fill(SCREEN_BG)
    draw_grid_2(screen)
    draw_piece(screen, current_piece)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FRAME_RATE)

pygame.quit()
sys.exit()