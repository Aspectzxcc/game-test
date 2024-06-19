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
piece_locked = False

# Initialize the timer for moving the piece down
last_move_time = pygame.time.get_ticks()
move_interval = MOVE_INTERVAL

def reset_game():
    global current_piece, last_move_time, piece_locked, move_interval, running, screen, GAME_GRID

    # Reinitialize game state variables
    current_piece = get_new_piece()  # Reset the current piece
    last_move_time = 0  # Reset the last move time
    piece_locked = False  # Reset the piece locked state
    move_interval = MOVE_INTERVAL  # Reset the move interval to its initial value from settings

    # Clear the game grid
    reset_settings()

    # Reset the running state to True to restart the game loop
    running = True

while running:
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in KEY_STATES and not piece_locked:  # Prevent movement when piece is locked
                KEY_STATES[event.key] = True
            elif event.key == pygame.K_UP and not piece_locked:  # Prevent rotation when piece is locked
                rotate_piece(current_piece)
        elif event.type == pygame.KEYUP:
            if event.key in KEY_STATES:
                KEY_STATES[event.key] = False

    # Continuous movement handling
    for key, pressed in KEY_STATES.items():
        if pressed and not piece_locked:
            if key == pygame.K_UP:  
                rotate_piece(current_piece)  # Rotation is not continuous
            else:
                if current_time - MOVE_TIMERS.get(key, 0) > MOVE_DELAY:
                    if key == pygame.K_DOWN:
                        piece_locked = move_piece_down(current_piece)
                    elif key == pygame.K_LEFT:
                        move_piece_left(current_piece)
                    elif key == pygame.K_RIGHT:
                        move_piece_right(current_piece)
                    MOVE_TIMERS[key] = current_time
                    
    # Automatic piece movement down   
    elapsed_time = current_time - last_move_time
    
    if elapsed_time > move_interval:
        piece_locked = move_piece_down(current_piece)
        if piece_locked:
            lock_piece(current_piece)
            if check_game_over():
                if display_game_over_message(screen):
                    reset_game()
                else:
                    running = False  # Exit game loop
            current_piece = get_new_piece()
            piece_locked = False
        last_move_time = current_time

    # Fill the background, game logic, and update display
    screen.fill(SCREEN_BG)
    render_grid(screen)
    draw_piece(screen, current_piece)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FRAME_RATE)

pygame.quit()
sys.exit()