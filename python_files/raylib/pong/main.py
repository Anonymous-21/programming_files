from pyray import *

from paddle import Paddle
from ball import Ball


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PONG"
SCREEN_BACKGROUND = RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self) -> None:
        self.game_over = False
        self.score_left = 0
        self.score_right = 0

        self.paddle_left = Paddle(x=10)
        self.paddle_right = Paddle(
            x=get_screen_width() - self.paddle_left.width - 10,
        )
        self.ball = Ball()

    def draw(self):
        # draw screen divider
        draw_line_ex((SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT), 5, GRAY)

        # draw score
        # left
        draw_text(str(self.score_left), get_screen_width() // 2 - 70, 10, 30, GRAY)
        # right
        draw_text(str(self.score_right), get_screen_width() // 2 + 50, 10, 30, GRAY)

        self.paddle_left.draw()
        self.paddle_right.draw()
        self.ball.draw()

    def update(self):
        if not self.game_over:
            self.paddle_left.move(key_up=KeyboardKey.KEY_W, key_down=KeyboardKey.KEY_S)
            self.paddle_right.move(
                key_up=KeyboardKey.KEY_UP, key_down=KeyboardKey.KEY_DOWN
            )

            self.score_left, self.score_right = self.ball.move(
                self.score_left, self.score_right
            )

            # collision between ball and paddle
            if check_collision_circle_rec(
                (self.ball.x, self.ball.y),
                self.ball.radius,
                (
                    self.paddle_left.x,
                    self.paddle_left.y,
                    self.paddle_left.width,
                    self.paddle_left.height,
                ),
            ):
                self.ball.change_x *= -1
            elif check_collision_circle_rec(
                (self.ball.x, self.ball.y),
                self.ball.radius,
                (
                    self.paddle_right.x,
                    self.paddle_right.y,
                    self.paddle_right.width,
                    self.paddle_right.height,
                ),
            ):
                self.ball.change_x *= -1


def main():
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    set_target_fps(GAME_FPS)

    game = Game()

    while not window_should_close():
        begin_drawing()
        clear_background(SCREEN_BACKGROUND)

        game.draw()
        game.update()

        end_drawing()

    close_window()


if __name__ == "__main__":
    main()
