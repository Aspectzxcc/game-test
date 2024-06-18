import random

# Tetromino Variables
tetromino_shapes = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1],
          [1, 1]],
    'T': [[0, 1, 0],
          [1, 1, 1]],
    'S': [[0, 1, 1],
          [1, 1, 0]],
    'Z': [[1, 1, 0],
          [0, 1, 1]],
    'J': [[1, 0, 0],
          [1, 1, 1]],
    'L': [[0, 0, 1],
          [1, 1, 1]]
}
tetromino_colors = {
    'I': (0, 255, 255),  # Cyan
    'O': (255, 165, 0),  # Orange
    'T': (0, 0, 255),  # Blue
    'S': (255, 255, 0),  # Yellow
    'Z': (128, 0, 128),  # Purple
    'J': (0, 128, 0),  # Green
    'L': (255, 0, 0)  # Red
}

def get_new_piece():
    """Select a new piece and its initial position and color."""
    shape_key = random.choice(list(tetromino_shapes.keys()))
    initial_position = [0, grid_options['columns'] // 2 - len(tetromino_shapes[shape_key][0]) // 2]
    color = tetromino_colors[shape_key]
    return {
        'shape': shape_key,
        'position': initial_position,
        'color': color
    }