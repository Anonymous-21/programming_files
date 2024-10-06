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

    def on_draw(self):
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

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.paddle_left.change_y = self.paddle_left.speed
        elif key == arcade.key.S:
            self.paddle_left.change_y = -self.paddle_left.speed

        if key == arcade.key.UP:
            self.paddle_right.change_y = self.paddle_right.speed
        elif key == arcade.key.DOWN:
            self.paddle_right.change_y = -self.paddle_right.speed

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W:
            self.paddle_left.change_y = 0
        elif key == arcade.key.S:
            self.paddle_left.change_y = 0

        if key == arcade.key.UP:
            self.paddle_right.change_y = 0
        elif key == arcade.key.DOWN:
            self.paddle_right.change_y = 0

    def on_update(self, delta_time):
        self.paddle_left.update()
        self.paddle_right.update()    

        self.ball.update()


if __name__ == "__main__":
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
    
