import pyray as p
from dataclasses import dataclass

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Inventory"
SCREEN_BACKGROUND: p.Color = p.RAYWHITE

ROWS: int = 5
COLS: int = 5
SLOT_SIZE: int = 80
SLOT_GAP: int = 3

NUM_OF_ITEMS: int = 3


@dataclass
class Item:
    id: int
    rect: p.Rectangle
    color: p.Color
    offset: p.Vector2
    dragging: bool
    quantity: int


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    pos: p.Vector2 = p.Vector2(10, 10)

    slots: list[p.Rectangle] = []
    for i in range(ROWS):
        for j in range(COLS):
            x: int = j * (SLOT_SIZE + SLOT_GAP) + pos.x
            y: int = i * (SLOT_SIZE + SLOT_GAP) + pos.y

            slots.append(p.Rectangle(x, y, SLOT_SIZE, SLOT_SIZE))

    inventory: list[Item] = []
    inventory_active: bool = True

    items: list[Item] = []
    for i in range(NUM_OF_ITEMS):
        item: Item = Item(
            id=(i + 1),
            rect=p.Rectangle(600, (i + 1) * 80, 50, 50),
            color=p.Color(
                p.get_random_value(0, 255),
                p.get_random_value(0, 255),
                p.get_random_value(0, 255),
                255,
            ),
            dragging=False,
            quantity=1,
            offset=p.Vector2(0, 0),
        )

        items.append(item)

        last_current_time: float = 0.0
        print_interval: float = 1.0

    while not p.window_should_close():
        # activate/deactivate inventory
        if p.is_key_pressed(p.KeyboardKey.KEY_I):
            inventory_active = not inventory_active

        mouse_pos: p.Vector2 = p.get_mouse_position()

        # activate item dragging
        for item in items:
            if p.is_mouse_button_pressed(p.MouseButton.MOUSE_BUTTON_LEFT):
                if (
                    p.check_collision_point_rec(mouse_pos, item.rect)
                    and not item.dragging
                ):
                    item.dragging = True
                    item.offset.x = mouse_pos.x - item.rect.x
                    item.offset.y = mouse_pos.y - item.rect.y

        for item in inventory[:]:
            if p.is_mouse_button_pressed(p.MouseButton.MOUSE_BUTTON_LEFT):
                if p.check_collision_point_rec(mouse_pos, item.rect) and not item.dragging:
                    item.dragging = True
                    item.offset.x = mouse_pos.x - item.rect.x
                    item.offset.y = mouse_pos.y - item.rect.y

                    inventory.remove(item)
                    items.append(item)

        # handle dragging
        for item in items[:]:
            if item.dragging:
                item.rect.x = mouse_pos.x - item.offset.x
                item.rect.y = mouse_pos.y - item.offset.y

                if p.is_mouse_button_released(p.MouseButton.MOUSE_BUTTON_LEFT):
                    item.dragging = False

                    # snap item to slot
                    for slot in slots:
                        if p.check_collision_recs(slot, item.rect):
                            item.rect.x = slot.x + (slot.width - item.rect.width) / 2
                            item.rect.y = slot.y + (slot.height - item.rect.height) / 2

                            inventory.append(item)
                            if item in items:
                                items.remove(item)

        # debug prints
        current_time: float = p.get_time()
        if current_time - last_current_time > print_interval:
            last_current_time = current_time
            print()
            print(f"Time: {last_current_time}")
            print()
            print("========== Items ===============")
            for item in items:
                print(f"id: {item.id}; x: {item.rect.x}; y: {item.rect.y}")
            print()
            print("========== Inventory ===============")
            for item in inventory:
                print(f"id: {item.id}; x: {item.rect.x}; y: {item.rect.y}")
            print()

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        if inventory_active:
            # draw slots
            for slot in slots:
                slot_color: p.Color = (
                    p.RED if p.check_collision_point_rec(mouse_pos, slot) else p.BLACK
                )

                p.draw_rectangle_lines_ex(slot, 5, slot_color)

            # draw inventory items
            for item in inventory:
                p.draw_rectangle_rec(item.rect, item.color)

        # draw items
        for item in items:
            p.draw_rectangle_rec(item.rect, item.color)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
