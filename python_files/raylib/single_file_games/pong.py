import pyray as p
from math import sqrt


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong"
SCREEN_BACKGROUND = p.SKYBLUE
GAME_FPS = 60


class Paddle:
    def __init__(self, x) -> None:
        self.width = 10
        self.height = 100
        self.initial_x = x
        self.initial_y = p.get_screen_height() / 2 - self.height / 2
        self.x = self.initial_x
        self.y = self.initial_y
        self.color = p.BLACK
        self.speed = 5
        self.ai_speed = 7

    def reset(self):
        self.x = self.initial_x
        self.y = self.initial_y

    def draw(self):
        p.draw_rectangle_rec((self.x, self.y, self.width, self.height), self.color)

    def update(self):
        if p.is_key_down(p.KeyboardKey.KEY_W) and self.y >= 0:
            self.y -= self.speed
        elif (
            p.is_key_down(p.KeyboardKey.KEY_S)
            and self.y <= p.get_screen_height() - self.height
        ):
            self.y += self.speed

    def update_ai(self, ball):
        if ball.x > p.get_screen_width() / 2:
            distance_x = ball.x - (self.x + self.width / 2)
            distance_y = ball.y - (self.y + self.height / 2)
            distance = sqrt((distance_x**2) + (distance_y**2))
            if distance > 0:
                distance_y /= distance

                self.y += distance_y * self.ai_speed

        if self.y <= 0:
            self.y = 0
        elif self.y >= p.get_screen_height() - self.height:
            self.y = p.get_screen_height() - self.height


class Ball:
    def __init__(self) -> None:
        self.initial_x = p.get_screen_width() / 2
        self.initial_y = p.get_screen_height() / 2
        self.x = self.initial_x
        self.y = self.initial_y
        self.radius = 10
        self.color = p.RED
        self.initial_speed_x = 4.0
        self.initial_speed_y = 4.0
        self.speed_x = self.initial_speed_x
        self.speed_y = self.initial_speed_y
        self.speed_increment = 0.0005
        self.active = False

    def reset(self):
        self.x = self.initial_x
        self.y = self.initial_y
        self.speed_x = self.initial_speed_x
        self.speed_y = self.initial_speed_y
        self.speed_x *= -1
        self.active = False

    def draw(self):
        p.draw_circle_v((self.x, self.y), self.radius, self.color)

    def update(self):
        if p.is_key_pressed(p.KeyboardKey.KEY_SPACE):
            self.active = True

        if self.active:
            self.x += self.speed_x
            self.y += self.speed_y

            # increment speed
            if self.speed_x > 0:
                self.speed_x += self.speed_increment
            else:
                self.speed_x -= self.speed_increment

            if self.speed_y > 0:
                self.speed_y += self.speed_increment
            else:
                self.speed_y -= self.speed_increment

        if self.y <= self.radius or self.y >= p.get_screen_height() - self.radius:
            self.speed_y *= -1


class Game:
    def __init__(self) -> None:
        self.score_right = 0
        self.score_left = 0

        self.paddle_left = Paddle(10)
        self.ai = Paddle(p.get_screen_width() - self.paddle_left.width - 10)
        self.ball = Ball()

    def reset(self):
        self.ball.reset()
        self.paddle_left.reset()
        self.ai.reset()

    def draw(self):
        # draw scores
        p.draw_text(str(self.score_left), 200, 20, 40, p.BLACK)
        p.draw_text(str(self.score_right), p.get_screen_width() - 220, 20, 40, p.BLACK)

        self.paddle_left.draw()
        self.ai.draw()
        self.ball.draw()

    def update(self):
        self.paddle_left.update()
        self.ai.update_ai(self.ball)
        self.ball.update()

        # update scores
        if self.ball.x < 0:
            self.score_right += 1
            self.reset()
        elif self.ball.x > p.get_screen_width():
            self.score_left += 1
            self.reset()

        # ball collision paddle
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
                self.ai.x,
                self.ai.y,
                self.ai.width,
                self.ai.height,
            ),
        ):
            self.ball.speed_x *= -1


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    game = Game()

    while not p.window_should_close():
        game.update()

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        game.draw()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
