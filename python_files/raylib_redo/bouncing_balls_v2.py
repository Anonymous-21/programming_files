import pyray as p
from math import cos, sin, radians

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Bouncing Balls"
SCREEN_BACKGROUND: p.Color = p.SKYBLUE

NUM_OF_BALLS: int = 200


class Ball:
    def __init__(self) -> None:
        self.radius: float = p.get_random_value(10, 30)
        self.pos: p.Vector2 = p.Vector2(
            p.get_random_value(self.radius, p.get_screen_width() - self.radius),
            p.get_random_value(self.radius, p.get_screen_height() - self.radius),
        )

        speed: float = p.get_random_value(100, 300)
        angle: float = p.get_random_value(1, 360)
        self.velocity: p.Vector2 = p.Vector2(
            speed * cos(radians(angle)),
            speed * sin(radians(angle)),
        )
        
        self.color: p.Color = p.color_alpha(
            p.Color(
                p.get_random_value(0, 255),
                p.get_random_value(0, 255),
                p.get_random_value(0, 255),
            ),
            255,
        )

    def draw(self) -> None:
        p.draw_circle_v(self.pos, self.radius, self.color)

    def update(self) -> None:
        # move ball
        self.pos.x += self.velocity.x * p.get_frame_time()
        self.pos.y += self.velocity.y * p.get_frame_time()

        # ball bounds
        if self.pos.x < self.radius or self.pos.x > p.get_screen_width() - self.radius:
            self.velocity.x *= -1
        if self.pos.y < self.radius or self.pos.y > p.get_screen_height() - self.radius:
            self.velocity.y *= -1


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    balls: list[Ball] = []

    for i in range(NUM_OF_BALLS):
        ball: Ball = Ball()

        balls.append(ball)

    while not p.window_should_close():
        for ball in balls:
            ball.update()

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        for ball in balls:
            ball.draw()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
