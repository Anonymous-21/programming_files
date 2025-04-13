import pyray as p

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong"
SCREEN_BACKGROUND = p.SKYBLUE


class Ball:
    def __init__(self):
        self.initial_x = p.get_screen_width() / 2
        self.initial_y = p.get_screen_height() / 2
        self.x = self.initial_x
        self.y = self.initial_y
        self.radius = 10
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
        # ball activation text
        if not self.active:
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
        if self.y < self.radius or self.y > p.get_screen_height() - self.radius:
            self.direction.y *= -1

        # normalize direction
        self.direction = p.vector2_normalize(self.direction)


class Paddle:
    def __init__(self, x):
        self.width = 10
        self.height = 100
        self.initial_x = x
        self.initial_y = p.get_screen_height() / 2 - self.height / 2
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

    def update_player(self):
        # get input and move paddle
        if p.is_key_down(p.KeyboardKey.KEY_UP):
            self.y -= self.speed * p.get_frame_time()
        elif p.is_key_down(p.KeyboardKey.KEY_DOWN):
            self.y += self.speed * p.get_frame_time()

        # paddle bounds
        self.y = max(0, min(self.y, p.get_screen_height() - self.height))

    def update_ai(self, ball):
        # move paddle
        if ball.y > self.y + self.height / 2:
            self.y += self.speed * p.get_frame_time()
        elif ball.y < self.y + self.height / 2:
            self.y -= self.speed * p.get_frame_time()

        # paddle bounds
        self.y = max(0, min(self.y, p.get_screen_height() - self.height))


class Game:
    def __init__(self):
        self.score_left = 0
        self.score_right = 0

        self.ball = Ball()
        self.player = Paddle(10)
        self.ai = Paddle(p.get_screen_width() - self.player.width - 10)

    def reset(self):
        self.ball.reset()
        self.player.reset()
        self.ai.reset()

    def draw(self):
        # draw scores
        p.draw_text(str(self.score_left), 200, 30, 40, p.BLACK)
        p.draw_text(str(self.score_right), p.get_screen_width() - 200, 30, 40, p.BLACK)

        self.ball.draw()
        self.player.draw()
        self.ai.draw()

    def update(self):
        self.ball.update()
        self.player.update_player()
        self.ai.update_ai(self.ball)

        # ball collision paddle
        if p.check_collision_circle_rec(
            p.Vector2(self.ball.x, self.ball.y),
            self.ball.radius,
            p.Rectangle(
                self.player.x, self.player.y, self.player.width, self.player.height
            ),
        ):
            self.ball.direction.x *= -1
        if p.check_collision_circle_rec(
            p.Vector2(self.ball.x, self.ball.y),
            self.ball.radius,
            p.Rectangle(self.ai.x, self.ai.y, self.ai.width, self.ai.height),
        ):
            self.ball.direction.x *= -1

        # update scores
        if self.ball.x < self.ball.radius:
            self.score_right += 1
            self.reset()
        elif self.ball.x > p.get_screen_width() - self.ball.radius:
            self.score_left += 1
            self.reset()


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
