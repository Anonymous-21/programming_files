import pyray as p
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Random Walker"
SCREEN_BACKGROUND = p.BLACK
GAME_FPS = 60


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    width = 6
    height = 6
    color = p.WHITE

    lst = [p.Vector2(p.get_screen_width() / 2, p.get_screen_height() / 2)]

    active = True

    while not p.window_should_close():
        if p.is_key_pressed(p.KeyboardKey.KEY_SPACE):
            if active:
                active = False
            elif not active:
                active = True

        if active:
            pos = p.Vector2(lst[-1].x, lst[-1].y)
            choice = random.randint(1, 4)

            if choice == 1:
                pos.x += width
            elif choice == 2:
                pos.x -= width
            elif choice == 3:
                pos.y += width
            elif choice == 4:
                pos.y -= width

            if pos.x <= 0:
                pos.x = 0
            elif pos.x >= p.get_screen_width() - width:
                pos.x = p.get_screen_width() - width
            elif pos.y <= 0:
                pos.y = 0
            elif pos.y >= p.get_screen_height() - height:
                pos.y = p.get_screen_height() - height

            lst.append(pos)

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        for i in lst:
            p.draw_rectangle_rec((i.x, i.y, width, height), color)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
