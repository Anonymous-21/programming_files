import pyray as p
import random


class Food:
    def __init__(self, grid, snake_list) -> None:
        self.grid = grid
        self.snake_list = snake_list
        self.width = self.grid.block_size
        self.height = self.grid.block_size
        self.x, self.y = self.gen_random_food()
        self.color = p.RED

    def gen_random_food(self):
        while True:
            x = (
                random.randint(0, self.grid.rows - 1) * self.grid.block_size
            ) + self.grid.margin
            y = (
                random.randint(0, self.grid.cols - 1) * self.grid.block_size
            ) + self.grid.margin

            if (x, y) not in self.snake_list:
                return (x, y)

    def draw(self):
        p.draw_rectangle_rec((self.x, self.y, self.width, self.height), self.color)
