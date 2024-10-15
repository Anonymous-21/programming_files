import pyray as p


class Ball:
    def __init__(self):
        self.radius = 10
        self.initial_x = p.get_screen_width() / 2 - self.radius
        self.initial_y = p.get_screen_height() / 2 - self.radius
        self.x = self.initial_x
        self.y = self.initial_y
        self.color = p.RED
        self.speed_x = 4
        self.speed_y = 5
        self.active = False

    def reset(self):
        self.x = self.initial_x
        self.y = self.initial_y

    def draw(self):
        p.draw_circle_v((self.x, self.y), self.radius, self.color)

    def update(self):
        if p.is_key_pressed(p.KeyboardKey.KEY_SPACE):
            self.active = True

        if self.active:
            self.x += self.speed_x
            self.y += self.speed_y

        # collision with wall
        if self.x <= self.radius or self.x >= p.get_screen_width() - self.radius:
            self.speed_x *= -1
        elif self.y <= self.radius or self.y >= p.get_screen_height() - self.radius:
            self.speed_y *= -1
