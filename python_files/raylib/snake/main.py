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
        self.score = 0

        self.rows = 20
        self.cols = 20
        self.block_size = 30
        self.margin_x = (pr.get_screen_width() - (self.cols * self.block_size)) / 2
        self.margin_y = (pr.get_screen_height() - (self.rows * self.block_size)) / 2

        self.snake = Snake(
            self.rows, self.cols, self.margin_x, self.margin_y, self.block_size
        )
        self.food = Food(
            self.rows,
            self.cols,
            self.margin_x,
            self.margin_y,
            self.block_size,
            self.snake.list,
        )

    def draw(self):
        draw_grid(self.rows, self.cols, self.block_size, self.margin_x, self.margin_y)

        # draw score
        pr.draw_text(
            f"SCORE: {self.score}",
            pr.get_screen_width() // 2 - 65,
            40,
            30,
            pr.GRAY,
        )

        self.snake.draw()
        self.food.draw()

    def update(self):
        self.food.x, self.food.y, self.score = self.snake.update(self.food, self.score)

        self.game_over = self.snake.collision_walls(self.game_over)
        self.game_over = self.snake.collision_itself(self.game_over)

    def game_over_menu(self):
        if self.game_over:
            pr.draw_rectangle_rec(
                (0, 0, pr.get_screen_width(), pr.get_screen_height()), SCREEN_BACKGROUND
            )
            pr.draw_text(
                f"SCORE: {self.score}",
                pr.get_screen_width() // 2 - 90,
                pr.get_screen_height() // 2 - 100,
                40,
                pr.GRAY,
            )
            pr.draw_text(
                "GAME OVER",
                pr.get_screen_width() // 2 - 110,
                pr.get_screen_height() // 2,
                40,
                pr.GRAY,
            )
            pr.draw_text(
                "Press 'ENTER' to continue",
                pr.get_screen_width() // 2 - 250,
                pr.get_screen_height() // 2 + 100,
                40,
                pr.GRAY,
            )

            if pr.is_key_pressed(pr.KeyboardKey.KEY_ENTER):
                self.game_over = False
                self.score = 0
                self.snake = Snake(
                    self.rows, self.cols, self.margin_x, self.margin_y, self.block_size
                )
                self.food = Food(
                    self.rows,
                    self.cols,
                    self.margin_x,
                    self.margin_y,
                    self.block_size,
                    self.snake.list,
                )


def main():
    pr.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    pr.set_target_fps(GAME_FPS)

    game = Game()

    while not pr.window_should_close():
        pr.begin_drawing()
        pr.clear_background(SCREEN_BACKGROUND)

        if not game.game_over:
            game.draw()
            game.update()
        else:
            game.game_over_menu()

        pr.end_drawing()

    pr.close_window()


if __name__ == "__main__":
    main()
