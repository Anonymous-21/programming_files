import pyray as p
from enum import Enum
from collections import deque

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 800
SCREEN_TITLE: str = "Snake"
SCREEN_BACKGROUND: p.Color = p.LIGHTGRAY
GAME_FPS: int = 60

ROWS: int = 20
COLS: int = 20
MARGIN: int = 100
BLOCK_WIDTH: int = (SCREEN_WIDTH - MARGIN * 2) / COLS
BLOCK_HEIGHT: int = (SCREEN_HEIGHT - MARGIN * 2) / ROWS


class Direction(Enum):
    right = 0
    left = 1
    up = 2
    down = 3


class Snake:
    def __init__(self) -> None:
        self.x: int = MARGIN
        self.y: int = MARGIN
        self.direction: Direction = Direction.right
        self.list: deque[p.Vector2] = deque([p.Vector2(self.x, self.y)])

        self.last_current_time: float = 0.0
        self.move_interval: float = 0.05

    def draw(self) -> None:
        for i, segment in enumerate(self.list):
            color: p.Color = p.BLUE if i == 0 else p.SKYBLUE

            p.draw_rectangle_rec(
                p.Rectangle(segment.x, segment.y, BLOCK_WIDTH, BLOCK_HEIGHT), color
            )

    def get_user_input(self) -> None:
        if (
            p.is_key_pressed(p.KeyboardKey.KEY_RIGHT)
            and self.direction is not Direction.left
        ):
            self.direction = Direction.right
        if (
            p.is_key_pressed(p.KeyboardKey.KEY_LEFT)
            and self.direction is not Direction.right
        ):
            self.direction = Direction.left
        if (
            p.is_key_pressed(p.KeyboardKey.KEY_UP)
            and self.direction is not Direction.down
        ):
            self.direction = Direction.up
        if (
            p.is_key_pressed(p.KeyboardKey.KEY_DOWN)
            and self.direction is not Direction.up
        ):
            self.direction = Direction.down

    def move(self) -> None:
        match self.direction:
            case Direction.right:
                self.x += BLOCK_WIDTH
            case Direction.left:
                self.x -= BLOCK_WIDTH
            case Direction.up:
                self.y -= BLOCK_HEIGHT
            case Direction.down:
                self.y += BLOCK_HEIGHT

    def update(self) -> bool:
        game_over: bool = False

        self.get_user_input()

        current_time: float = p.get_time()
        if current_time - self.last_current_time > self.move_interval:
            self.last_current_time = current_time

            self.move()
            # collision itself
            for i in range(1, len(self.list)):
                if p.check_collision_recs(
                    p.Rectangle(self.x, self.y, BLOCK_WIDTH, BLOCK_HEIGHT),
                    p.Rectangle(
                        self.list[i].x, self.list[i].y, BLOCK_WIDTH, BLOCK_HEIGHT
                    ),
                ):
                    game_over = True

            # collision walls
            if self.x < MARGIN or self.x > p.get_screen_width() - MARGIN - BLOCK_WIDTH:
                game_over = True
            if (
                self.y < MARGIN
                or self.y > p.get_screen_height() - MARGIN - BLOCK_HEIGHT
            ):
                game_over = True

            self.list.appendleft(p.Vector2(self.x, self.y))
            self.list.pop()

        return game_over


class Food:
    def gen_random_food(self) -> None:
        while True:
            value_in_list: bool = False

            x: int = p.get_random_value(0, COLS - 1) * BLOCK_WIDTH + MARGIN
            y: int = p.get_random_value(0, ROWS - 1) * BLOCK_HEIGHT + MARGIN

            for segment in self.snake.list:
                if x == segment.x and y == segment.y:
                    value_in_list = True
                    break

            if not value_in_list:
                self.x: int = x
                self.y: int = y
                return

    def __init__(self, snake: Snake) -> None:
        self.snake: Snake = snake
        self.gen_random_food()
        self.color: p.Color = p.RED

    def draw(self) -> None:
        p.draw_rectangle_rec(
            p.Rectangle(self.x, self.y, BLOCK_WIDTH, BLOCK_HEIGHT), self.color
        )


class Game:
    def __init__(self) -> None:
        self.score: int = 0
        self.game_over: bool = False

        self.snake: Snake = Snake()
        self.food: Food = Food(self.snake)

    def draw_grid(self) -> None:
        line_thickness: float = 2.0
        line_color: p.Color = p.BLACK

        outline_rect_thickness: float = 5.0
        outline_rect_color: p.Color = p.BLACK

        for i in range(1, COLS):
            x: int = i * BLOCK_WIDTH + MARGIN

            p.draw_line_ex(
                p.Vector2(x, MARGIN),
                p.Vector2(x, p.get_screen_height() - MARGIN),
                line_thickness,
                line_color,
            )

        for i in range(1, ROWS):
            y: int = i * BLOCK_HEIGHT + MARGIN

            p.draw_line_ex(
                p.Vector2(MARGIN, y),
                p.Vector2(p.get_screen_width() - MARGIN, y),
                line_thickness,
                line_color,
            )

        # outline rect
        p.draw_rectangle_lines_ex(
            p.Rectangle(
                MARGIN,
                MARGIN,
                p.get_screen_width() - MARGIN * 2,
                p.get_screen_height() - MARGIN * 2,
            ),
            outline_rect_thickness,
            outline_rect_color,
        )

    def center_and_draw_text(
        self, text: str, font_size: float, rect: p.Rectangle, tint: p.Color
    ) -> None:
        font: p.Font = p.get_font_default()
        text: str = text
        font_size: float = font_size
        text_width: float = p.measure_text(text, int(font_size))
        text_x: float = rect.x + rect.width / 2 - text_width / 2
        text_y: float = rect.y + rect.height / 2 - font_size / 2
        spacing: float = 5.0
        tint: p.Color = tint

        p.draw_text_ex(font, text, p.Vector2(text_x, text_y), font_size, spacing, tint)

    def draw(self) -> None:
        # draw score
        text: str = str(self.score)
        font_size: int = 40
        text_width: int = p.measure_text(text, font_size)
        p.draw_text(
            text, p.get_screen_width() // 2 - text_width // 2, 30, font_size, p.BLACK
        )

        self.snake.draw()
        self.food.draw()
        self.draw_grid()

        if self.game_over:
            self.center_and_draw_text(
                "GAME OVER",
                40,
                p.Rectangle(0, 0, p.get_screen_width(), p.get_screen_height()),
                p.BLACK,
            )

    def update(self) -> None:
        if not self.game_over:
            self.game_over = self.snake.update()

            # snake eating food
            if p.check_collision_recs(
                p.Rectangle(self.food.x, self.food.y, BLOCK_WIDTH, BLOCK_HEIGHT),
                p.Rectangle(
                    self.snake.list[0].x,
                    self.snake.list[0].y,
                    BLOCK_WIDTH,
                    BLOCK_HEIGHT,
                ),
            ):
                last_element: p.Vector2 = p.Vector2(
                    self.snake.list[-1].x, self.snake.list[-1].y
                )
                self.snake.list.append(last_element)
                self.food.gen_random_food()
                self.score += 1
        else:
            if p.is_key_pressed(p.KeyboardKey.KEY_ENTER):
                self.score = 0

                self.snake = Snake()
                self.food = Food(self.snake)

                self.game_over = False


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

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
