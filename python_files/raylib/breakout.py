import pyray as p


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Breakout"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60
ROWS = 5
COLS = 10
BLOCK_WIDTH = 79
BLOCK_HEIGHT = 30
BLOCK_GAP = 2


class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.x = p.get_screen_width() / 2 - self.width / 2
        self.y = p.get_screen_height() - 30
        self.color = p.BLACK
        self.speed = 5

    def draw(self):
        p.draw_rectangle_rec((self.x, self.y, self.width, self.height), self.color)

    def update(self):
        if p.is_key_down(p.KeyboardKey.KEY_LEFT) and self.x >= 0:
            self.x -= self.speed
        elif (
            p.is_key_down(p.KeyboardKey.KEY_RIGHT)
            and self.x <= p.get_screen_width() - self.width
        ):
            self.x += self.speed


class Ball:
    def __init__(self):
        self.radius = 10
        self.x = p.get_screen_width() / 2 - self.radius / 2
        self.y = p.get_screen_height() / 2 - self.radius / 2
        self.color = p.BLUE
        self.speed_x = 5
        self.speed_y = 6
        self.active = False

    def draw(self):
        p.draw_circle_v((self.x, self.y), self.radius, self.color)

    def update(self):
        if p.is_key_pressed(p.KeyboardKey.KEY_SPACE):
            self.active = True

        if self.active:
            self.x += self.speed_x
            self.y += self.speed_y

        if self.x <= 0 or self.x >= p.get_screen_width() - self.radius:
            self.speed_x *= -1
        elif self.y <= 0:
            self.speed_y *= -1


class Game:
    def __init__(self):
        self.lives = 5
        self.game_over = False
        self.game_won = False

        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = []

        for i in range(ROWS):
            for j in range(COLS):
                x = j * (BLOCK_WIDTH + BLOCK_GAP)
                y = i * (BLOCK_HEIGHT + BLOCK_GAP)

                self.bricks.append(p.Vector2(x, y))

    def draw(self):
        if not self.ball.active and not self.game_over and not self.game_won:
            p.draw_text("Press SPACE to begin!", 250, 400, 30, p.GRAY)

        # draw lives
        # p.draw_text(str(self.lives), 20, p.get_screen_height() - 30, 30, p.GRAY)
        for i in range(self.lives):
            x = 30 + i * (2 * 10 + 10)
            p.draw_circle(x, p.get_screen_height() - 30, 10, p.RED)

        self.paddle.draw()
        self.ball.draw()

        for brick in self.bricks:
            p.draw_rectangle_rec((brick.x, brick.y, BLOCK_WIDTH, BLOCK_HEIGHT), p.GRAY)

        if self.game_over:
            p.draw_text(
                "GAME OVER",
                p.get_screen_width() // 2 - 100,
                p.get_screen_height() // 2,
                40,
                p.GRAY,
            )
            p.draw_text("Press ENTER to restart!", 250, 400, 30, p.GRAY)
        if self.game_won:
            p.draw_text(
                "YOU WIN",
                p.get_screen_width() // 2 - 70,
                p.get_screen_height() // 2,
                40,
                p.GRAY,
            )
            p.draw_text("Press ENTER to restart!", 250, 400, 30, p.GRAY)

    def update(self):
        if self.lives <= 0:
            self.game_over = True

        if len(self.bricks) <= 0:
            self.game_won = True

        if not self.game_over and not self.game_won:
            self.paddle.update()
            self.ball.update()

            # ball collision paddle
            if p.check_collision_circle_rec(
                (self.ball.x, self.ball.y),
                self.ball.radius,
                (self.paddle.x, self.paddle.y, self.paddle.width, self.paddle.height),
            ):
                self.ball.speed_y *= -1

            # ball collision bricks
            for brick in self.bricks:
                if p.check_collision_circle_rec(
                    (self.ball.x, self.ball.y),
                    self.ball.radius,
                    (brick.x, brick.y, BLOCK_WIDTH, BLOCK_HEIGHT),
                ):
                    self.bricks.remove(brick)
                    self.ball.speed_y *= -1

            # update lives
            if self.ball.y >= p.get_screen_height() - self.ball.radius:
                self.lives -= 1
                self.paddle = Paddle()
                self.ball = Ball()
        else:
            if p.is_key_pressed(p.KeyboardKey.KEY_ENTER):
                self.lives = 5
                self.game_over = False
                self.game_won = False
                self.paddle = Paddle()
                self.ball = Ball()


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
