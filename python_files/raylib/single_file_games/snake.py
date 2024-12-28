import pyray as p
from random import randint


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Snake"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60
ROWS = 20
COLS = 20
BLOCK_SIZE = 30
MARGIN = 100


class Snake:
    def __init__(self):
        self.x = MARGIN
        self.y = MARGIN
        self.list = [p.Vector2(self.x, self.y)]
        self.direction = "right"
        self.frames_counter = 0

    def draw(self):
        for i in range(0, len(self.list)):
            if i == 0:
                color = p.BLUE
            else:
                color = p.SKYBLUE

            p.draw_rectangle_rec(
                (self.list[i].x, self.list[i].y, BLOCK_SIZE, BLOCK_SIZE), color
            )

    def get_direction(self):
        if p.is_key_pressed(p.KeyboardKey.KEY_LEFT) and self.direction != "right":
            self.direction = "left"
        elif p.is_key_pressed(p.KeyboardKey.KEY_RIGHT) and self.direction != "left":
            self.direction = "right"
        elif p.is_key_pressed(p.KeyboardKey.KEY_UP) and self.direction != "down":
            self.direction = "up"
        elif p.is_key_pressed(p.KeyboardKey.KEY_DOWN) and self.direction != "up":
            self.direction = "down"

    def update(self, food, score):
        self.get_direction()

        self.frames_counter += 1
        if self.frames_counter % 5 == 0:
            if self.frames_counter >= 1000:
                self.frames_counter = 0

            match self.direction:
                case "right":
                    self.x += BLOCK_SIZE
                case "left":
                    self.x -= BLOCK_SIZE
                case "up":
                    self.y -= BLOCK_SIZE
                case "down":
                    self.y += BLOCK_SIZE

            if self.x < MARGIN:
                self.x = p.get_screen_width() - MARGIN - BLOCK_SIZE
            elif self.x > p.get_screen_width() - MARGIN - BLOCK_SIZE:
                self.x = MARGIN
            elif self.y < MARGIN:
                self.y = p.get_screen_height() - MARGIN - BLOCK_SIZE
            elif self.y > p.get_screen_height() - MARGIN - BLOCK_SIZE:
                self.y = MARGIN

            # snake collision food
            if p.check_collision_recs(
                (self.list[0].x, self.list[0].y, BLOCK_SIZE, BLOCK_SIZE),
                (food.x, food.y, BLOCK_SIZE, BLOCK_SIZE),
            ):
                food.gen_random_food()
                self.list.append(self.list[-1])
                score += 1

            self.list.insert(0, p.Vector2(self.x, self.y))
            self.list.pop()

        return score


class Food:
    def __init__(self, snake_list):
        self.color = p.RED
        self.snake_list = snake_list

        self.gen_random_food()

    def gen_random_food(self):
        while True:
            match = False

            x = randint(0, ROWS - 1) * BLOCK_SIZE + MARGIN
            y = randint(0, COLS - 1) * BLOCK_SIZE + MARGIN

            for segment in self.snake_list:
                if x == segment.x and y == segment.y:
                    match = True
                    break

            if not match:
                self.x = x
                self.y = y
                break

    def draw(self):
        p.draw_rectangle_rec((self.x, self.y, BLOCK_SIZE, BLOCK_SIZE), self.color)


class Game:
    def __init__(self):
        self.score = 0
        self.game_over = False

        self.snake = Snake()
        self.food = Food(self.snake.list)

    def draw_grid(self):
        for i in range(ROWS):
            for j in range(COLS):
                x = j * BLOCK_SIZE + MARGIN
                y = i * BLOCK_SIZE + MARGIN

                p.draw_rectangle_lines_ex((x, y, BLOCK_SIZE, BLOCK_SIZE), 1, p.BLACK)

    def draw(self):
        # draw score
        p.draw_text(
            f"Score: {self.score}", p.get_screen_width() // 2 - 70, 30, 30, p.GRAY
        )

        self.draw_grid()
        self.snake.draw()
        self.food.draw()

        if self.game_over:
            p.draw_text(
                "GAME OVER",
                p.get_screen_width() // 2 - 100,
                p.get_screen_height() // 2,
                40,
                p.BLACK,
            )
            p.draw_text("Press ENTER to restart!", 250, 500, 30, p.BLACK)

    def update(self):
        if len(self.snake.list) >= (ROWS * COLS):
            self.game_over = True

        if not self.game_over:
            self.score = self.snake.update(self.food, self.score)

            # snake collision itself
            for i in range(1, len(self.snake.list)):
                if p.check_collision_recs(
                    (
                        self.snake.list[0].x,
                        self.snake.list[0].y,
                        BLOCK_SIZE,
                        BLOCK_SIZE,
                    ),
                    (
                        self.snake.list[i].x,
                        self.snake.list[i].y,
                        BLOCK_SIZE,
                        BLOCK_SIZE,
                    ),
                ):
                    self.game_over = True
        else:
            if p.is_key_pressed(p.KeyboardKey.KEY_ENTER):
                self.score = 0
                self.game_over = False
                self.snake = Snake()
                self.food = Food(self.snake.list)


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
