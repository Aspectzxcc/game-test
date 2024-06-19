import random
from src.settings import *
from src.utils.collision import *

def get_new_piece():
    """Select a new piece and its initial position and color."""
    shape_key = 'I'
    initial_position = [0, GRID_OPTIONS['columns'] // 2 - 2]
    color = TETROMINOS[shape_key]['color']
    return {
        'shape': shape_key,
        'position': initial_position,
        'color': color
    }
    
def get_occupied_positions(piece):
    """Get a list of grid positions occupied by the given piece."""
    positions = []
    shape = TETROMINOS[piece['shape']]['shape']
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                x = piece['position'][0] + i
                y = piece['position'][1] + j
                positions.append((x, y))
    return positions

def lock_piece(current_piece):
    """Lock the piece into the grid and check for line clears."""
    for x, y in get_occupied_positions(current_piece):
        GAME_GRID[x][y] = current_piece['color']
    # clear_lines(GAME_GRID)
    # if check_game_over(get_new_piece(), GAME_GRID):
        # Handle game over scenario
    
def move_piece_down(current_piece):
    """Move the current piece down by one row or lock it if it can't move. Return a boolean indicating if the piece was locked."""
    next_position = (current_piece['position'][0] + 1, current_piece['position'][1])
    if check_piece_collision(current_piece, next_position):
        lock_piece(current_piece)  # Locks the piece and integrates it into the grid
        return True  # Return True for collision indicating the piece was locked
    else:
        current_piece['position'][0] += 1
        return False  # Return False since there was no collision and the piece was not locked

def move_piece_left(current_piece):
    """Move the current piece left by one column."""
    if check_piece_collision(current_piece, (current_piece['position'][0], current_piece['position'][1] - 1)):
        return
    current_piece['position'][1] -= 1

def move_piece_right(current_piece):
    """Move the current piece right by one column."""
    if check_piece_collision(current_piece, (current_piece['position'][0], current_piece['position'][1] + 1)):
        return # Don't move if there's a collision
    current_piece['position'][1] += 1
    
def rotate_piece(current_piece):
    """Rotate the current piece 90 degrees clockwise, adjusting its position in case of collision."""
    original_position = current_piece['position'][:]
    shape_matrix = TETROMINOS[current_piece['shape']]['shape']
    
    transposed_matrix = [list(row) for row in zip(*shape_matrix)]
    rotated_matrix = [row[::-1] for row in transposed_matrix]
    
    # Temporarily update the shape in the current_piece dictionary to check for collisions
    current_piece['shape_matrix'] = rotated_matrix  # Temporarily store the rotated shape for collision checks
    
    # Use calculate_shift_directions to dynamically generate shift directions
    shift_directions = calculate_shift_directions(rotated_matrix)
    
    for dx, dy in shift_directions:
        # Reset position to original before each shift attempt
        current_piece['position'] = [original_position[0] + dx, original_position[1] + dy]
        if not check_rotation_collision(current_piece):
            # If no collision, rotation and position adjustment is successful
            # Update the shape in TETROMINOS to the rotated shape
            TETROMINOS[current_piece['shape']]['shape'] = rotated_matrix
            return
    
    # Revert to the original shape and position if all shifts result in collision
    current_piece['position'] = original_position