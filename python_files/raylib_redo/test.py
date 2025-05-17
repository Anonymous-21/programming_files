import pyray as p
from dataclasses import dataclass

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = ""
SCREEN_BACKGROUND: p.Color = p.RAYWHITE


@dataclass
class Item:
    rect: p.Rectangle
    color: p.Color
    offset: p.Vector2
    is_dragging: bool


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    source_rect: p.Rectangle = p.Rectangle(100, 100, 200, 200)
    source_rect_color: p.Color = p.LIGHTGRAY

    area_list: list[Item] = []

    while not p.window_should_close():
        mouse_pos: p.Vector2 = p.get_mouse_position()

        if p.check_collision_point_rec(mouse_pos, source_rect):
            if p.is_mouse_button_pressed(p.MouseButton.MOUSE_BUTTON_LEFT):
                width: float = 50.0
                height: float = 50.0
                rect: p.Rectangle = p.Rectangle(
                    mouse_pos.x - width / 2, mouse_pos.y - height / 2, width, height
                )
                color: p.Color = p.Color(
                    p.get_random_value(0, 255),
                    p.get_random_value(0, 255),
                    p.get_random_value(0, 255),
                    255,
                )
                offset: p.Vector2 = p.Vector2(0, 0)
                is_dragging: bool = False
                item: Item = Item(rect, color, offset, is_dragging)

                area_list.append(item)

        for item in area_list:
            if p.check_collision_point_rec(mouse_pos, item.rect):
                if p.is_mouse_button_pressed(p.MouseButton.MOUSE_BUTTON_LEFT):
                    item.is_dragging = True
                    item.offset.x = mouse_pos.x - item.rect.x
                    item.offset.y = mouse_pos.y - item.rect.y

                if p.is_mouse_button_down(p.MouseButton.MOUSE_BUTTON_LEFT):
                    item.rect.x += item.offset.x * p.get_frame_time()
                    item.rect.y += item.offset.y * p.get_frame_time()

                if p.is_mouse_button_released(p.MouseButton.MOUSE_BUTTON_LEFT):
                    item.is_dragging = False
                    item.offset = p.Vector2(0, 0)

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        p.draw_rectangle_rec(source_rect, source_rect_color)

        for item in area_list:
            p.draw_rectangle_rec(item.rect, item.color)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
