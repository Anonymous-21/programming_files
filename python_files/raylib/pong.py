import pyray as p

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Pong"
SCREEN_BACKGROUND: p.Color = p.SKYBLUE


class Ball:
    def __init__(self) -> None:
        self.initial_x: float = p.get_screen_width() / 2
        self.initial_y: float = p.get_screen_height() / 2
        self.x: float = self.initial_x
        self.y: float = self.initial_y
        self.radius: float = 10.0
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
        self.direction.x *= -1
        self.active = False

    def draw(self) -> None:
        p.draw_circle_v(p.Vector2(self.x, self.y), self.radius, self.color)

    def update(self) -> None:
        # activate ball
        if p.is_key_pressed(p.KeyboardKey.KEY_SPACE):
            self.active = not self.active

        if abs(self.pos.x) > 0.01 and abs(self.pos.y) > 0.01:
            self.direction = p.vector2_normalize(self.direction)

        # move ball
        if self.active:
            self.x += self.direction.x * self.speed * p.get_frame_time()
            self.y += self.direction.y * self.speed * p.get_frame_time()

        # ball bounds
        if self.y < self.radius or self.y > p.get_screen_height() - self.radius:
            self.direction.y *= -1


class Paddle:
    def __init__(self, x: float) -> None:
        self.width: float = 10.0
        self.height: float = 100.0
        self.initial_x: float = x
        self.initial_y: float = p.get_screen_height() / 2 - self.height / 2
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

    def update_player(self) -> None:
        # move paddle
        if p.is_key_down(p.KeyboardKey.KEY_UP):
            self.y -= self.speed * p.get_frame_time()
        if p.is_key_down(p.KeyboardKey.KEY_DOWN):
            self.y += self.speed * p.get_frame_time()

        # paddle bounds
        self.y = max(0.0, min(self.y, p.get_screen_height() - self.height))

    def update_ai(self, ball: Ball) -> None:
        # move paddle
        if ball.y < self.y + self.height / 2:
            self.y -= self.speed * p.get_frame_time()
        if ball.y > self.y + self.height / 2:
            self.y += self.speed * p.get_frame_time()

        # paddle bounds
        self.y = max(0.0, min(self.y, p.get_screen_height() - self.height))


class Game:
    def __init__(self) -> None:
        self.score_left: int = 0
        self.score_right: int = 0

        self.ball: Ball = Ball()
        self.player: Paddle = Paddle(10.0)
        self.ai: Paddle = Paddle(p.get_screen_width() - self.player.width - 10.0)

    def reset(self) -> None:
        self.ball.reset()
        self.player.reset()
        self.ai.reset()

    def draw(self) -> None:
        # draw scores
        p.draw_text(str(self.score_left), 200, 30, 40, p.BLACK)
        p.draw_text(str(self.score_right), p.get_screen_width() - 200, 30, 40, p.BLACK)

        self.ball.draw()
        self.player.draw()
        self.ai.draw()

    def update(self) -> None:
        self.ball.update()
        self.player.update_player()
        self.ai.update_ai(self.ball)

        # ball collision paddle
        if p.check_collision_circle_rec(
            p.Vector2(self.ball.x, self.ball.y),
            self.ball.radius,
            p.Rectangle(
                self.player.x, self.player.y, self.player.width, self.player.height
            ),
        ):
            self.ball.direction.x *= -1

        if p.check_collision_circle_rec(
            p.Vector2(self.ball.x, self.ball.y),
            self.ball.radius,
            p.Rectangle(self.ai.x, self.ai.y, self.ai.width, self.ai.height),
        ):
            self.ball.direction.x *= -1

        # update scores
        if self.ball.x < self.ball.radius:
            self.score_right += 1
            self.reset()
        if self.ball.x > p.get_screen_width() - self.ball.radius:
            self.score_left += 1
            self.reset()


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
