import pyray as p

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = ""
SCREEN_BACKGROUND: p.Color = p.RAYWHITE


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    ball_pos: p.Vector2 = p.Vector2(100, 100)
    ball_radius: float = 20.0
    ball_color: p.Color = p.RED
    ball_direction: p.Vector2 = p.Vector2(1, 1)
    ball_speed: float = 400.0

    while not p.window_should_close():
        if abs(ball_pos.x) > 0.01 and abs(ball_pos.y) > 0.01:
            ball_direction = p.vector2_normalize(ball_direction)

        # move ball
        ball_pos.x += ball_direction.x * ball_speed * p.get_frame_time()
        ball_pos.y += ball_direction.y * ball_speed * p.get_frame_time()

        # ball bounds
        if ball_pos.x < ball_radius or ball_pos.x > p.get_screen_width() - ball_radius:
            ball_direction.x *= -1
        if ball_pos.y < ball_radius or ball_pos.y > p.get_screen_height() - ball_radius:
            ball_direction.y *= -1

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        p.draw_circle_v(ball_pos, ball_radius, ball_color)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
