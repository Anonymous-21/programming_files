import pyray as p
import random


class Bricks:
    def __init__(self):
        self.rows = 5
        self.cols = 10
        self.width = 79
        self.height = 28
        self.color_num = 1
        self.gap = 2
        self.grid = []

        self.update_color()
        self.gen_grid()

    def update_color(self):
        match self.color_num:
            case 1:
                self.color = p.RED
            case 2:
                self.color = p.GREEN
            case 3:
                self.color = p.BLUE
            case 4:
                self.color = p.ORANGE
            case 5:
                self.color = p.PURPLE

    def gen_grid(self):
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                x = j * (self.width + self.gap)
                y = i * (self.height + self.gap)

                row.append((x, y))

            self.grid.append(row)

    def draw(self):
        for rows in self.grid:
            for cols in rows:
                x, y = cols

                p.draw_rectangle_rec(
                    (x, y, self.width, self.height),
                    self.color,
                )

            self.color_num += 1
            if self.color_num > 5:
                self.color_num = 1
            self.update_color()

