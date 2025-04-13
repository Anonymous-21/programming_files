import pyray as p

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Movable Inventory"
SCREEN_BACKGROUND = p.RAYWHITE


class Inventory:
    def __init__(self, rows, cols, slot_size, pos):
        self.rows = rows
        self.cols = cols
        self.slot_size = slot_size
        self.gap = 5
        self.outer_rect_padding = 10
        self.outer_rect = p.Rectangle(
            pos.x - self.outer_rect_padding,
            pos.y - self.outer_rect_padding,
            rows * (slot_size + self.gap) + pos.x + self.outer_rect_padding,
            cols * (slot_size + self.gap) + pos.y + self.outer_rect_padding,
        )
        self.outer_rect_color = p.SKYBLUE
        self.pos = pos
        self.outline_color = p.BLACK
        self.thickness = 5
        self.list = []

        for i in range(rows):
            for j in range(cols):
                x = j * (slot_size + self.gap) + pos.x
                y = i * (slot_size + self.gap) + pos.y

                self.list.append(p.Rectangle(x, y, slot_size, slot_size))

    def draw(self):
        p.draw_rectangle_rec(self.outer_rect, self.outline_color)

        for slot in self.list:
            self.highlight_color = p.WHITE
            p.draw_rectangle_rec(slot, self.highlight_color)
            p.draw_rectangle_lines_ex(slot, self.thickness, self.outline_color)


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    inventory = Inventory(2, 5, 60, p.Vector2(100, 200))

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        inventory.draw()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
