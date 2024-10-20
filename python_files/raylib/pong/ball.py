import pyray as p


class Ball:
    def __init__(self) -> None:
        self.radius = 10
        self.initial_x = p.get_screen_width() / 2
        self.initial_y = p.get_screen_height() / 2
        self.x = self.initial_x
        self.y = self.initial_y
        self.color = p.RED
        self.speed_x = 5
        self.speed_y = 6
        self.frames_counter = 0

    def reset(self):
        self.x = self.initial_x
        self.y = self.initial_y

    def draw(self):
        p.draw_circle_v((self.x, self.y), self.radius, self.color)

    def update(self):
        self.frames_counter += 1
        if self.frames_counter > 60:
            self.frames_counter = 61
            self.x += self.speed_x
            self.y += self.speed_y
        

        if self.y <= self.radius or self.y >= p.get_screen_height() - self.radius:
            self.speed_y *= -1
