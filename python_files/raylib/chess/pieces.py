import pyray as p

from constants import BLOCK_SIZE


class Pieces:
    def __init__(self, pieces_spritesheet) -> None:
        self.spritesheet = pieces_spritesheet

        self.source_width = self.spritesheet.width / 6
        self.source_height = self.spritesheet.height / 2

        self.dest_width = BLOCK_SIZE
        self.dest_height = BLOCK_SIZE


class Rook(Pieces):
    def __init__(self, pieces_spritesheet) -> None:
        super().__init__(pieces_spritesheet)

        self.black_rook_source_x = 0
        self.black_rook_source_y = 0
        self.black_rook_dest1_x = 0
        self.black_rook_dest1_y = 0
        self.black_rook_dest2_x = BLOCK_SIZE * 7
        self.black_rook_dest2_y = 0

        self.white_rook_source_x = 0
        self.white_rook_source_y = self.source_height
        self.white_rook_dest1_x = 0
        self.white_rook_dest1_y = BLOCK_SIZE * 7
        self.white_rook_dest2_x = BLOCK_SIZE * 7
        self.white_rook_dest2_y = BLOCK_SIZE * 7

    def draw(self):
        # black
        p.draw_texture_pro(
            self.spritesheet,
            (
                self.black_rook_source_x,
                self.black_rook_source_y,
                self.source_width,
                self.source_height,
            ),
            (
                self.black_rook_dest1_x,
                self.black_rook_dest1_y,
                self.dest_width,
                self.dest_height,
            ),
            (0, 0),
            0,
            p.WHITE,
        )
        p.draw_texture_pro(
            self.spritesheet,
            (
                self.black_rook_source_x,
                self.black_rook_source_y,
                self.source_width,
                self.source_height,
            ),
            (
                self.black_rook_dest2_x,
                self.black_rook_dest2_y,
                self.dest_width,
                self.dest_height,
            ),
            (0, 0),
            0,
            p.WHITE,
        )

        # white
        p.draw_texture_pro(
            self.spritesheet,
            (
                self.white_rook_source_x,
                self.white_rook_source_y,
                self.source_width,
                self.source_height,
            ),
            (
                self.white_rook_dest1_x,
                self.white_rook_dest1_y,
                self.dest_width,
                self.dest_height,
            ),
            (0, 0),
            0,
            p.WHITE,
        )
        p.draw_texture_pro(
            self.spritesheet,
            (
                self.white_rook_source_x,
                self.white_rook_source_y,
                self.source_width,
                self.source_height,
            ),
            (
                self.white_rook_dest2_x,
                self.white_rook_dest2_y,
                self.dest_width,
                self.dest_height,
            ),
            (0, 0),
            0,
            p.WHITE,
        )


class Knight(Pieces):
    def __init__(self, pieces_spritesheet) -> None:
        super().__init__(pieces_spritesheet)

        self.black_knight_source_x = self.source_width
        self.black_knight_source_y = 0
        self.black_knight_dest1_x = BLOCK_SIZE
        self.black_knight_dest1_y = 0
        self.black_knight_dest2_x = BLOCK_SIZE * 6
        self.black_knight_dest2_y = 0

        self.white_knight_source_x = self.source_width
        self.white_knight_source_y = self.source_height
        self.white_knight_dest1_x = 0
        self.white_knight_dest1_y = BLOCK_SIZE * 7
        self.white_knight_dest2_x = BLOCK_SIZE * 6
        self.white_knight_dest2_y = BLOCK_SIZE * 7

    def draw(self):
        p.draw_texture_pro(
            self.spritesheet,
            (
                self.black_knight_source_x,
                self.black_knight_source_y,
                self.source_width,
                self.source_height,
            ),
            (
                self.black_knight_dest1_x,
                self.black_knight_dest1_y,
                self.dest_width,
                self.dest_height,
            ),
            (0, 0),
            0,
            p.WHITE,
        )
        p.draw_texture_pro(
            self.spritesheet,
            (
                self.black_knight_source_x,
                self.black_knight_source_y,
                self.source_width,
                self.source_height,
            ),
            (
                self.black_knight_dest2_x,
                self.black_knight_dest2_y,
                self.dest_width,
                self.dest_height,
            ),
            (0, 0),
            0,
            p.WHITE,
        )
        # white
        p.draw_texture_pro(
            self.spritesheet,
            (
                self.white_knight_source_x,
                self.white_knight_source_y,
                self.source_width,
                self.source_height,
            ),
            (
                self.white_knight_dest1_x,
                self.white_knight_dest1_y,
                self.dest_width,
                self.dest_height,
            ),
            (0, 0),
            0,
            p.WHITE,
        )
        p.draw_texture_pro(
            self.spritesheet,
            (
                self.white_knight_source_x,
                self.white_knight_source_y,
                self.source_width,
                self.source_height,
            ),
            (
                self.white_knight_dest2_x,
                self.white_knight_dest2_y,
                self.dest_width,
                self.dest_height,
            ),
            (0, 0),
            0,
            p.WHITE,
        )
        


class Bishop(Pieces):
    def __init__(self, pieces_spritesheet) -> None:
        super().__init__(pieces_spritesheet)

        self.black_bishop_source_x = self.source_width * 2
        self.black_bishop_source_y = 0
        self.black_bishop_dest1_x = BLOCK_SIZE * 2
        self.black_bishop_dest1_y = 0
        self.black_bishop_dest2_x = BLOCK_SIZE * 5
        self.black_bishop_dest2_y = 0

        self.white_bishop_source_x = self.source_width * 2
        self.white_bishop_source_y = self.source_height
        self.white_bishop_dest1_x = BLOCK_SIZE * 2
        self.white_bishop_dest1_y = BLOCK_SIZE * 7
        self.white_bishop_dest2_x = BLOCK_SIZE * 5
        self.white_bishop_dest2_y = BLOCK_SIZE * 7


class King(Pieces):
    def __init__(self, pieces_spritesheet) -> None:
        super().__init__(pieces_spritesheet)

        self.black_king_source_x = self.source_width * 3
        self.black_king_source_y = 0
        self.black_king_dest_x = BLOCK_SIZE * 4
        self.black_king_dest_y = 0

        self.white_king_source_x = self.source_width * 3
        self.white_king_source_y = self.source_height
        self.white_king_dest_x = BLOCK_SIZE * 4
        self.white_king_dest_y = BLOCK_SIZE * 7


class Queen(Pieces):
    def __init__(self, pieces_spritesheet) -> None:
        super().__init__(pieces_spritesheet)

        self.black_queen_source_x = self.source_width * 4
        self.black_queen_source_y = 0
        self.black_queen_dest_x = BLOCK_SIZE * 3
        self.black_queen_dest_y = 0

        self.white_queen_source_x = self.source_width * 4
        self.white_queen_source_y = self.source_height
        self.white_queen_dest_x = BLOCK_SIZE * 3
        self.white_queen_dest_y = BLOCK_SIZE * 7


class Pawn(Pieces):
    def __init__(self, pieces_spritesheet) -> None:
        super().__init__(pieces_spritesheet)

        self.black_pawn_source_x = self.source_width * 5
        self.black_pawn_source_y = 0
        self.black_pawn_dest1_x = 0
        self.black_pawn_dest1_y = BLOCK_SIZE
        self.black_pawn_dest2_x = BLOCK_SIZE
        self.black_pawn_dest2_y = BLOCK_SIZE
        self.black_pawn_dest3_x = BLOCK_SIZE * 2
        self.black_pawn_dest3_y = BLOCK_SIZE
        self.black_pawn_dest4_x = BLOCK_SIZE * 3
        self.black_pawn_dest4_y = BLOCK_SIZE
        self.black_pawn_dest5_x = BLOCK_SIZE * 4
        self.black_pawn_dest5_y = BLOCK_SIZE
        self.black_pawn_dest6_x = BLOCK_SIZE * 5
        self.black_pawn_dest6_y = BLOCK_SIZE
        self.black_pawn_dest7_x = BLOCK_SIZE * 6
        self.black_pawn_dest7_y = BLOCK_SIZE
        self.black_pawn_dest8_x = BLOCK_SIZE * 7
        self.black_pawn_dest8_y = BLOCK_SIZE

        # white
        self.white_pawn_source_x = self.source_width * 5
        self.white_pawn_source_y = self.source_height
        self.white_pawn_dest1_x = 0
        self.white_pawn_dest1_y = BLOCK_SIZE * 6
        self.white_pawn_dest2_x = BLOCK_SIZE
        self.white_pawn_dest2_y = BLOCK_SIZE * 6
        self.white_pawn_dest3_x = BLOCK_SIZE * 2
        self.white_pawn_dest3_y = BLOCK_SIZE * 6
        self.white_pawn_dest4_x = BLOCK_SIZE * 3
        self.white_pawn_dest4_y = BLOCK_SIZE * 6
        self.white_pawn_dest5_x = BLOCK_SIZE * 4
        self.white_pawn_dest5_y = BLOCK_SIZE * 6
        self.white_pawn_dest6_x = BLOCK_SIZE * 5
        self.white_pawn_dest6_y = BLOCK_SIZE * 6
        self.white_pawn_dest7_x = BLOCK_SIZE * 6
        self.white_pawn_dest7_y = BLOCK_SIZE * 6
        self.white_pawn_dest8_x = BLOCK_SIZE * 7
        self.white_pawn_dest8_y = BLOCK_SIZE * 6
