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
        self.left_score = 0
        self.right_score = 0

        self.paddle_left = Paddle(10)
        self.paddle_right = Paddle(p.get_screen_width() - self.paddle_left.width - 10)

        self.ball = Ball()

    def draw(self):
        # draw screen divider
        p.draw_line_ex(
            (p.get_screen_width() / 2, 0),
            (p.get_screen_width() / 2, p.get_screen_height()),
            5,
            p.GRAY,
        )
        # draw score
        p.draw_text(
            str(self.left_score), p.get_screen_width() // 2 - 70, 10, 30, p.GRAY
        )
        p.draw_text(
            str(self.right_score), p.get_screen_width() // 2 + 50, 10, 30, p.GRAY
        )

        self.paddle_left.draw()
        self.paddle_right.draw()

        self.ball.draw()

    def update(self):
        self.paddle_left.move(p.KeyboardKey.KEY_W, p.KeyboardKey.KEY_S)
        self.paddle_right.move(p.KeyboardKey.KEY_UP, p.KeyboardKey.KEY_DOWN)

        self.paddle_left.collision_ball(self.ball)
        self.paddle_right.collision_ball(self.ball)

        self.ball.move()
        self.left_score, self.right_score = self.ball.collision_walls(
            self.paddle_left, self.paddle_right, self.left_score, self.right_score
        )


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
