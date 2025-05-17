import pyray as p

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = ""
SCREEN_BACKGROUND: p.Color = p.RAYWHITE


class Item:
    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        self.rect: p.Rectangle = p.Rectangle(x, y, width, height)
        self.color: p.Color = p.Color(
            p.get_random_value(0, 255),
            p.get_random_value(0, 255),
            p.get_random_value(0, 255),
            255,
        )
        self.offset: p.Vector2 = p.Vector2(0, 0)
        self.is_dragging: bool = False

    def draw(self) -> None:
        p.draw_rectangle_rec(self.rect, self.color)


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    item: Item = Item(100, 100, 100, 100)

    while not p.window_should_close():
        mouse_pos: p.Vector2 = p.get_mouse_position()

        if p.check_collision_point_rec(mouse_pos, item.rect):
            if (
                p.is_mouse_button_pressed(p.MouseButton.MOUSE_BUTTON_LEFT)
                and not item.is_dragging
            ):
                item.is_dragging = True
                item.offset.x = mouse_pos.x - item.rect.x
                item.offset.y = mouse_pos.y - item.rect.y

            if item.is_dragging:
                item.rect.x = mouse_pos.x - item.offset.x
                item.rect.y = mouse_pos.y - item.offset.y

            if (
                p.is_mouse_button_released(p.MouseButton.MOUSE_BUTTON_LEFT)
                and item.is_dragging
            ):
                item.is_dragging = False
                item.offset = p.Vector2(0, 0)

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        item.draw()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
