import pygame

pygame.init()
import random

# Screen size
WIDTH = 800
HEIGHT = 600

# Tetromino shapeslaunch

SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 0], [1, 1], [0, 1]],
    [[0, 1], [1, 1], [1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
]

# Tetromino colors
COLORS = [
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
    (255, 165, 0),  # Orange
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (255, 0, 0),    # Red
]

def draw_grid(surface, grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            pygame.draw.rect(                                         
                surface,
                COLORS[grid[y][x]],
                (x * 30, y * 30, 30, 30),
                0
            )
            pygame.draw.rect(
                surface,
                (50, 50, 50),
                (x * 30, y * 30, 30, 30),
                1
            )

def check_collision(tetromino, grid, offset):
    for y in range(len(tetromino)):
        for x in range(len(tetromino[y])):
            if (
                tetromino[y][x] and
                (offset[1] + y >= len(grid) or
                 offset[0] + x < 0 or
                 offset[0] + x >= len(grid[y]) or
                 grid[offset[1] + y][offset[0] + x] != -1)
            ):
                return True
    return False 