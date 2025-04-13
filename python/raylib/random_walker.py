import pyray as p
from random import choice

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Random Walker"
SCREEN_BACKGROUND: p.Color = p.RAYWHITE


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(60)

    x: float = p.get_screen_width() / 2
    y: float = p.get_screen_height() / 2

    size: float = 5.0

    trail: list[p.Vector2] = [p.Vector2(x, y)]

    while not p.window_should_close():
        direction: str = choice(["up", "down", "left", "right"])

        match direction:
            case "right":
                x += size
            case "left":
                x -= size
            case "up":
                y -= size
            case "down":
                y += size

        x = max(0, min(x, p.get_screen_width() - size))
        y = max(0, min(y, p.get_render_height() - size))

        trail.append(p.Vector2(x, y))

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        for pos in trail:
            p.draw_rectangle_rec(
                p.Rectangle(pos.x, pos.y, size, size),
                p.BLACK,
            )

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
