import random
from settings import *

def get_new_piece():
    """Select a new piece and its initial position and color."""
    shape_key = random.choice(list(TETRONIMOS.keys()))
    initial_position = [0, 4]
    color = TETRONIMOS[shape_key]['color']
    return {
        'shape': shape_key,
        'position': initial_position,
        'color': color
    }