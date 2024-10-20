import pyray as p

from paddle import Paddle
from ball import Ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self) -> None:
        self.score_left = 0
        self.score_right = 0

        self.paddle_left = Paddle(10)
        self.paddle_right = Paddle(p.get_screen_width() - self.paddle_left.width - 10)

        self.ball = Ball()

    def draw(self):
        # print scores
        p.draw_text(
            str(self.score_left), p.get_screen_width() // 2 - 70, 20, 30, p.GRAY
        )
        p.draw_text(
            str(self.score_right), p.get_screen_width() // 2 + 50, 20, 30, p.GRAY
        )

        # draw screen divider
        p.draw_line_ex(
            (p.get_screen_width() / 2, 0),
            (p.get_screen_width() / 2, p.get_screen_height()),
            5,
            p.GRAY,
        )

        self.paddle_left.draw()
        self.paddle_right.draw()

        self.ball.draw()

    def update(self):
        self.paddle_left.move(p.KeyboardKey.KEY_W, p.KeyboardKey.KEY_S)
        self.paddle_right.move(p.KeyboardKey.KEY_UP, p.KeyboardKey.KEY_DOWN)

        self.ball.update()

        # ball collision with horizontal walls
        if self.ball.x <= self.ball.radius:
            self.score_right += 1
            self.ball.frames_counter = 0
            self.ball.speed_x *= -1
            self.ball.reset()
            self.paddle_left.reset()
            self.paddle_right.reset()
        elif self.ball.x >= p.get_screen_width() - self.ball.radius:
            self.score_left += 1
            self.ball.frames_counter = 0
            self.ball.speed_x *= -1
            self.ball.reset()
            self.paddle_left.reset()
            self.paddle_right.reset()

        # ball collision paddles
        if p.check_collision_circle_rec(
            (self.ball.x, self.ball.y),
            self.ball.radius,
            (
                self.paddle_left.x,
                self.paddle_left.y,
                self.paddle_left.width,
                self.paddle_left.height,
            ),
        ):
            self.ball.speed_x *= -1
        elif p.check_collision_circle_rec(
            (self.ball.x, self.ball.y),
            self.ball.radius,
            (
                self.paddle_right.x,
                self.paddle_right.y,
                self.paddle_right.width,
                self.paddle_right.height,
            ),
        ):
            self.ball.speed_x *= -1


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    game = Game()

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        game.draw()
        game.update()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
