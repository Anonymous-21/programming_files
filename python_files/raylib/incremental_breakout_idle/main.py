import pyray as p

from constants import *
from balls import Ball
from bricks import Bricks

class Game:
    def __init__(self) -> None:
        self.ball: Ball = Ball()
        self.bricks: Bricks = Bricks()

    def draw(self) -> None:
        self.bricks.draw()
        self.ball.draw()

    def update(self) -> None:
        self.ball.update()


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
