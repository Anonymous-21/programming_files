import pyray as p
from math import cos, sin, radians

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Radar Sweep"
SCREEN_BACKGROUND: p.Color = p.RAYWHITE


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    ring_center: p.Vector2 = p.Vector2(
        p.get_screen_width() / 2, p.get_screen_height() / 2
    )
    ring_inner_radius: float = 250.0
    ring_outer_radius: float = 260.0
    ring_start_angle: float = 0
    ring_end_angle: float = 360
    ring_segments: int = 64
    ring_color: p.Color = p.RED

    line_start: p.Vector2 = ring_center
    line_end: p.Vector2 = p.Vector2(0, 0)
    line_thickness: float = 5.0
    line_color: p.Color = p.DARKGREEN

    angle: float = 0.0
    sweep_speed: float = 100.0

    while not p.window_should_close():
        angle += sweep_speed * p.get_frame_time()
        if angle > 360:
            angle = 0

        line_end.x = ring_center.x + ring_inner_radius * cos(radians(angle))
        line_end.y = ring_center.y + ring_inner_radius * sin(radians(angle))

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        p.draw_ring(
            ring_center,
            ring_inner_radius,
            ring_outer_radius,
            ring_start_angle,
            ring_end_angle,
            ring_segments,
            ring_color,
        )

        p.draw_line_ex(line_start, line_end, line_thickness, line_color)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
