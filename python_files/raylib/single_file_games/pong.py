import pyray as p


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


class Paddle:
    def __init__(self, x):
        self.width = 10
        self.height = 100
        self.initial_x = x
        self.initial_y = p.get_screen_height() / 2 - self.height / 2
        self.x = self.initial_x
        self.y = self.initial_y
        self.color = p.BLACK
        self.speed = 5

    def reset(self):
        self.x = self.initial_x
        self.y = self.initial_y

    def draw(self):
        p.draw_rectangle_rec((self.x, self.y, self.width, self.height), self.color)

    def update(self, key_up, key_down):
        if p.is_key_down(key_up) and self.y >= 0:
            self.y -= self.speed
        elif p.is_key_down(key_down) and self.y <= p.get_screen_height() - self.height:
            self.y += self.speed


class Ball:
    def __init__(self):
        self.radius = 10
        self.initial_x = p.get_screen_width() / 2
        self.initial_y = p.get_screen_height() / 2
        self.x = self.initial_x
        self.y = self.initial_y
        self.color = p.RED
        self.speed_x = 5
        self.speed_y = 6
        self.frames_counter = 0

    def reset(self):
        self.x = self.initial_x
        self.y = self.initial_y
        self.speed_x *= -1
        self.frames_counter = 0

    def draw(self):
        p.draw_circle_v((self.x, self.y), self.radius, self.color)

    def update(self, paddle_left, paddle_right, left_score, right_score):
        self.frames_counter += 1
        if self.frames_counter >= 60:
            self.frames_counter = 61

            self.x += self.speed_x
            self.y += self.speed_y

        if self.x <= self.radius:
            self.reset()
            paddle_left.reset()
            paddle_right.reset()
            right_score += 1
        elif self.x >= p.get_screen_width() - self.radius:
            self.reset()
            paddle_left.reset()
            paddle_right.reset()
            left_score += 1

        if self.y <= self.radius or self.y >= p.get_screen_height() - self.radius:
            self.speed_y *= -1

        return (left_score, right_score)


class Game:
    def __init__(self):
        self.left_score = 0
        self.right_score = 0

        self.paddle_left = Paddle(10)
        self.paddle_right = Paddle(p.get_screen_width() - self.paddle_left.width - 10)
        self.ball = Ball()

    def draw(self):
        # draw screen divider
        p.draw_line_ex(
            (p.get_screen_width() / 2, 0),
            (p.get_screen_width() / 2, p.get_screen_height()),
            5,
            p.GRAY,
        )

        # draw scores
        p.draw_text(
            str(self.left_score), p.get_screen_width() // 2 - 70, 20, 30, p.GRAY
        )
        p.draw_text(
            str(self.right_score), p.get_screen_width() // 2 + 50, 20, 30, p.GRAY
        )

        self.paddle_left.draw()
        self.paddle_right.draw()
        self.ball.draw()

    def update(self):
        self.paddle_left.update(p.KeyboardKey.KEY_W, p.KeyboardKey.KEY_S)
        self.paddle_right.update(p.KEY_UP, p.KEY_DOWN)
        self.left_score, self.right_score = self.ball.update(
            self.paddle_left, self.paddle_right, self.left_score, self.right_score
        )

        # paddle collision ball
        if p.check_collision_circle_rec(
            (self.ball.x, self.ball.y),
            self.ball.radius,
            (
                self.paddle_left.x,
                self.paddle_left.y,
                self.paddle_left.width,
                self.paddle_left.height,
            ),
        ):
            self.ball.speed_x *= -1
        elif p.check_collision_circle_rec(
            (self.ball.x, self.ball.y),
            self.ball.radius,
            (
                self.paddle_right.x,
                self.paddle_right.y,
                self.paddle_right.width,
                self.paddle_right.height,
            ),
        ):
            self.ball.speed_x *= -1


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

# %%
