import arcade

from paddle import Paddle
from ball import Ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PONG"


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.game_over = False

        self.paddle_left = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT, 10)
        self.paddle_right = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH - 10 - self.paddle_left.width)

        self.ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT)

    def draw(self):
        self.clear()

        # draw screen divider
        arcade.draw_line(SCREEN_WIDTH / 2,
                         0,
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT,
                         arcade.color.GRAY,
                         2)

        self.paddle_left.draw()
        self.paddle_right.draw()

        self.ball.draw()

if __name__ == "__main__":
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.draw()
    arcade.run()
    
