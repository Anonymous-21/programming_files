import pyray as p


class Ball:
    def __init__(self) -> None:
        self.radius: float = 10.0
        self.pos: p.Vector2 = p.Vector2(self.radius, self.radius)
        self.speed: float = 250.0
        self.color: p.Color = p.RED
        self.damage: float = 1.0
        self.direction: p.Vector2 = p.Vector2(1, 1)

    def draw(self) -> None:
        p.draw_circle_v(self.pos, self.radius, self.color)

    def update(self) -> None:
        # move ball
        self.pos.x += self.direction.x * self.speed * p.get_frame_time()
        self.pos.y += self.direction.y * self.speed * p.get_frame_time()

        # ball bounds
        if self.pos.x < self.radius or self.pos.x > p.get_screen_width() - self.radius:
            self.direction.x *= -1
        if self.pos.y < self.radius or self.pos.y > p.get_screen_height() - self.radius:
            self.direction.y *= -1

        # normalize direction vector
        if self.direction.x != 0 and self.direction.y != 0:
            self.direction = p.vector2_normalize(self.direction)
