import pyray as p

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Breakout"
SCREEN_BACKGROUND = p.RAYWHITE

ROWS = 5
COLS = 10
BLOCK_WIDTH = 79
BLOCK_HEIGHT = 30
GAP = 2


class Bricks:
    def __init__(self):
        self.list = []

        for i in range(ROWS):
            for j in range(COLS):
                x = j * (BLOCK_WIDTH + GAP)
                y = i * (BLOCK_HEIGHT + GAP)

                self.list.append(p.Rectangle(x, y, BLOCK_WIDTH, BLOCK_HEIGHT))

        self.color = p.GRAY

    def draw(self):
        for brick in self.list:
            p.draw_rectangle_rec(brick, self.color)


class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.initial_x = p.get_screen_width() / 2 - self.width / 2
        self.initial_y = p.get_screen_height() - self.height - 10
        self.x = self.initial_x
        self.y = self.initial_y
        self.speed = 300
        self.color = p.BLACK

    def reset(self):
        self.x = self.initial_x
        self.y = self.initial_y

    def draw(self):
        p.draw_rectangle_rec(
            p.Rectangle(self.x, self.y, self.width, self.height), self.color
        )

    def update(self):
        # move paddle
        if p.is_key_down(p.KeyboardKey.KEY_RIGHT):
            self.x += self.speed * p.get_frame_time()
        elif p.is_key_down(p.KeyboardKey.KEY_LEFT):
            self.x -= self.speed * p.get_frame_time()

        # paddle bounds
        self.x = max(0, min(self.x, p.get_screen_width() - self.width))


class Ball:
    def __init__(self, paddle):
        self.paddle = paddle
        self.radius = 10
        self.initial_x = self.paddle.x + self.paddle.width / 2
        self.initial_y = self.paddle.y - self.radius
        self.x = self.initial_x
        self.y = self.initial_y
        self.speed = 400
        self.direction = p.Vector2(1, 1)
        self.color = p.RED
        self.show_text = False
        self.active = False
        self.last_current_time = 0

    def reset(self):
        self.x = self.initial_x
        self.y = self.initial_y
        self.direction.x *= -1
        self.active = False
        self.last_current_time = 0

    def draw(self):
        if self.show_text:
            p.draw_text(
                "Press SPACE to start",
                p.get_screen_width() // 2 - 150,
                p.get_screen_height() // 2 + 100,
                30,
                p.BLACK,
            )

        p.draw_circle_v(p.Vector2(self.x, self.y), self.radius, self.color)

    def update(self):
        # ball activation instructions
        if not self.active:
            # update ball position
            self.x = self.paddle.x + self.paddle.width / 2
            self.y = self.paddle.y - self.radius

            # blinking text
            current_time = p.get_time()
            if current_time - self.last_current_time > 1:
                self.show_text = not self.show_text
                self.last_current_time = current_time

        # activate ball
        if p.is_key_pressed(p.KeyboardKey.KEY_SPACE):
            self.active = True
            self.show_text = False

        # move ball
        if self.active:
            self.x += self.direction.x * self.speed * p.get_frame_time()
            self.y += self.direction.y * self.speed * p.get_frame_time()

        # ball bounds
        if self.x < self.radius or self.x > p.get_screen_width() - self.radius:
            self.direction.x *= -1
        if self.y < self.radius:
            self.direction.y *= -1


class Game:
    def __init__(self):
        self.lives = 5
        self.game_over = False
        self.game_won = False

        self.bricks = Bricks()
        self.paddle = Paddle()
        self.ball = Ball(self.paddle)

    def reset(self):
        self.paddle.reset()
        self.ball.reset()

    def draw(self):
        self.bricks.draw()
        self.paddle.draw()
        self.ball.draw()

        # draw lives
        p.draw_text(str(self.lives), 20, p.get_screen_height() - 50, 40, p.BLACK)

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
        if self.game_won:
            p.draw_text(
                "YOU WIN",
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
        if self.lives <= 0:
            self.game_over = True

        if len(self.bricks.list) <= 0:
            self.game_won = True

        if not self.game_over and not self.game_won:
            self.paddle.update()
            self.ball.update()

            # ball collision paddle
            if p.check_collision_circle_rec(
                p.Vector2(self.ball.x, self.ball.y),
                self.ball.radius,
                p.Rectangle(
                    self.paddle.x, self.paddle.y, self.paddle.width, self.paddle.height
                ),
            ):
                self.ball.direction.y *= -1

            # update lives
            if self.ball.y > p.get_screen_height():
                self.lives -= 1
                self.reset()

            # bricks collision ball
            for brick in self.bricks.list:
                if p.check_collision_circle_rec(
                    p.Vector2(self.ball.x, self.ball.y),
                    self.ball.radius,
                    p.Rectangle(brick.x, brick.y, brick.width, brick.height),
                ):
                    self.ball.direction.y *= -1
                    self.bricks.list.remove(brick)

        else:
            if p.is_key_pressed(p.KeyboardKey.KEY_ENTER):
                self.lives = 5
                self.game_over = False
                self.game_won = False

                self.bricks = Bricks()
                self.paddle = Paddle()
                self.ball = Ball(self.paddle)


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

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
