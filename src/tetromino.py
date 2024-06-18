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
    current_piece['position'][0] += 1

def move_piece_left(current_piece):
    """Move the current piece left by one column."""
    current_piece['position'][1] -= 1

def move_piece_right(current_piece):
    """Move the current piece right by one column."""
    current_piece['position'][1] += 1