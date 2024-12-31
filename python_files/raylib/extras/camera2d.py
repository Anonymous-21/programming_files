import pyray as p
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = ""
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    background = p.load_texture(
        "/home/anonymous/Downloads/programming_files/python_files/raylib/simple_space_survival/assets/background.png"
    )
    player = p.load_texture(
        "/home/anonymous/Downloads/programming_files/assets/kenny_simple_space/PNG/Default/ship_A.png"
    )
    source = p.Rectangle(0, 0, player.width, player.height)
    dest = p.Rectangle(
        background.width / 2, background.height / 2, player.width, player.height
    )
    origin = (dest.width / 2, dest.height / 2)
    rotation = 0
    tint = p.WHITE
    speed = 5

    camera = p.Camera2D()
    camera.rotation = 0
    camera.zoom = 1

    while not p.window_should_close():
        camera.target = p.Vector2(dest.x, dest.y)
        camera.offset = p.Vector2(p.get_screen_width() / 2, p.get_screen_height() / 2)

        camera.target.x = max(
            p.get_screen_width() / 2,
            min(dest.x, background.width - p.get_screen_width() / 2),
        )
        camera.target.y = max(
            p.get_screen_height() / 2,
            min(dest.y, background.height - p.get_screen_height() / 2),
        )

        if p.is_key_down(p.KeyboardKey.KEY_W):
            dest.y -= speed
        if p.is_key_down(p.KeyboardKey.KEY_S):
            dest.y += speed
        if p.is_key_down(p.KeyboardKey.KEY_A):
            dest.x -= speed
        if p.is_key_down(p.KeyboardKey.KEY_D):
            dest.x += speed

        # player boundary checks
        dest.x = max(0, min(dest.x, background.width - dest.width))
        dest.y = max(0, min(dest.y, background.height - dest.height))

        # mouse position according to world space (background)
        mouse_x = p.get_mouse_x() - p.get_screen_width() / 2 + camera.target.x
        mouse_y = p.get_mouse_y() - p.get_screen_height() / 2 + camera.target.y

        # player rotation
        dx = mouse_x - dest.x
        dy = mouse_y - dest.y
        rotation = math.degrees(math.atan2(dy, dx))
        rotation += 90

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)
        p.begin_mode_2d(camera)

        p.draw_texture(background, 0, 0, p.WHITE)
        p.draw_texture_pro(player, source, dest, origin, rotation, tint)

        p.end_mode_2d()
        p.end_drawing()

    p.unload_texture(background)
    p.close_window()


if __name__ == "__main__":
    main()
