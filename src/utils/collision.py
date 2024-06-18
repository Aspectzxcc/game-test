from src.settings import TETROMINOS, GAME_GRID

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
    
def check_piece_collision(current_piece, next_position):
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
                if grid_row >= len(GAME_GRID) or grid_col < 0 or grid_col >= len(GAME_GRID[0]):
                    return True  # Collision with boundary
                
                # Block collision check
                if GAME_GRID[grid_row][grid_col]:
                    return True  # Collision with another block
    
    return False  # No collision detected

def check_rotation_collision(current_piece, rotation=1):
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
                if grid_row >= len(GAME_GRID) or grid_col < 0 or grid_col >= len(GAME_GRID[0]):
                    return True  # Collision with boundary
                
                # Check if the position is outside the grid's vertical bounds
                if grid_row < 0:
                    continue  # Skip this iteration, as it's above the grid
                
                # Block collision check
                if GAME_GRID[grid_row][grid_col]:
                    return True  # Collision with another block
    
    return False  # No collision detected