import pyray as p
from dataclasses import dataclass
from random import uniform, randint

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Bouncing Balls"
SCREEN_BACKGROUND: p.Color = p.SKYBLUE

NUM_OF_BALLS: int = 200


@dataclass
class Ball:
    pos: p.Vector2
    radius: float
    speed: float
    direction: p.Vector2
    color: p.Color


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    balls: list[Ball] = []

    for i in range(NUM_OF_BALLS):
        ball: Ball = Ball(
            pos=p.Vector2(
                uniform(0, p.get_screen_width()), uniform(0, p.get_screen_height())
            ),
            radius=uniform(5, 30),
            speed=uniform(100, 300),
            direction=p.Vector2(
                -1 if randint(0, 1) == 0 else 1,
                -1 if randint(0, 1) == 0 else 1,
            ),
            color=p.Color(randint(0, 255), randint(0, 255), randint(0, 255), 255),
        )

        balls.append(ball)

    while not p.window_should_close():
        for ball in balls:
            ball.pos.x += ball.direction.x * ball.speed * p.get_frame_time()
            ball.pos.y += ball.direction.y * ball.speed * p.get_frame_time()

            if (
                ball.pos.x < ball.radius
                or ball.pos.x > p.get_screen_width() - ball.radius
            ):
                ball.direction.x *= -1
            if (
                ball.pos.y < ball.radius
                or ball.pos.y > p.get_screen_height() - ball.radius
            ):
                ball.direction.y *= -1

            if ball.direction.x != 0 and ball.direction.y != 0:
                ball.direction = p.vector2_normalize(ball.direction)

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        for ball in balls:
            p.draw_circle_v(ball.pos, ball.radius, ball.color)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
