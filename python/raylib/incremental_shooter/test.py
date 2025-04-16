import pyray as p
from math import atan2, degrees

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = ""
SCREEN_BACKGROUND: p.Color = p.RAYWHITE


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    rect: p.Rectangle = p.Rectangle(
        p.get_screen_width() / 2, p.get_screen_height() / 2, 20, 50
    )
    color: p.Color = p.BLACK
    origin: p.Vector2 = p.Vector2(rect.width / 2, 0)

    while not p.window_should_close():
        mouse_pos: p.Vector2 = p.get_mouse_position()

        dx: float = mouse_pos.x - origin.x
        dy: float = mouse_pos.y - origin.y

        angle_rad: float = atan2(dy, dx)
        angle_deg: float = degrees(angle_rad)

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        p.draw_rectangle_pro(rect, origin, angle_deg, color)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
