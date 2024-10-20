import pyray as p


class Paddle:
    def __init__(self, x) -> None:
        self.width = 10
        self.height = 100
        self.initial_x = x
        self.initial_y = p.get_screen_height() / 2 - self.height / 2
        self.x = self.initial_x
        self.y = self.initial_y
        self.color = p.BLACK
        self.speed = 8

    def reset(self):
        self.x = self.initial_x
        self.y = self.initial_y

    def draw(self):
        p.draw_rectangle_rec((self.x, self.y, self.width, self.height), self.color)

    def move(self, key_up, key_down):
        if p.is_key_down(key_up) and self.y >= 0:
            self.y -= self.speed
        elif p.is_key_down(key_down) and self.y <= p.get_screen_height() - self.height:
            self.y += self.speed
