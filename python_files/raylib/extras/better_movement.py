import pyray as p
from math import sqrt

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Diagonal Movement Test"
SCREEN_BACKGROUND: p.Color = p.RAYWHITE
GAME_FPS: int = 60


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    rect = p.Rectangle(0, 0, 40, 40)
    rect_color: p.Color = p.BLUE
    rect_speed: float = 300
    rect_direction = p.Vector2(0, 0)

    while not p.window_should_close():
        rect_direction.x = int(p.is_key_down(p.KeyboardKey.KEY_RIGHT)) - int(
            p.is_key_down(p.KeyboardKey.KEY_LEFT)
        )
        rect_direction.y = int(p.is_key_down(p.KeyboardKey.KEY_DOWN)) - int(
            p.is_key_down(p.KeyboardKey.KEY_UP)
        )
        # rect_direction: p.Vector2 = p.vector2_normalize(rect_direction)
        direction = sqrt(rect_direction.x ** 2 + rect_direction.y ** 2)
        if direction != 0:
            rect_direction.x /= direction
            rect_direction.y /= direction

        dt: float = p.get_frame_time()
        rect.x += rect_speed * rect_direction.x * dt
        rect.y += rect_speed * rect_direction.y * dt

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        p.draw_rectangle_rec(rect, rect_color)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
