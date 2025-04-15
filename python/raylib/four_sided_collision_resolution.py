import pyray as p
from dataclasses import dataclass
from math import copysign

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Four Side Collision And Resolutions"
SCREEN_BACKGROUND: p.Color = p.RAYWHITE


@dataclass
class Item:
    rect: p.Rectangle
    color: p.Color
    speed: float
    direction: p.Vector2
    center: p.Vector2


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    item1: Item = Item(
        rect=p.Rectangle(10, 10, 50, 50),
        color=p.BLUE,
        speed=300.0,
        direction=p.Vector2(0, 0),
        center=p.Vector2(0, 0),
    )

    item2: Item = Item(
        rect=p.Rectangle(
            p.get_screen_width() / 2 - 150, p.get_screen_height() / 2 - 150, 300, 300
        ),
        color=p.GREEN,
        speed=300.0,
        direction=p.Vector2(0, 0),
        center=p.Vector2(0, 0),
    )

    while not p.window_should_close():
        # update centers
        item1.center.x = item1.rect.x + item1.rect.width / 2
        item1.center.y = item1.rect.y + item1.rect.height / 2

        item2.center.x = item2.rect.x + item2.rect.width / 2
        item2.center.y = item2.rect.y + item2.rect.height / 2

        # get direction and move item
        item1.direction.x = int(p.is_key_down(p.KeyboardKey.KEY_RIGHT)) - int(
            p.is_key_down(p.KeyboardKey.KEY_LEFT)
        )
        item1.direction.y = int(p.is_key_down(p.KeyboardKey.KEY_DOWN)) - int(
            p.is_key_down(p.KeyboardKey.KEY_UP)
        )

        if item1.direction.x != 0 and item1.direction.y != 0:
            item1.direction = p.vector2_normalize(item1.direction)

        item1.rect.x += item1.direction.x * item1.speed * p.get_frame_time()
        item1.rect.y += item1.direction.y * item1.speed * p.get_frame_time()

        # collision and resolution
        if p.check_collision_recs(item1.rect, item2.rect):
            # current distance between rect centers
            current_distance: p.Vector2 = p.vector2_subtract(item1.center, item2.center)

            # minimum required/set distance
            min_distance: p.Vector2 = p.Vector2(
                item1.rect.width / 2 + item2.rect.width / 2,
                item1.rect.height / 2 + item2.rect.height / 2,
            )

            # calculate overlap/penetration
            overlap: p.Vector2 = p.Vector2(
                min_distance.x - abs(current_distance.x),
                min_distance.y - abs(current_distance.y),
            )

            # set position x, y of item
            if overlap.x < overlap.y:
                item1.rect.x += copysign(overlap.x, current_distance.x)
            else:
                item1.rect.y += copysign(overlap.y, current_distance.y)

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        p.draw_rectangle_rec(item2.rect, item2.color)

        item1.color = (
            p.RED if p.check_collision_recs(item1.rect, item2.rect) else p.BLUE
        )

        p.draw_rectangle_rec(item1.rect, item1.color)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
