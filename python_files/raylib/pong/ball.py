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
        self.active = False

    def reset(self):
        self.x = self.initial_x
        self.y = self.initial_y

    def draw(self):
        p.draw_circle_v((self.x, self.y), self.radius, self.color)

    def move(self):
        if not self.active:
            if p.is_key_pressed(p.KeyboardKey.KEY_SPACE):
                self.active = True

        if self.active:
            self.x += self.speed_x
            self.y += self.speed_y

    def collision_walls(self, paddle_left, paddle_right, left_score, right_score):
        if self.x <= self.radius:
            right_score += 1
            self.active = False
            self.speed_x *= -1
            self.reset()
            paddle_left.reset()
            paddle_right.reset()
        elif self.x >= p.get_screen_width() - self.radius:
            left_score += 1
            self.active = False
            self.speed_x *= -1
            self.reset()
            paddle_left.reset()
            paddle_right.reset()
        elif self.y <= self.radius or self.y >= p.get_screen_height() - self.radius:
            self.speed_y *= -1

        return (left_score, right_score)
