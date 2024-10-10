import pyray as p


class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.x = p.get_screen_width() / 2 - self.width / 2
        self.y = p.get_screen_height() - self.height / 2 - 20
        self.color = p.BLACK
        self.speed = 8

    def draw(self):
        p.draw_rectangle_rec((self.x, self.y, self.width, self.height), self.color)

    def move(self):
        if (
            p.is_key_down(p.KeyboardKey.KEY_RIGHT)
            and self.x <= p.get_screen_width() - self.width
        ):
            self.x += self.speed
        elif p.is_key_down(p.KeyboardKey.KEY_LEFT) and self.x >= 0:
            self.x -= self.speed

    def collision_ball(self, ball):
        if p.check_collision_circle_rec(
            (ball.x, ball.y), ball.radius, (self.x, self.y, self.width, self.height)
        ):
            ball.change_y *= -1
