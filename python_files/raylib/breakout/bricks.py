import pyray as p


class Bricks:
    def __init__(self) -> None:
        self.rows = 5
        self.cols = 10
        self.width = 78
        self.height = 30
        self.grid = []
        self.color_num = 1

        self.gen_grid()
        self.update_colors()

    def update_colors(self):
        match self.color_num:
            case 1:
                self.color = p.RED
            case 2:
                self.color = p.BLUE
            case 3:
                self.color = p.GREEN
            case 4:
                self.color = p.YELLOW
            case 5:
                self.color = p.PURPLE

    def gen_grid(self):
        self.grid = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                x = j * (self.width + 2)
                y = i * (self.height + 2)

                row.append((x, y))

            self.grid.append(row)

    def draw(self):
        for row in self.grid:
            for brick in row:
                p.draw_rectangle_rec(
                    p.Rectangle(brick[0], brick[1], self.width, self.height), self.color
                )

            self.color_num += 1
            if self.color_num > 5:
                self.color_num = 1
            self.update_colors()

    def collision_ball(self, ball):
        for row in range(len(self.grid)):
            for brick in range(row):
                if p.check_collision_circle_rec(
                    (ball.x, ball.y),
                    ball.radius,
                    (
                        self.grid[row][brick][0],
                        self.grid[row][brick][0],
                        self.width,
                        self.height,
                    ),
                ):
                    del self.grid[row][brick]
