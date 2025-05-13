import pyray as p

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Blinking Text"
SCREEN_BACKGROUND: p.Color = p.RAYWHITE


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    active: bool = False
    last_current_time: float = 0.0

    while not p.window_should_close():
        current_time: float = p.get_time()
        if current_time - last_current_time > 1:
            active = not active
            last_current_time = current_time

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        if active:
            p.draw_text(
                "Test",
                p.get_screen_width() // 2,
                p.get_screen_height() // 2,
                40,
                p.BLACK,
            )

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
