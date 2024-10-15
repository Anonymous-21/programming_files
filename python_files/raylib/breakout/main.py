import pyray as p

from paddle import Paddle
from ball import Ball
from bricks import Bricks

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Breakout"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self):
        self.lives = 5

        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = Bricks()

    def draw(self):
        self.paddle.draw()
        self.ball.draw()
        self.bricks.draw()

    def update(self):
        self.paddle.update()
        self.ball.update()

        # paddle collision with ball
        if p.check_collision_circle_rec(
            (self.ball.x, self.ball.y),
            self.ball.radius,
            (self.paddle.x, self.paddle.y, self.paddle.width, self.paddle.height),
        ):
            self.ball.speed_y *= -1

        # ball collision with bricks
        for row in self.bricks.grid:
            for col in row:
                x, y = col
                if p.check_collision_circle_rec(
                    (self.ball.x, self.ball.y),
                    self.ball.radius,
                    (x, y, self.bricks.width, self.bricks.height),
                ):
                    self.ball.speed_y *= -1


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
