from pyray import *


def draw_grid(rows, cols, block_size, margin_x, margin_y):
    for i in range(rows):
        for j in range(cols):
            y = i * block_size + margin_y
            x = j * block_size + margin_x

            draw_rectangle_lines_ex((x, y, block_size, block_size), 1, BLACK)
