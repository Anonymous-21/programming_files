import pyray as p

from grid import Grid
from snake import Snake
from food import Food

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Snake"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self) -> None:
        self.game_over = False
        self.score = 0

        self.grid = Grid()
        self.snake = Snake(self.grid)
        self.food = Food(self.grid, self.snake.list)

    def draw(self):
        # draw score
        p.draw_text(
            f"Score: {self.score}", p.get_screen_width() // 2 - 80, 30, 40, p.GRAY
        )

        self.grid.draw()
        self.snake.draw()
        self.food.draw()

    def update(self):
        self.snake.get_direction()
        self.score = self.snake.move(self.food, self.score)
        self.game_over = self.snake.collision_itself(self.game_over)
        self.game_over = self.snake.collision_walls(self.game_over)

    def game_over_menu(self):
        p.draw_rectangle(
            0, 0, p.get_screen_width(), p.get_screen_height(), SCREEN_BACKGROUND
        )
        p.draw_text(
            f"Score: {self.score}",
            p.get_screen_width() // 2 - 60,
            p.get_screen_height() // 2 - 100,
            40,
            p.GRAY,
        )
        p.draw_text(
            "Game Over",
            p.get_screen_width() // 2 - 70,
            p.get_screen_height() // 2,
            40,
            p.GRAY,
        )
        p.draw_text(
            "Press 'Enter' to restart",
            p.get_screen_width() // 2 - 150,
            p.get_screen_height() // 2 + 70,
            30,
            p.GRAY,
        )

        if p.is_key_pressed(p.KeyboardKey.KEY_ENTER):
            self.game_over = False
            self.score = 0
            self.grid = Grid()
            self.snake = Snake(self.grid)
            self.food = Food(self.grid, self.snake.list)


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    game = Game()

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        if not game.game_over:
            game.draw()
            game.update()
        elif game.game_over:
            game.game_over_menu()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
