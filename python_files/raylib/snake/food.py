import pyray as pr
import random


class Food:
    def __init__(self, rows, cols, margin_x, margin_y, block_size, snake_list) -> None:
        self.rows = rows
        self.cols = cols
        self.margin_x = margin_x
        self.margin_y = margin_y
        self.block_size = block_size
        self.snake_list = snake_list

        self.x, self.y = self.gen_random_food()
        self.width = block_size
        self.height = block_size
        self.color = pr.RED

    def gen_random_food(self):
        while True:
            x = random.randint(0, self.cols - 1) * self.block_size + self.margin_x
            y = random.randint(0, self.rows - 1) * self.block_size + self.margin_y
            
            if (x, y) not in self.snake_list:
                return (x, y)

    def draw(self):
        pr.draw_rectangle_rec((self.x, self.y, self.width, self.height), self.color)
