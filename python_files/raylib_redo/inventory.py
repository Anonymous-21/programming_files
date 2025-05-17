import pyray as p
from dataclasses import dataclass

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Simple Inventory"
SCREEN_BACKGROUND: p.Color = p.RAYWHITE

ROWS: int = 5
COLS: int = 5
SLOT_SIZE: int = 80
SLOT_GAP: int = 5

@dataclass
class Item:
    rect: p.Rectangle
    color: p.Color

def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    pos: p.Vector2 = p.Vector2(10, 10)

    slots: list[p.Rectangle] = []    

    for i in range(ROWS):
        for j in range(COLS):
            x: float = j * (SLOT_SIZE + SLOT_GAP) + pos.x
            y: float = i * (SLOT_SIZE + SLOT_GAP) + pos.y

            slots.append(p.Rectangle(x, y, SLOT_SIZE, SLOT_SIZE))

    while not p.window_should_close():
        mouse_pos: p.Vector2 = p.get_mouse_position()

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        # draw inventory
        for slot in slots:
            color: p.Color = (
                p.RED if p.check_collision_point_rec(mouse_pos, slot) else p.BLACK
            )

            p.draw_rectangle_lines_ex(slot, 5.0, color)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
