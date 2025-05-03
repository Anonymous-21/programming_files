import pyray as p
from math import copysign

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "4 Sided Platform Collision"
SCREEN_BACKGROUND: p.Color = p.RAYWHITE


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(60)

    width: float = 300.0
    height: float = 150.0
    platform_rect: p.Rectangle = p.Rectangle(
        p.get_screen_width() / 2 - width / 2,
        p.get_screen_height() / 2 - height / 2,
        width,
        height,
    )
    platform_color: p.Color = p.RED

    player_rect: p.Rectangle = p.Rectangle(10, 10, 80, 80)
    player_color: p.Color = p.BLUE
    player_speed: float = 400.0
    player_direction: p.Vector2 = p.Vector2(0, 0)

    while not p.window_should_close():

        # get keyboard input and normalize direction vector
        player_direction.x = float(
            p.is_key_down(p.KeyboardKey.KEY_RIGHT)
            - p.is_key_down(p.KeyboardKey.KEY_LEFT)
        )
        player_direction.y = float(
            p.is_key_down(p.KeyboardKey.KEY_DOWN) - p.is_key_down(p.KeyboardKey.KEY_UP)
        )

        if player_direction.x != 0 and player_direction.y != 0:
            player_direction = p.vector2_normalize(player_direction)

        # move player
        player_rect.x += player_direction.x * player_speed * p.get_frame_time()
        player_rect.y += player_direction.y * player_speed * p.get_frame_time()

        # player bounds
        player_rect.x = max(
            0.0, min(player_rect.x, p.get_screen_width() - player_rect.width)
        )
        player_rect.y = max(
            0.0, min(player_rect.y, p.get_screen_height() - player_rect.height)
        )

        # calculate center of rects
        platform_center: p.Vector2 = p.Vector2(
            platform_rect.x + platform_rect.width / 2,
            platform_rect.y + platform_rect.height / 2,
        )

        player_center: p.Vector2 = p.Vector2(
            player_rect.x + player_rect.width / 2,
            player_rect.y + player_rect.height / 2,
        )

        # current_distance between both rect centers
        current_distance: p.Vector2 = p.vector2_subtract(player_center, platform_center)

        # minimum distance to maintain between both rects
        min_distance: float = p.Vector2(
            platform_rect.width / 2 + player_rect.width / 2 - abs(current_distance.x),
            platform_rect.height / 2 + player_rect.height / 2 - abs(current_distance.y),
        )

        # find out which axis has smaller penetration and resolve that first
        if p.check_collision_recs(player_rect, platform_rect):
            if min_distance.x < min_distance.y:
                player_rect.x += copysign(min_distance.x, current_distance.x)
            else:
                player_rect.y += copysign(min_distance.y, current_distance.y)


        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        p.draw_rectangle_rec(platform_rect, platform_color)

        p.draw_rectangle_rec(player_rect, player_color)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
