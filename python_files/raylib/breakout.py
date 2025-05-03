import pyray as p
from dataclasses import dataclass
from random import randint

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Breakout"
SCREEN_BACKGROUND: p.Color = p.RAYWHITE

ROWS: int = 5
COLS: int = 10
BRICK_WIDTH: int = 79
BRICK_HEIGHT: int = 30
BRICK_GAP: int = 2


@dataclass
class Brick:
    rect: p.Rectangle
    color: p.Color


class Bricks:
    def __init__(self) -> None:
        self.list: list[Brick] = []

        for i in range(ROWS):
            for j in range(COLS):
                x: int = j * (BRICK_WIDTH + BRICK_GAP)
                y: int = i * (BRICK_HEIGHT + BRICK_GAP)

                brick: Brick = Brick(
                    rect=p.Rectangle(x, y, BRICK_WIDTH, BRICK_HEIGHT),
                    color=p.GRAY,
                )

                self.list.append(brick)

    def draw(self) -> None:
        for brick in self.list:
            p.draw_rectangle_rec(brick.rect, brick.color)


class Paddle:
    def __init__(self) -> None:
        width: float = 100.0
        height: float = 10.0

        self.initial_rect: p.Rectangle = p.Rectangle(
            p.get_screen_width() / 2 - width / 2,
            p.get_screen_height() - height - 10.0,
            width,
            height,
        )
        self.rect: p.Rectangle = self.initial_rect
        self.speed: float = 300.0
        self.color: p.Color = p.BLACK

    def reset(self) -> None:
        self.rect = self.initial_rect

    def draw(self) -> None:
        p.draw_rectangle_rec(self.rect, self.color)

    def update(self) -> None:
        # move paddle
        if p.is_key_down(p.KeyboardKey.KEY_LEFT):
            self.rect.x -= self.speed * p.get_frame_time()
        if p.is_key_down(p.KeyboardKey.KEY_RIGHT):
            self.rect.x += self.speed * p.get_frame_time()

        # paddle bounds
        self.rect.x = max(0.0, min(self.rect.x, p.get_screen_width() - self.rect.width))


class Ball:
    def __init__(self, paddle: Paddle) -> None:
        self.paddle: Paddle = paddle

        self.radius: float = 10.0
        self.initial_pos: p.Vector2 = p.Vector2(
            self.paddle.rect.x + self.paddle.rect.width / 2,
            self.paddle.rect.y - self.radius - 10.0,
        )
        self.pos: p.Vector2 = self.initial_pos
        self.speed: float = 400.0
        random_x: int = -1 if randint(0, 1) == 0 else 1
        self.direction: p.Vector2 = p.Vector2(random_x, 1)
        self.color: p.Color = p.RED
        self.is_active: bool = False

    def reset(self) -> None:
        self.pos = self.initial_pos
        random_x: int = -1 if randint(0, 1) == 0 else 1
        self.direction: p.Vector2 = p.Vector2(random_x, 1)
        self.is_active: bool = False

    def draw(self) -> None:
        p.draw_circle_v(self.pos, self.radius, self.color)

    def update(self) -> None:
        # update ball position if ball inactive
        if not self.is_active:
            self.pos: p.Vector2 = p.Vector2(
                self.paddle.rect.x + self.paddle.rect.width / 2,
                self.paddle.rect.y - self.radius - 10.0,
            )

        if abs(self.pos.x) > 0.01 and abs(self.pos.y) > 0.01:
            self.direction = p.vector2_normalize(self.direction)

        # activate ball
        if p.is_key_pressed(p.KeyboardKey.KEY_SPACE):
            self.is_active = not self.is_active

        # move ball
        if self.is_active:
            self.pos.x += self.direction.x * self.speed * p.get_frame_time()
            self.pos.y += self.direction.y * self.speed * p.get_frame_time()

        # ball bounds
        if self.pos.x < self.radius or self.pos.x > p.get_screen_width() - self.radius:
            self.direction.x *= -1
        if self.pos.y < self.radius:
            self.direction.y *= -1


class Game:
    def __init__(self) -> None:
        self.lives: int = 5
        self.game_over: bool = False
        self.game_won: bool = False

        self.bricks: Bricks = Bricks()
        self.paddle: Paddle = Paddle()
        self.ball: Ball = Ball(self.paddle)

    def reset(self) -> None:
        self.paddle.reset()
        self.ball.reset()

    def draw(self) -> None:
        # draw lives
        p.draw_text(str(self.lives), 20, p.get_screen_height() - 50, 40, p.BLACK)

        self.bricks.draw()
        self.paddle.draw()
        self.ball.draw()

    def update(self) -> None:
        if not self.game_over and not self.game_won:
            if len(self.bricks.list) <= 0:
                self.game_won = True

            if self.lives <= 0:
                self.game_over = True

            self.paddle.update()
            self.ball.update()

            # ball collision paddle
            if p.check_collision_circle_rec(
                self.ball.pos, self.ball.radius, self.paddle.rect
            ):
                self.ball.direction.y *= -1

            # ball collision bricks
            for brick in self.bricks.list:
                if p.check_collision_circle_rec(
                    self.ball.pos, self.ball.radius, brick.rect
                ):
                    self.ball.direction.y *= -1
                    self.bricks.list.remove(brick)

            # update lives
            if self.ball.pos.y > p.get_screen_height():
                self.lives -= 1
                self.reset()

        else:
            if p.is_key_pressed(p.KeyboardKey.KEY_ENTER):
                self.lives = 5
                self.game_over = False
                self.game_won = False

                self.bricks = Bricks()
                self.paddle = Paddle()
                self.ball = Ball(self.paddle)


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    game: Game = Game()

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        game.draw()
        game.update()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
