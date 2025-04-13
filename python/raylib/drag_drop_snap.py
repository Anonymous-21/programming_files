import pyray as p

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Drag, Drop, Snap"
SCREEN_BACKGROUND = p.RAYWHITE

ROWS = 1
COLS = 5
SIZE = 100
GAP = 5


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    item_rect = p.Rectangle(10, 10, 60, 60)
    item_color = p.BLUE
    item_offset = p.Vector2(0, 0)
    item_dragged = False

    inventory = []
    inventory_pos = p.Vector2(100, 200)
    thickness = 5
    outline_color = p.BLACK

    for i in range(ROWS):
        for j in range(COLS):
            x = j * (SIZE + GAP) + inventory_pos.x
            y = i * (SIZE + GAP) + inventory_pos.y

            inventory.append(p.Rectangle(x, y, SIZE, SIZE))

    while not p.window_should_close():
        mouse_pos = p.get_mouse_position()

        if (
            p.is_mouse_button_pressed(p.MouseButton.MOUSE_BUTTON_LEFT)
            and not item_dragged
        ):
            item_dragged = True
            item_color = p.RED
            item_offset = p.Vector2(
                mouse_pos.x - item_rect.x, mouse_pos.y - item_rect.y
            )

        if p.is_mouse_button_released(p.MouseButton.MOUSE_BUTTON_LEFT):
            item_dragged = False
            item_color = p.BLUE

            for slot in inventory:
                if p.check_collision_recs(slot, item_rect):
                    item_rect.x = slot.x + (slot.width - item_rect.width) / 2
                    item_rect.y = slot.y + (slot.height - item_rect.height) / 2

        if item_dragged:
            item_rect.x = mouse_pos.x - item_offset.x
            item_rect.y = mouse_pos.y - item_offset.y

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        for slot in inventory:
            if p.check_collision_recs(item_rect, slot):
                highlight_color = p.YELLOW
            else:
                highlight_color = p.WHITE

            p.draw_rectangle_rec(slot, highlight_color)
            p.draw_rectangle_lines_ex(slot, thickness, outline_color)

        p.draw_rectangle_rec(item_rect, item_color)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
