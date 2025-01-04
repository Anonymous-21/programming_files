import pyray as p
from math import radians, sin, cos

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 800
SCREEN_TITLE: str = "Radar Sweep"
SCREEN_BACKGROUND: p.Color = p.SKYBLUE
GAME_FPS: int = 60


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    ring_center = p.Vector2(p.get_screen_width() / 2, p.get_screen_height() / 2)
    ring_inner_radius: float = 250
    ring_outer_radius: float = 260
    ring_start_angle: float = 0
    ring_end_angle: float = 360
    ring_segments: int = 64
    ring_color: p.Color = p.BLACK

    line_start_pos: p.Vector2 = ring_center
    line_thickness: float = 10
    line_color: p.Color = p.RED
    
    angle: float = 0

    while not p.window_should_close():

        line_end_pos = p.Vector2(
            ring_inner_radius * cos(radians(angle)) + ring_center.x,
            ring_inner_radius * sin(radians(angle)) + ring_center.y,
        )

        angle += 1
        if angle > 360:
            angle = 0
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
        p.draw_line_ex(line_start_pos, line_end_pos, line_thickness, line_color)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
