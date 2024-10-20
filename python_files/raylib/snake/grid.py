import pyray as p


class Grid:
    def __init__(self) -> None:
        self.rows = 20
        self.cols = 20
        self.block_size = 30
        self.margin = 100
        self.color = p.BLACK
        self.line_thickness = 1

    def draw(self):
        for i in range(self.rows):
            for j in range(self.cols):
                x = j * self.block_size + self.margin
                y = i * self.block_size + self.margin

                p.draw_rectangle_lines_ex(
                    (x, y, self.block_size, self.block_size),
                    self.line_thickness,
                    self.color,
                )
