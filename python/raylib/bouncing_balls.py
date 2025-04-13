import pyray as p

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = ""
SCREEN_BACKGROUND = p.SKYBLUE
NUMBER_OF_BALLS = 200


class Ball:
    def __init__(self):
        self.radius = p.get_random_value(5, 30)
        self.x = p.get_random_value(self.radius, SCREEN_WIDTH - self.radius)
        self.y = p.get_random_value(self.radius, SCREEN_HEIGHT - self.radius)
        self.speed = p.get_random_value(100, 300)
        while True:
            self.direction = p.Vector2(
                p.get_random_value(-1, 1), p.get_random_value(-1, 1)
            )
            if self.direction.x != 0 and self.direction.y != 0:
                break
        self.color = p.Color(
            p.get_random_value(0, 255),
            p.get_random_value(0, 255),
            p.get_random_value(0, 255),
            255,
        )

    def draw(self):
        p.draw_circle_v(p.Vector2(self.x, self.y), self.radius, self.color)

    def update(self):
        # move ball
        self.x += self.direction.x * self.speed * p.get_frame_time()
        self.y += self.direction.y * self.speed * p.get_frame_time()

        if self.x < self.radius or self.x > p.get_screen_width() - self.radius:
            self.direction.x *= -1
        elif self.y < self.radius or self.y > p.get_screen_height() - self.radius:
            self.direction.y *= -1

        self.direction = p.vector2_normalize(self.direction)


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    balls = []

    for i in range(NUMBER_OF_BALLS):
        ball = Ball()
        balls.append(ball)

    while not p.window_should_close():
        for ball in balls:
            ball.update()

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        for ball in balls:
            ball.draw()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
