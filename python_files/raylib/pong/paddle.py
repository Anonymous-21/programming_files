import pyray as p


class Paddle:
    def __init__(self, x):
        self.width = 10
        self.height = 100
        self.x = x
        self.y = p.get_screen_height() / 2 - self.height / 2
        self.color = p.BLACK
        self.speed = 8

    def draw(self):
        p.draw_rectangle_rec((self.x, self.y, self.width, self.height), self.color)

    def move(self, key_up, key_down):
        if p.is_key_down(key_up) and self.y >= 0:
            self.y -= self.speed
        elif p.is_key_down(key_down) and self.y <= p.get_screen_height() - self.height:
            self.y += self.speed

    def collision_ball(self, ball):
        if p.check_collision_circle_rec(
            (ball.x, ball.y), ball.radius, (self.x, self.y, self.width, self.height)
        ):
            ball.speed_x *= -1
