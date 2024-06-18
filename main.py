import pygame
import sys
from init_screen import init_screen, draw_grid  # Import the init_screen function

# Initialize screen
screen = init_screen()

# Game Variables
frame_rate = 30
colors = {
    'background': (10, 10, 10),  # Dark background
    'tetrominoes': [(0, 255, 255), (255, 165, 0), (0, 0, 255), (255, 255, 0), (128, 0, 128), (0, 128, 0), (255, 0, 0)],  # Cyan, Orange, Blue, Yellow, Purple, Green, Red
}

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(colors['background'])

    # Game logic goes here
    draw_grid(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(frame_rate)

pygame.quit()
sys.exit()