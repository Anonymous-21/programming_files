from pyray import *

from grid import draw_grid
from snake import Snake

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "SNAKE"
SCREEN_BACKGROUND = RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self) -> None:
        self.game_over = False

        self.rows = 20
        self.cols = 20
        self.block_size = 30
        self.margin_x = (get_screen_width() - (self.cols * self.block_size)) / 2
        self.margin_y = (get_screen_height() - (self.rows * self.block_size)) / 2

        self.snake = Snake(
            self.rows, self.cols, self.margin_x, self.margin_y, self.block_size
        )

    def draw(self):
        draw_grid(self.rows, self.cols, self.block_size, self.margin_x, self.margin_y)

        self.snake.draw()
        
    def update(self):
        self.snake.move()


def main():
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    set_target_fps(GAME_FPS)

    game = Game()

    while not window_should_close():
        begin_drawing()
        clear_background(SCREEN_BACKGROUND)

        game.draw()

        end_drawing()

    close_window()


if __name__ == "__main__":
    main()
