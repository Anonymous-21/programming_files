# INITIALIZE CHESS PIECES AND MANAGE GAME STATE

import pyray as p

from constants import BLOCK_SIZE
from board import Board
import pieces


class Game_Manager:
    def __init__(self, pieces_spritesheet) -> None:
        self.board = Board()

        # BLACK PIECES

        self.black_rook1 = pieces.Black_Rook(pieces_spritesheet, 0, 0)
        self.black_knight1 = pieces.Black_Knight(pieces_spritesheet, BLOCK_SIZE, 0)
        self.black_bishop1 = pieces.Black_Bishop(pieces_spritesheet, BLOCK_SIZE * 2, 0)
        self.black_queen = pieces.Black_Queen(pieces_spritesheet, BLOCK_SIZE * 3, 0)
        self.black_king = pieces.Black_King(pieces_spritesheet, BLOCK_SIZE * 4, 0)
        self.black_bishop2 = pieces.Black_Bishop(pieces_spritesheet, BLOCK_SIZE * 5, 0)
        self.black_knight2 = pieces.Black_Knight(pieces_spritesheet, BLOCK_SIZE * 6, 0)
        self.black_rook2 = pieces.Black_Rook(pieces_spritesheet, BLOCK_SIZE * 7, 0)
        self.black_pawn1 = pieces.Black_Pawn(pieces_spritesheet, 0, BLOCK_SIZE)
        self.black_pawn2 = pieces.Black_Pawn(pieces_spritesheet, BLOCK_SIZE, BLOCK_SIZE)
        self.black_pawn3 = pieces.Black_Pawn(
            pieces_spritesheet, BLOCK_SIZE * 2, BLOCK_SIZE
        )
        self.black_pawn4 = pieces.Black_Pawn(
            pieces_spritesheet, BLOCK_SIZE * 3, BLOCK_SIZE
        )
        self.black_pawn5 = pieces.Black_Pawn(
            pieces_spritesheet, BLOCK_SIZE * 4, BLOCK_SIZE
        )
        self.black_pawn6 = pieces.Black_Pawn(
            pieces_spritesheet, BLOCK_SIZE * 5, BLOCK_SIZE
        )
        self.black_pawn7 = pieces.Black_Pawn(
            pieces_spritesheet, BLOCK_SIZE * 6, BLOCK_SIZE
        )
        self.black_pawn8 = pieces.Black_Pawn(
            pieces_spritesheet, BLOCK_SIZE * 7, BLOCK_SIZE
        )

        # WHITE PIECES

        self.white_rook1 = pieces.White_Rook(pieces_spritesheet, 0, BLOCK_SIZE * 7)
        self.white_knight1 = pieces.White_Knight(
            pieces_spritesheet, BLOCK_SIZE, BLOCK_SIZE * 7
        )
        self.white_bishop1 = pieces.White_Bishop(
            pieces_spritesheet, BLOCK_SIZE * 2, BLOCK_SIZE * 7
        )
        self.white_queen = pieces.White_Queen(
            pieces_spritesheet, BLOCK_SIZE * 3, BLOCK_SIZE * 7
        )
        self.white_king = pieces.White_King(
            pieces_spritesheet, BLOCK_SIZE * 4, BLOCK_SIZE * 7
        )
        self.white_bishop2 = pieces.White_Bishop(
            pieces_spritesheet, BLOCK_SIZE * 5, BLOCK_SIZE * 7
        )
        self.white_knight2 = pieces.White_Knight(
            pieces_spritesheet, BLOCK_SIZE * 6, BLOCK_SIZE * 7
        )
        self.white_rook2 = pieces.White_Rook(
            pieces_spritesheet, BLOCK_SIZE * 7, BLOCK_SIZE * 7
        )
        self.white_pawn1 = pieces.White_Pawn(pieces_spritesheet, 0, BLOCK_SIZE * 6)
        self.white_pawn2 = pieces.White_Pawn(
            pieces_spritesheet, BLOCK_SIZE, BLOCK_SIZE * 6
        )
        self.white_pawn3 = pieces.White_Pawn(
            pieces_spritesheet, BLOCK_SIZE * 2, BLOCK_SIZE * 6
        )
        self.white_pawn4 = pieces.White_Pawn(
            pieces_spritesheet, BLOCK_SIZE * 3, BLOCK_SIZE * 6
        )
        self.white_pawn5 = pieces.White_Pawn(
            pieces_spritesheet, BLOCK_SIZE * 4, BLOCK_SIZE * 6
        )
        self.white_pawn6 = pieces.White_Pawn(
            pieces_spritesheet, BLOCK_SIZE * 5, BLOCK_SIZE * 6
        )
        self.white_pawn7 = pieces.White_Pawn(
            pieces_spritesheet, BLOCK_SIZE * 6, BLOCK_SIZE * 6
        )
        self.white_pawn8 = pieces.White_Pawn(
            pieces_spritesheet, BLOCK_SIZE * 7, BLOCK_SIZE * 6
        )

        # chess pieces list

        self.chess_pieces_list = [
            # BLACK
            self.black_rook1,
            self.black_knight1,
            self.black_bishop1,
            self.black_queen,
            self.black_king,
            self.black_bishop2,
            self.black_knight2,
            self.black_rook2,
            self.black_pawn1,
            self.black_pawn2,
            self.black_pawn3,
            self.black_pawn4,
            self.black_pawn5,
            self.black_pawn6,
            self.black_pawn7,
            self.black_pawn8,
            # WHITE
            self.white_rook1,
            self.white_knight1,
            self.white_bishop1,
            self.white_queen,
            self.white_king,
            self.white_bishop2,
            self.white_knight2,
            self.white_rook2,
            self.white_pawn1,
            self.white_pawn2,
            self.white_pawn3,
            self.white_pawn4,
            self.white_pawn5,
            self.white_pawn6,
            self.white_pawn7,
            self.white_pawn8,
        ]

    def draw(self):
        self.board.draw()
        for piece in self.chess_pieces_list:
            piece.draw()

    def update(self):
        self.board.update()

        mouse_x = p.get_mouse_x()
        mouse_y = p.get_mouse_y()

        # GET CHESS PIECE FOCUSED BY MOUSE
        for piece in self.chess_pieces_list:
            if p.check_collision_point_rec(
                (mouse_x, mouse_y), (piece.dest_x, piece.dest_y, BLOCK_SIZE, BLOCK_SIZE)
            ):
                active_piece = piece

        # MOVE PIECES
        if (
            p.is_mouse_button_pressed(p.MouseButton.MOUSE_BUTTON_LEFT)
            and not piece.is_dragging
        ):
            active_piece.is_dragging = True
            active_piece.offset_x = mouse_x - active_piece.dest_x
            active_piece.offset_y = mouse_y - active_piece.dest_y
        elif (
            p.is_mouse_button_down(p.MouseButton.MOUSE_BUTTON_LEFT)
            and piece.is_dragging
        ):
            active_piece.dest_x = mouse_x - active_piece.offset_x
            active_piece.dest_y = mouse_y - active_piece.offset_y
        elif p.is_mouse_button_released(p.MouseButton.MOUSE_BUTTON_LEFT):
            active_piece.is_dragging = False
            active_piece.offset_x = 0
            active_piece.offset_y = 0
            if self.board.active_block:
                active_piece.dest_x = self.board.active_block[0]
                active_piece.dest_y = self.board.active_block[1]
