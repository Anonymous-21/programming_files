import raylib as r
import random


class Food:
    def __init__(self, rows, cols, box_size, snake) -> None:
        self.rows = rows
        self.cols = cols
        self.snake = snake
        self.box_size = box_size
        self.x, self.y = self.gen_random_coordinates()
        self.width = box_size
        self.height = box_size
        self.color = r.RED

    def gen_random_coordinates(self):
        while True:
            x = random.randint(0, self.rows - 1) * self.box_size
            y = random.randint(0, self.cols - 1) * self.box_size

            if (x, y) not in self.snake.list:
                return (x, y)

    def draw(self):
        r.DrawRectangle(self.x, self.y, self.width, self.height, self.color)
