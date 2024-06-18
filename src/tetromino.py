import random
from src.settings import *

def get_new_piece():
    """Select a new piece and its initial position and color."""
    shape_key = random.choice(list(TETRONIMOS.keys()))
    initial_position = [0, GRID_OPTIONS['columns'] // 2 - 2]
    color = TETRONIMOS[shape_key]['color']
    return {
        'shape': shape_key,
        'position': initial_position,
        'color': color
    }