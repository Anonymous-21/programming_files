import pyray as p

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Centered Text"
SCREEN_BACKGROUND: p.Color = p.RAYWHITE


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    width: float = 100.0
    height: float = width
    rect: p.Rectangle = p.Rectangle(
        p.get_screen_width() / 2 - width / 2,
        p.get_screen_height() / 2 - height / 2,
        width,
        height,
    )
    color: p.Color = p.BLACK
    thickness: float = 5.0

    count: int = 0

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        if p.is_key_pressed(p.KeyboardKey.KEY_UP):
            count += 1
        elif p.is_key_pressed(p.KeyboardKey.KEY_DOWN):
            count -= 1

        text: str = str(count)
        font_size: int = 40
        text_width: float = p.measure_text(text, font_size)
        text_x: int = int(rect.x + rect.width / 2 - text_width / 2)
        text_y: int = int(rect.y + rect.height / 2 - font_size / 2)

        p.draw_rectangle_lines_ex(rect, thickness, color)

        p.draw_text(text, text_x, text_y, font_size, color)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
