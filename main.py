import pygame
import sys
from src.settings import *
from src.screen import *
from src.game_logic import *

# Initialize Pygame
pygame.init()
    
# Create screen
screen = init_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

# Main game loop
clock = pygame.time.Clock()

# game variables
running = True 
game_over = False
current_piece = get_new_piece()
piece_locked = False
last_move_time =  pygame.time.get_ticks()
move_interval = MOVE_INTERVAL

def reset_game():
    global GAME_GRID, game_over, current_piece, MOVE_TIMERS, last_move_time, piece_locked
    # Reset the game grid to its initial state
    GAME_GRID = [[0 for _ in range(GRID_OPTIONS['columns'])] for _ in range(GRID_OPTIONS['rows'])]
    
    # Reset game state variables
    game_over = False
    piece_locked = False
    
    # Reset or reinitialize the current piece and next pieces queue
    current_piece = get_new_piece()
    
    # Reset movement timers
    MOVE_TIMERS = {pygame.K_LEFT: 0, pygame.K_RIGHT: 0, pygame.K_DOWN: 0}
    
    # Reset the last move time to the current time
    last_move_time = pygame.time.get_ticks()
    
    # Additional resets as needed based on game logic
    

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
            game_over = lock_piece(current_piece)  # lock_piece now returns True if game over
            print(game_over)
            if game_over:
                should_continue = display_game_over_screen(screen)
                if should_continue:
                    reset_game()
                else:
                    running = False 
            current_piece = get_new_piece()
            piece_locked = False
        last_move_time = current_time

    # Fill the background, game logic, and update display
    screen.fill(SCREEN_BG)
    render_grid(screen, GAME_GRID)
    draw_piece(screen, current_piece)
        
    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FRAME_RATE)

pygame.quit()
sys.exit()