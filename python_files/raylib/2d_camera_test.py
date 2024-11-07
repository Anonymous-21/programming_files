import pyray as p


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_TITLE = "2D CAMERA TEST"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    background = p.load_texture(
        "/home/anonymous/Downloads/programming_files/assets/tappyplane/PNG/background.png"
    )
    background_width = 800
    background_height = 480

    rect_x = background_width / 2
    rect_y = background_height / 2
    rect_width = 30
    rect_height = 30
    rect_color = p.BLUE
    rect_speed = 5

    camera = p.Camera2D()
    camera.offset = (p.get_screen_width() / 2, p.get_screen_height() / 2)
    camera.rotation = 0
    camera.zoom = 1

    while not p.window_should_close():
        if p.is_key_down(p.KeyboardKey.KEY_LEFT) and rect_x > 0:
            rect_x -= rect_speed
        if (
            p.is_key_down(p.KeyboardKey.KEY_RIGHT)
            and rect_x < background_width - rect_width
        ):
            rect_x += rect_speed
        if p.is_key_down(p.KeyboardKey.KEY_UP) and rect_y > 0:
            rect_y -= rect_speed
        if (
            p.is_key_down(p.KeyboardKey.KEY_DOWN)
            and rect_y < background_height - rect_width
        ):
            rect_y += rect_speed

        camera.target.x = rect_x
        camera.target.y = rect_y

        if camera.target.x <= p.get_screen_width() / 2:
            camera.target.x = p.get_screen_width() / 2
        if camera.target.x >= background_width - p.get_screen_width() / 2:
            camera.target.x = background_width - p.get_screen_width() / 2
        if camera.target.y <= p.get_screen_height() / 2:
            camera.target.y = p.get_screen_height() / 2
        if camera.target.y >= background_height - p.get_screen_height() / 2:
            camera.target.y = background_height - p.get_screen_height() / 2

        p.begin_drawing()
        p.begin_mode_2d(camera)

        p.clear_background(SCREEN_BACKGROUND)

        p.draw_texture(background, 0, 0, p.WHITE)

        p.draw_rectangle_rec((rect_x, rect_y, rect_width, rect_height), rect_color)

        p.end_mode_2d()
        p.end_drawing()

    p.unload_texture(background)
    p.close_window()


if __name__ == "__main__":
    main()
