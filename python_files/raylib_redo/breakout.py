import pyray as p

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Breakout"
SCREEN_BACKGROUND: p.Color = p.RAYWHITE

ROWS: int = 5
COLS: int = 10
BRICK_WIDTH: int = 79
BRICK_HEIGHT: int = 30
BRICK_GAP: int = 2


class Bricks:
    def __init__(self) -> None:
        self.list: list[p.Vector2] = []
        self.color: p.Color = p.GRAY

        for i in range(ROWS):
            for j in range(COLS):
                x: int = j * (BRICK_WIDTH + BRICK_GAP)
                y: int = i * (BRICK_HEIGHT + BRICK_GAP)

                self.list.append(p.Vector2(x, y))

    def draw(self) -> None:
        for brick in self.list:
            p.draw_rectangle_rec(
                p.Rectangle(brick.x, brick.y, BRICK_WIDTH, BRICK_HEIGHT), self.color
            )


class Paddle:
    def __init__(self) -> None:
        self.width: float = 100.0
        self.height: float = 10.0
        self.initial_x: float = p.get_screen_width() / 2 - self.width / 2
        self.initial_y: float = p.get_screen_height() - self.height - 10.0
        self.x: float = self.initial_x
        self.y: float = self.initial_y
        self.speed: float = 300.0
        self.color: p.Color = p.BLACK

    def reset(self) -> None:
        self.x = self.initial_x
        self.y = self.initial_y

    def draw(self) -> None:
        p.draw_rectangle_rec(
            p.Rectangle(self.x, self.y, self.width, self.height), self.color
        )

    def update(self) -> None:
        # move paddle
        if p.is_key_down(p.KeyboardKey.KEY_LEFT) and self.x > 0:
            self.x -= self.speed * p.get_frame_time()
        if (
            p.is_key_down(p.KeyboardKey.KEY_RIGHT)
            and self.x < p.get_screen_width() - self.width
        ):
            self.x += self.speed * p.get_frame_time()


class Ball:
    def __init__(self, paddle: Paddle) -> None:
        self.paddle: Paddle = paddle
        self.radius: float = 10.0
        self.initial_x: float = self.paddle.x + self.paddle.width / 2
        self.initial_y: float = self.paddle.y - self.paddle.height - (self.radius * 2)
        self.x: float = self.initial_x
        self.y: float = self.initial_y
        self.speed: float = 400.0
        self.direction: p.Vector2 = p.Vector2(
            -1 if p.get_random_value(0, 1) == 0 else 1,
            -1 if p.get_random_value(0, 1) == 0 else 1,
        )
        self.color: p.Color = p.RED
        self.active: bool = False

    def reset(self) -> None:
        self.x = self.initial_x
        self.y = self.initial_y
        self.direction = p.Vector2(
            -1 if p.get_random_value(0, 1) == 0 else 1,
            -1 if p.get_random_value(0, 1) == 0 else 1,
        )
        self.active = False

    def draw(self) -> None:
        p.draw_circle_v(p.Vector2(self.x, self.y), self.radius, self.color)

    def update(self) -> None:
        # update ball position
        if not self.active:
            self.x: float = self.paddle.x + self.paddle.width / 2
            self.y: float = self.paddle.y - self.paddle.height - (self.radius * 2)

        # activate ball
        if p.is_key_pressed(p.KeyboardKey.KEY_SPACE):
            self.active = not self.active

        # move ball
        if self.active:
            self.x += self.direction.x * self.speed * p.get_frame_time()
            self.y += self.direction.y * self.speed * p.get_frame_time()

        # normalize direction vector
        if self.direction.x != 0 and self.direction.y != 0:
            self.direction = p.vector2_normalize(self.direction)

        # ball bounds
        if self.x < self.radius or self.x > p.get_screen_width() - self.radius:
            self.direction.x *= -1
        if self.y < self.radius:
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

    def center_and_draw_text(
        self, text: str, font_size: float, rect: p.Rectangle, tint: p.Color
    ) -> None:
        font: p.Font = p.get_font_default()
        text: str = text
        font_size: float = font_size
        text_width: float = p.measure_text(text, int(font_size))
        text_x: float = rect.x + rect.width / 2 - text_width / 2
        text_y: float = rect.y + rect.height / 2 - font_size / 2
        spacing: float = 5.0
        tint: p.Color = tint

        p.draw_text_ex(font, text, p.Vector2(text_x, text_y), font_size, spacing, tint)

    def draw(self) -> None:
        # draw lives
        p.draw_text(str(self.lives), 20, p.get_screen_height() - 50, 40, p.BLACK)

        self.ball.draw()
        self.paddle.draw()
        self.bricks.draw()

        if self.game_over:
            self.center_and_draw_text(
                "GAME OVER",
                40.0,
                p.Rectangle(0, 0, p.get_screen_width(), p.get_screen_height()),
                p.BLACK,
            )

        if self.game_won:
            self.center_and_draw_text(
                "YOU WIN",
                40.0,
                p.Rectangle(0, 0, p.get_screen_width(), p.get_screen_height()),
                p.BLACK,
            )

    def update(self) -> None:
        if not self.game_won and not self.game_over:
            # game over condition:
            if self.lives <= 0:
                self.game_over = True

            # game won condition
            if len(self.bricks.list) == 0:
                self.game_won = True

            self.paddle.update()
            self.ball.update()

            # ball collision paddle
            if p.check_collision_circle_rec(
                p.Vector2(self.ball.x, self.ball.y),
                self.ball.radius,
                p.Rectangle(
                    self.paddle.x, self.paddle.y, self.paddle.width, self.paddle.height
                ),
            ):
                self.ball.direction.y *= -1

            # ball collision bricks
            for brick in self.bricks.list[:]:
                if p.check_collision_circle_rec(
                    p.Vector2(self.ball.x, self.ball.y),
                    self.ball.radius,
                    p.Rectangle(brick.x, brick.y, BRICK_WIDTH, BRICK_HEIGHT),
                ):
                    self.ball.direction.y *= -1
                    self.bricks.list.remove(brick)

            # update lives
            if self.ball.y > p.get_screen_height():
                self.lives -= 1
                self.reset()
        else:
            if p.is_key_down(p.KeyboardKey.KEY_ENTER):
                self.game_over = False
                self.game_won = False
                self.lives = 5

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
