import pyray as p


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Tetris"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    size = 40
    x = size * 2
    y = size * 2

    color = p.YELLOW

    shape_list = {
        "O": [
            p.Vector2(x, y),
            p.Vector2(x + size, y),
            p.Vector2(x, y + size),
            p.Vector2(x + size, y + size),
        ],
        "I": [
            p.Vector2(x, y),
            p.Vector2(x, y + size),
            p.Vector2(x, y + size * 2),
            p.Vector2(x, y + size * 3),
        ],
        "S": [
            p.Vector2(x, y),
            p.Vector2(x + size, y),
            p.Vector2(x, y + size),
            p.Vector2(x - size, y + size),
        ],
        "Z": [
            p.Vector2(x, y),
            p.Vector2(x + size, y),
            p.Vector2(x + size, y + size),
            p.Vector2(x + size * 2, y + size),
        ],
        "L": [
            p.Vector2(x, y),
            p.Vector2(x, y + size),
            p.Vector2(x, y + size * 2),
            p.Vector2(x + size, y + size * 2),
        ],
        "J": [
            p.Vector2(x, y),
            p.Vector2(x, y + size),
            p.Vector2(x, y + size * 2),
            p.Vector2(x - size, y + size * 2),
        ],
        "T": [
            p.Vector2(x, y),
            p.Vector2(x + size, y),
            p.Vector2(x + size * 2, y),
            p.Vector2(x + size, y + size),
        ],
    }

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
