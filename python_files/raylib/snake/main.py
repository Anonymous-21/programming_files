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

        self.snake.draw()
        self.food.draw()

    def update(self):
        self.game_over = self.snake.update()

        # snake collision with food
        for segment in self.snake.list:
            if pr.check_collision_recs(
                (segment[0], segment[1], self.snake.width, self.snake.height),
                (self.food.x, self.food.y, self.food.width, self.food.height),
            ):
                self.food.x, self.food.y = self.food.gen_random_food()
                self.snake.list.append(self.snake.list[-1])

    def game_over_menu(self):
        if self.game_over:
            pr.draw_rectangle_rec(
                (0, 0, pr.get_screen_width(), pr.get_screen_height()), SCREEN_BACKGROUND
            )
            pr.draw_text(
                "GAME OVER",
                pr.get_screen_width() // 2 - 110,
                pr.get_screen_height() // 2 - 100,
                40,
                pr.GRAY,
            )
            pr.draw_text(
                "Press 'ENTER' to continue",
                pr.get_screen_width() // 2 - 180,
                pr.get_screen_height() // 2,
                30,
                pr.GRAY,
            )

            if pr.is_key_pressed(pr.KeyboardKey.KEY_ENTER):
                self.game_over = False
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
