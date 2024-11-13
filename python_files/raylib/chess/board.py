import pyray as p

from constants import ROWS, COLS, BLOCK_SIZE


class Board:
    def __init__(self) -> None:
        self.board = []
        self.gen_grid()

    def gen_grid(self):
        tile_color = p.WHITE
        for i in range(ROWS):
            for j in range(COLS):
                x = j * BLOCK_SIZE
                y = i * BLOCK_SIZE

                self.board.append([x, y, tile_color])

                if tile_color == p.WHITE:
                    tile_color = p.SKYBLUE
                elif tile_color == p.SKYBLUE:
                    tile_color = p.WHITE

            if tile_color == p.WHITE:
                tile_color = p.SKYBLUE
            elif tile_color == p.SKYBLUE:
                tile_color = p.WHITE

    def draw(self):
        for tile in self.board:
            p.draw_rectangle_rec(
                (tile[0], tile[1], BLOCK_SIZE, BLOCK_SIZE), tile[2]
            )
