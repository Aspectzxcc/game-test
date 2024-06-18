def rotate_shape(shape):
    """Rotate the shape (a matrix) clockwise."""
    return [list(row) for row in zip(*shape[::-1])]