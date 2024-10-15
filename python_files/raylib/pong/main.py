import pyray as p

from paddle import Paddle
from ball import Ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self):
        self.left_score = 0
        self.right_score = 0

        self.left_paddle = Paddle(x=10)
        self.right_paddle = Paddle(x=p.get_screen_width() - self.left_paddle.width - 10)

        self.ball = Ball()

    def draw(self):
        # draw score
        p.draw_text(
            str(self.left_score), p.get_screen_width() // 2 - 70, 20, 30, p.GRAY
        )
        p.draw_text(
            str(self.right_score), p.get_screen_width() // 2 + 50, 20, 30, p.GRAY
        )
        # draw screen divider
        p.draw_line_ex(
            (p.get_screen_width() / 2, 0),
            (p.get_screen_width() / 2, p.get_screen_height()),
            5,
            p.GRAY,
        )

        self.left_paddle.draw()
        self.right_paddle.draw()

        self.ball.draw()

    def update(self):
        self.left_paddle.update(p.KeyboardKey.KEY_W, p.KeyboardKey.KEY_S)
        self.right_paddle.update(p.KeyboardKey.KEY_UP, p.KeyboardKey.KEY_DOWN)

        self.ball.update()

        # ball collision with paddle
        if p.check_collision_circle_rec(
            (self.ball.x, self.ball.y),
            self.ball.radius,
            (
                self.left_paddle.x,
                self.left_paddle.y,
                self.left_paddle.width,
                self.left_paddle.height,
            ),
        ):
            self.ball.speed_x *= -1
        elif p.check_collision_circle_rec(
            (self.ball.x, self.ball.y),
            self.ball.radius,
            (
                self.right_paddle.x,
                self.right_paddle.y,
                self.right_paddle.width,
                self.right_paddle.height,
            ),
        ):
            self.ball.speed_x *= -1

        # ball horizontal wall collision and score update
        if self.ball.x <= self.ball.radius:
            self.right_score += 1
            self.ball.reset()
            self.left_paddle.reset()
            self.right_paddle.reset()
            self.ball.speed_x *= -1
        elif self.ball.x >= p.get_screen_width() - self.ball.radius:
            self.left_score += 1
            self.ball.reset()
            self.left_paddle.reset()
            self.right_paddle.reset()
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
