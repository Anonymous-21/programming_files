import pyray as p


class Ball:
    def __init__(self) -> None:
        self.radius = 10
        self.initial_x = p.get_screen_width() / 2
        self.initial_y = p.get_screen_height() / 2
        self.x = self.initial_x
        self.y = self.initial_y
        self.color = p.RED
        self.change_x = 5
        self.change_y = 6

    def ball_reset(self):
        self.x = self.initial_x
        self.y = self.initial_y

    def draw(self):
        p.draw_circle_v((self.x, self.y), self.radius, self.color)

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def collision_walls(self, lives):
        if self.x <= self.radius:
            self.change_x *= -1
        elif self.x >= p.get_screen_width() - self.radius:
            self.change_x *= -1
        elif self.y <= self.radius:
            self.change_y *= -1
        elif self.y >= p.get_screen_height() - self.radius:
            lives -= 1
            self.ball_reset()
            self.change_x *= -1
