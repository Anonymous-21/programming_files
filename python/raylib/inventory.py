import pyray as p

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = ""
SCREEN_BACKGROUND: p.Color = p.RAYWHITE

ROWS: int = 5
COLS: int = 5
SLOT_SIZE: int = 80
SLOT_GAP: int = 5

NUM_OF_ITEM: int = 5


class Item:
    def __init__(self, name: str, pos: p.Vector2) -> None:
        self.id: int = -1
        self.name: str = name
        self.rect: p.Rectangle = p.Rectangle(pos.x, pos.y, 60, 60)
        self.color: p.Color = p.Color(
            int(p.get_random_value(0, 255)),
            int(p.get_random_value(0, 255)),
            int(p.get_random_value(0, 255)),
            255,
        )
        self.offset: p.Vector2 = p.Vector2(0, 0)
        self.is_dragging: bool = False


class Game:
    def __init__(self) -> None:
        self.pos: p.Vector2 = p.Vector2(20, 20)
        self.inventory_active: bool = True
        self.slots: list[p.Rectangle] = []
        self.inventory: list[Item] = []
        self.item_list: list[Item] = []

        for i in range(ROWS):
            for j in range(COLS):
                x: int = j * (SLOT_SIZE + SLOT_GAP) + self.pos.x
                y: int = i * (SLOT_SIZE + SLOT_GAP) + self.pos.y

                self.slots.append(p.Rectangle(x, y, SLOT_SIZE, SLOT_SIZE))

        for i in range(NUM_OF_ITEM):
            item: Item = Item(f"item{i + 1}", p.Vector2(600, (i + 1) * 80))
            self.item_list.append(item)

    def draw(self) -> None:
        if self.inventory_active:
            # draw slots
            for slot in self.slots:
                color: p.Color = (
                    p.RED
                    if p.check_collision_point_rec(p.get_mouse_position(), slot)
                    else p.BLACK
                )

                p.draw_rectangle_lines_ex(slot, 5, color)

            # draw inventory items
            for item in self.inventory:
                p.draw_rectangle_rec(item.rect, item.color)

        # draw scattered items
        for item in self.item_list:
            if item.id < 0:
                p.draw_rectangle_rec(item.rect, item.color)

    def update(self) -> None:
        if p.is_key_pressed(p.KeyboardKey.KEY_I):
            self.inventory_active = not self.inventory_active

        mouse_pos: p.Vector2 = p.get_mouse_position()

        for item in self.item_list:
            if p.is_mouse_button_pressed(p.MouseButton.MOUSE_BUTTON_LEFT):
                if not item.is_dragging and p.check_collision_point_rec(
                    mouse_pos, item.rect
                ):
                    item.is_dragging = True
                    item.offset.x = mouse_pos.x - item.rect.x
                    item.offset.y = mouse_pos.y - item.rect.y

                    item.id = -1
                    self.item_list.append(item)
                    for inv_item in self.inventory:
                        if inv_item == item:
                            self.inventory.remove(inv_item)

            if p.is_mouse_button_released(p.MouseButton.MOUSE_BUTTON_LEFT):
                if item.is_dragging:
                    item.is_dragging = False

                    # snap to slot
                    for slot in self.slots:
                        if p.check_collision_recs(slot, item.rect):
                            item.rect.x = slot.x + (slot.width - item.rect.width) / 2
                            item.rect.y = slot.y + (slot.height - item.rect.height) / 2
                            item.id = self.slots.index(slot)
                            self.inventory.append(item)
                            self.item_list.remove(item)

            if item.is_dragging:
                item.rect.x = mouse_pos.x - item.offset.x
                item.rect.y = mouse_pos.y - item.offset.y

        for item in self.inventory:
            print(f"{item.name}: {item.id}")
        for item in self.item_list:
            print(f"{item.name}: {item.id}")


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    game: Game = Game()

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        game.draw()
        game.update()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
