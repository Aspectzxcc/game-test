import random
from src.settings import *

def get_new_piece():
    """Select a new piece and its initial position and color."""
    shape_key = random.choice(list(TETROMINOS.keys()))
    initial_position = [0, GRID_OPTIONS['columns'] // 2 - 2]
    color = TETROMINOS[shape_key]['color']
    return {
        'shape': shape_key,
        'position': initial_position,
        'color': color
    }
    
def move_piece_down(current_piece):
    """Move the current piece down by one row."""
    if check_piece_collision(current_piece, (current_piece['position'][0] + 1, current_piece['position'][1]), GAME_GRID):
        return
    current_piece['position'][0] += 1

def move_piece_left(current_piece):
    """Move the current piece left by one column."""
    if check_piece_collision(current_piece, (current_piece['position'][0], current_piece['position'][1] - 1), GAME_GRID):
        return
    current_piece['position'][1] -= 1

def move_piece_right(current_piece):
    """Move the current piece right by one column."""
    if check_piece_collision(current_piece, (current_piece['position'][0], current_piece['position'][1] + 1), GAME_GRID):
        return # Don't move if there's a collision
    current_piece['position'][1] += 1
    
def rotate_shape(shape_matrix):
    # Rotate the shape matrix 90 degrees clockwise
    transposed_matrix = [list(row) for row in zip(*shape_matrix)]
    return [row[::-1] for row in transposed_matrix]
    
def rotate_piece(current_piece):
    """Rotate the current piece 90 degrees clockwise, adjusting its position in case of collision."""
    original_position = current_piece['position'][:]
    shape_matrix = TETROMINOS[current_piece['shape']]['shape']
    
    rotated_matrix = rotate_shape(shape_matrix)
    
    # Temporarily update the shape in the current_piece dictionary to check for collisions
    current_piece['shape_matrix'] = rotated_matrix  # Temporarily store the rotated shape for collision checks
    
    # Use calculate_shift_directions to dynamically generate shift directions
    shift_directions = calculate_shift_directions(rotated_matrix)
    
    for dx, dy in shift_directions:
        # Reset position to original before each shift attempt
        current_piece['position'] = [original_position[0] + dx, original_position[1] + dy]
        if not check_rotation_collision(current_piece, GAME_GRID):
            # If no collision, rotation and position adjustment is successful
            # Update the shape in TETROMINOS to the rotated shape
            TETROMINOS[current_piece['shape']]['shape'] = rotated_matrix
            return
    
    # Revert to the original shape and position if all shifts result in collision
    current_piece['position'] = original_position
    
def calculate_shift_directions(shape_matrix):
    """
    Calculate possible shift directions based on the shape matrix dimensions.
    This function aims to dynamically generate shift directions to accommodate
    the unique rotation needs of different Tetris pieces, including the "I" piece,
    especially near the horizontal and bottom edges of the grid.
    """
    height = len(shape_matrix)
    width = len(shape_matrix[0]) if height > 0 else 0

    # Basic shifts for all pieces
    shift_directions = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]

    # Add more shifts for taller or wider pieces
    if width > 2:  # Assuming width > 2 needs special handling, like the "I" piece
        shift_directions += [(0, -2), (0, 2)]
    if height > 2:  # Assuming height > 2 might also need special handling
        shift_directions += [(-2, 0), (2, 0)]

    # Diagonal shifts for pieces that are both tall and wide
    if width > 2 and height > 2:
        shift_directions += [(-1, -1), (-1, 1), (1, -1), (1, 1), (-2, -2), (-2, 2), (2, -2), (2, 2)]

    # Additional shifts for "I" piece near the horizontal and bottom edges
    if width == 4 or height == 4:  # Specific to the "I" piece
        shift_directions += [(0, -3), (0, 3), (-1, -2), (-1, 2), (1, -2), (1, 2)]
        # Allow for more extreme shifts to avoid edge collisions
        if height == 4:  # Vertical "I" piece might need to shift more on the horizontal axis
            shift_directions += [(-3, 0), (3, 0)]

    return shift_directions
    
def check_piece_collision(current_piece, next_position, game_grid):
    """
    Check for collision.
    
    :param current_piece: The current piece.
    :param next_position: The next position of the piece (row, column).
    :param game_grid: The game grid as a 2D list.
    :return: True if collision is detected, False otherwise.
    """
    shape_matrix = TETROMINOS[current_piece['shape']]['shape']
    next_row, next_col = next_position
    
    for i, row in enumerate(shape_matrix):
        for j, block in enumerate(row):
            if block:  # If there's a part of the tetromino here
                # Calculate the absolute position on the grid
                grid_row = next_row + i
                grid_col = next_col + j
                
                # Boundary checks
                if grid_row >= len(game_grid) or grid_col < 0 or grid_col >= len(game_grid[0]):
                    return True  # Collision with boundary
                
                # Block collision check
                if game_grid[grid_row][grid_col]:
                    return True  # Collision with another block
    
    return False  # No collision detected

def check_rotation_collision(current_piece, game_grid, rotation=1):
    """
    Check for collision when rotating a piece.
    
    :param current_piece: The current piece.
    :param game_grid: The game grid as a 2D list.
    :param rotation: Number of 90-degree clockwise rotations.
    :return: True if collision is detected after rotation, False otherwise.
    """
    # Get the current shape matrix
    shape_matrix = TETROMINOS[current_piece['shape']]['shape']
    
    # Apply rotation to the shape matrix
    for _ in range(rotation % 4):  # Ensure rotation is within 0-3
        shape_matrix = [list(row) for row in zip(*shape_matrix[::-1])]
    
    # Get the current position
    current_row, current_col = current_piece['position']
    
    for i, row in enumerate(shape_matrix):
        for j, block in enumerate(row):
            if block:  # If there's a part of the tetromino here
                # Calculate the absolute position on the grid
                grid_row = current_row + i
                grid_col = current_col + j
                
                # Boundary checks
                if grid_row >= len(game_grid) or grid_col < 0 or grid_col >= len(game_grid[0]):
                    return True  # Collision with boundary
                
                # Check if the position is outside the grid's vertical bounds
                if grid_row < 0:
                    continue  # Skip this iteration, as it's above the grid
                
                # Block collision check
                if game_grid[grid_row][grid_col]:
                    return True  # Collision with another block
    
    return False  # No collision detected