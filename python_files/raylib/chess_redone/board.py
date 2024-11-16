import pyray as p

from constants import ROWS, COLS, BLOCK_SIZE


class Board:
    def __init__(self) -> None:
        self.board = []
        self.tile_color = p.WHITE
        self.gen_board()

        self.active_block = None
        self.highlight_thickness = 5
        self.hightlight_color = p.GRAY

    def gen_board(self):
        for i in range(ROWS):
            for j in range(COLS):
                x = j * BLOCK_SIZE
                y = i * BLOCK_SIZE

                self.board.append([x, y, self.tile_color])

                if self.tile_color == p.WHITE:
                    self.tile_color = p.SKYBLUE
                elif self.tile_color == p.SKYBLUE:
                    self.tile_color = p.WHITE

            if self.tile_color == p.WHITE:
                self.tile_color = p.SKYBLUE
            elif self.tile_color == p.SKYBLUE:
                self.tile_color = p.WHITE

    def draw(self):
        for tile in self.board:
            p.draw_rectangle_rec((tile[0], tile[1], BLOCK_SIZE, BLOCK_SIZE), tile[2])
            
            if self.active_block:
                p.draw_rectangle_lines_ex(
                    (
                        self.active_block[0],
                        self.active_block[1],
                        BLOCK_SIZE,
                        BLOCK_SIZE,
                    ),
                    self.highlight_thickness,
                    self.hightlight_color,
                )

    def update(self):
        self.active_block = None
        mouse_x = p.get_mouse_x()
        mouse_y = p.get_mouse_y()

        for tile in self.board:
            if p.check_collision_point_rec(
                (mouse_x, mouse_y), (tile[0], tile[1], BLOCK_SIZE, BLOCK_SIZE)
            ):
                self.active_block = tile
                break
