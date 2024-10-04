import pyray as pr

from grid import draw_grid
from snake import Snake
from food import Food

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "SNAKE"
SCREEN_BACKGROUND = pr.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self) -> None:
        self.game_over = False

        self.rows = 20
        self.cols = 20
        self.block_size = 30
        self.margin_x = (pr.get_screen_width() - (self.cols * self.block_size)) / 2
        self.margin_y = (pr.get_screen_height() - (self.rows * self.block_size)) / 2

        self.snake = Snake(
            self.rows, self.cols, self.margin_x, self.margin_y, self.block_size
        )
        self.food = Food(self.rows,
                         self.cols,
                         self.margin_x,
                         self.margin_y,
                         self.block_size,
                         self.snake.list)

    def draw(self):
        draw_grid(self.rows, self.cols, self.block_size, self.margin_x, self.margin_y)

        self.snake.draw()
        self.food.draw()

    def update(self):
        if not self.game_over:
            self.snake.update()


def main():
    pr.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    pr.set_target_fps(GAME_FPS)

    game = Game()

    while not pr.window_should_close():
        pr.begin_drawing()
        pr.clear_background(SCREEN_BACKGROUND)

        game.draw()
        game.update()

        pr.end_drawing()

    pr.close_window()


if __name__ == "__main__":
    main()
