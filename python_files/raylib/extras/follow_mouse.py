import pyray as p
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Follow Mouse"
SCREEN_BACKGROUND = p.BLACK
GAME_FPS = 60


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    player = p.load_texture(
        "/home/anonymous/Downloads/programming_files/assets/kenny_simple_space/PNG/Default/ship_A.png"
    )
    source = p.Rectangle(0, 0, player.width, player.height)
    dest = p.Rectangle(0, 0, player.width, player.height)
    origin = p.Vector2(dest.width / 2, dest.height / 2)
    rotation = 0
    tint = p.WHITE
    speed = 5

    while not p.window_should_close():
        mouse_pos = p.get_mouse_position()

        # rotation
        dx = mouse_pos.x - (dest.x + dest.width / 2)
        dy = mouse_pos.y - (dest.y + dest.height / 2)
        rotation = math.degrees(math.atan2(dy, dx))
        rotation += 90

        # movement towards mouse
        distance = math.sqrt((dx**2) + (dy**2))
        if distance > 0:
            dx /= distance
            dy /= distance

            dest.x += dx * speed
            dest.y += dy * speed

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        p.draw_texture_pro(player, source, dest, origin, rotation, tint)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
