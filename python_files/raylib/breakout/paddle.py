import pyray as p


class Paddle:
    def __init__(self) -> None:
        self.width = 100
        self.height = 10
        self.initial_x = p.get_screen_width() / 2 - self.width / 2
        self.initial_y = p.get_screen_height() - self.height - 20
        self.x = self.initial_x
        self.y = self.initial_y
        self.color = p.BLACK
        self.speed = 8

    def reset(self):
        self.x = self.initial_x
        self.y = self.initial_y

    def draw(self):
        p.draw_rectangle_rec((self.x, self.y, self.width, self.height), self.color)

    def update(self):
        if (
            p.is_key_down(p.KeyboardKey.KEY_RIGHT)
            and self.x < p.get_screen_width() - self.width
        ):
            self.x += self.speed
        elif p.is_key_down(p.KeyboardKey.KEY_LEFT) and self.x > 0:
            self.x -= self.speed
