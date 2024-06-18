# Screen variables
SCREEN_WIDTH = 800 # Screen X width
SCREEN_HEIGHT = 600 # Screen Y height

# FPS 
FRAME_RATE = 20

# Grid variables
GRID_OPTIONS = {
    'rows': 20,  # Number of rows
    'columns': 10,  # Number of columns
    'cell_size': 27,  # Size of each cell in pixels
    'origin': (70, 50),  # Move grid X and Y pixels from the top left corner of the screen
    'color': (50, 50, 50)  # Color for the grid lines or cells
}

# Actual game grid data
GAME_GRID = [[0 for _ in range(GRID_OPTIONS['columns'])] for _ in range(GRID_OPTIONS['rows'])]

# colors
SCREEN_BG = (10, 10, 10)  # Dark Background color
CYAN = (0, 255, 255)  # I tetromino
ORANGE = (255, 165, 0)  # O tetromino
BLUE = (0, 0, 255)  # T tetromino
YELLOW = (255, 255, 0)  # S tetromino
PURPLE = (128, 0, 128)  # Z tetromino
GREEN = (0, 128, 0)  # J tetromino
RED = (255, 0, 0)  # L tetromino

TETROMINOS = {
    'I': {'shape': [[1, 1, 1, 1]], 'color': CYAN},
    'O': {'shape': 
         [[1, 1],
          [1, 1]], 'color': ORANGE},    
    'T': {'shape': 
         [[0, 1, 0],
          [1, 1, 1]], 'color': BLUE},
    'S': {'shape': 
         [[0, 1, 1],
          [1, 1, 0]], 'color': YELLOW}, 
    'Z': {'shape': 
         [[1, 1, 0],
          [0, 1, 1]], 'color': PURPLE},
    'J': {'shape': 
         [[1, 0, 0],
          [1, 1, 1]], 'color': GREEN},
    'L': {'shape': 
         [[0, 0, 1],
          [1, 1, 1]], 'color': RED}
}