import pyray as p

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Centered Text"
SCREEN_BACKGROUND: p.Color = p.RAYWHITE
GAME_FPS: int = 60


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    width: float = 400.0
    height: float = 200.0
    rect: p.Rectangle = p.Rectangle(
        p.get_screen_width() / 2 - width / 2,
        p.get_screen_height() / 2 - height / 2,
        width,
        height,
    )

    num: int = 0

    while not p.window_should_close():
        if p.is_key_pressed(p.KeyboardKey.KEY_UP):
            num += 1
        if p.is_key_pressed(p.KeyboardKey.KEY_DOWN):
            num -= 1

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        p.draw_rectangle_lines_ex(rect, 5.0, p.BLACK)

        text: str = str(num)
        font_size: float = 40.0
        text_width: float = p.measure_text(text, int(font_size))
        text_x: float = rect.x + rect.width / 2 - text_width / 2
        text_y: float = rect.y + rect.height / 2 - font_size / 2
        spacing: float = 7.0
        tint: p.Color = p.BLACK

        p.draw_text_ex(
            p.get_font_default(),
            text,
            p.Vector2(text_x, text_y),
            font_size,
            spacing,
            tint,
        )

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
