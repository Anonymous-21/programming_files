import pyray as p
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move Angle"
SCREEN_BACKGROUND: p.Color = p.RAYWHITE
GAME_FPS = 60


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    player = p.load_texture(
        "/home/anonymous/Downloads/programming_files/assets/kenny_space_shooter_redux/PNG/playerShip1_red.png"
    )
    width = player.width
    height = player.height

    source = p.Rectangle(0, 0, width, height)
    dest = p.Rectangle(
        p.get_screen_width() / 2, p.get_screen_height() / 2, width, height
    )
    origin = p.Vector2(width / 2, height / 2)
    rotation = 0
    speed = 5

    while not p.window_should_close():
        if p.is_key_down(p.KeyboardKey.KEY_LEFT):
            rotation -= 3
        elif p.is_key_down(p.KeyboardKey.KEY_RIGHT):
            rotation += 3

        if p.is_key_down(p.KeyboardKey.KEY_UP):
            dest.x += math.cos(math.radians(rotation - 90)) * speed
            dest.y += math.sin(math.radians(rotation - 90)) * speed

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        p.draw_texture_pro(player, source, dest, origin, rotation, p.WHITE)
        p.draw_circle_v((dest.x, dest.y), 5, p.ORANGE)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
