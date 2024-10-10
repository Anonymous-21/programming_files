import pyray as p
from paddle import Paddle
from ball import Ball
from bricks import Bricks

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "BREAKOUT"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self):
        self.game_over = False
        self.lives = 5

        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = Bricks()

    def draw(self):
        self.paddle.draw()
        self.ball.draw()
        self.bricks.draw()

    def update(self):
        self.paddle.move()
        self.paddle.collision_ball(self.ball)
        self.ball.move()
        self.ball.collision_walls(self.lives)
        self.bricks.collision_ball(self.ball)


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
