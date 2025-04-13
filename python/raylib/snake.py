import pyray as p

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Snake"
SCREEN_BACKGROUND = p.SKYBLUE

SIZE = 20


class Snake:
    def __init__(self):
        self.x = p.get_screen_width() / 2
        self.y = p.get_screen_height() / 2
        self.list = [p.Vector2(self.x, self.y)]
        self.color = p.DARKGREEN
        self.direction = None
        self.last_current_time = 0
        self.move_interval = 0.07

    def draw(self):
        for segment in self.list:
            p.draw_rectangle_rec(
                p.Rectangle(segment.x, segment.y, SIZE, SIZE), self.color
            )

    def update(self, food, score):
        # get direction input
        if p.is_key_pressed(p.KeyboardKey.KEY_RIGHT) and self.direction != "left":
            self.direction = "right"
        if p.is_key_pressed(p.KeyboardKey.KEY_LEFT) and self.direction != "right":
            self.direction = "left"
        if p.is_key_pressed(p.KeyboardKey.KEY_DOWN) and self.direction != "up":
            self.direction = "down"
        if p.is_key_pressed(p.KeyboardKey.KEY_UP) and self.direction != "down":
            self.direction = "up"

        if p.get_time() - self.last_current_time > self.move_interval:
            self.last_current_time = p.get_time()

            match self.direction:
                case "right":
                    self.x += SIZE
                case "left":
                    self.x -= SIZE
                case "up":
                    self.y -= SIZE
                case "down":
                    self.y += SIZE

            # snake eating food
            if p.check_collision_recs(
                p.Rectangle(self.x, self.y, SIZE, SIZE),
                p.Rectangle(food.x, food.y, SIZE, SIZE),
            ):
                food.gen_random_food()
                self.list.append(self.list[-1])
                score += 1

            self.list.insert(0, p.Vector2(self.x, self.y))
            self.list.pop()

        return score


class Food:
    def __init__(self, snake):
        self.snake = snake
        self.gen_random_food()
        self.color = p.RED

    def gen_random_food(self):
        while True:
            in_list = False

            x = p.get_random_value(0, p.get_screen_width() // SIZE - 1) * SIZE
            y = p.get_random_value(0, p.get_screen_height() // SIZE - 1) * SIZE

            for segment in self.snake.list:
                if segment.x == x and segment.y == y:
                    in_list = True
                    break

            if not in_list:
                self.x = x
                self.y = y
                break

    def draw(self):
        p.draw_rectangle_rec(p.Rectangle(self.x, self.y, SIZE, SIZE), self.color)


class Game:
    def __init__(self):
        self.score = 0
        self.game_over = False

        self.snake = Snake()
        self.food = Food(self.snake)

    def draw(self):
        self.snake.draw()
        self.food.draw()

        p.draw_text(f"Score: {self.score}", 10, 10, 30, p.BLACK)

        if self.game_over:
            p.draw_text(
                "GAME OVER",
                p.get_screen_width() // 2 - 100,
                p.get_screen_height() // 2,
                40,
                p.BLACK,
            )
            p.draw_text(
                "Press ENTER to restart",
                p.get_screen_width() // 2 - 150,
                p.get_screen_height() // 2 + 100,
                30,
                p.BLACK,
            )

    def update(self):
        if not self.game_over:
            self.score = self.snake.update(self.food, self.score)

            # snake collision walls
            if self.snake.list[0].x < 0 or self.snake.list[0].x > p.get_screen_width():
                self.game_over = True
            if self.snake.list[0].y < 0 or self.snake.list[0].y > p.get_screen_height():
                self.game_over = True

            # snake collision itself
            for i in range(1, len(self.snake.list)):
                if p.check_collision_recs(
                    p.Rectangle(self.snake.list[0].x, self.snake.list[0].y, SIZE, SIZE),
                    p.Rectangle(self.snake.list[i].x, self.snake.list[i].y, SIZE, SIZE),
                ):
                    self.game_over = True
        else:
            if p.is_key_pressed(p.KeyboardKey.KEY_ENTER):
                self.score = 0
                self.game_over = False

                self.snake = Snake()
                self.food = Food(self.snake)


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(60)

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
