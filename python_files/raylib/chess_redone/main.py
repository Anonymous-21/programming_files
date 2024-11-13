import pyray as p
import os

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    SCREEN_BACKGROUND,
    GAME_FPS,
    BLOCK_SIZE,
)
from board import Board
import pieces

os.chdir("/home/anonymous/Downloads/programming_files/python_files/raylib/chess_redone")


class Game:
    def __init__(self) -> None:
        self.pieces_spritesheet = p.load_texture("assets/tileset_128.png")

        self.board = Board()

        # black pieces

        self.black_rook1 = pieces.Black_Rook(self.pieces_spritesheet, 0, 0)
        self.black_knight1 = pieces.Black_Knight(self.pieces_spritesheet, BLOCK_SIZE, 0)
        self.black_bishop1 = pieces.Black_Bishop(
            self.pieces_spritesheet, BLOCK_SIZE * 2, 0
        )
        self.black_queen = pieces.Black_Queen(
            self.pieces_spritesheet, BLOCK_SIZE * 3, 0
        )
        self.black_king = pieces.Black_King(self.pieces_spritesheet, BLOCK_SIZE * 4, 0)
        self.black_bishop2 = pieces.Black_Bishop(
            self.pieces_spritesheet, BLOCK_SIZE * 5, 0
        )
        self.black_knight2 = pieces.Black_Knight(
            self.pieces_spritesheet, BLOCK_SIZE * 6, 0
        )
        self.black_rook2 = pieces.Black_Rook(self.pieces_spritesheet, BLOCK_SIZE * 7, 0)
        self.black_pawn1 = pieces.Black_Pawn(self.pieces_spritesheet, 0, BLOCK_SIZE)
        self.black_pawn2 = pieces.Black_Pawn(
            self.pieces_spritesheet, BLOCK_SIZE, BLOCK_SIZE
        )
        self.black_pawn3 = pieces.Black_Pawn(
            self.pieces_spritesheet, BLOCK_SIZE * 2, BLOCK_SIZE
        )
        self.black_pawn4 = pieces.Black_Pawn(
            self.pieces_spritesheet, BLOCK_SIZE * 3, BLOCK_SIZE
        )
        self.black_pawn5 = pieces.Black_Pawn(
            self.pieces_spritesheet, BLOCK_SIZE * 4, BLOCK_SIZE
        )
        self.black_pawn6 = pieces.Black_Pawn(
            self.pieces_spritesheet, BLOCK_SIZE * 5, BLOCK_SIZE
        )
        self.black_pawn7 = pieces.Black_Pawn(
            self.pieces_spritesheet, BLOCK_SIZE * 6, BLOCK_SIZE
        )
        self.black_pawn8 = pieces.Black_Pawn(
            self.pieces_spritesheet, BLOCK_SIZE * 7, BLOCK_SIZE
        )

        # white pieces

        self.white_rook1 = pieces.White_Rook(self.pieces_spritesheet, 0, BLOCK_SIZE * 7)
        self.white_knight1 = pieces.White_Knight(
            self.pieces_spritesheet, BLOCK_SIZE, BLOCK_SIZE * 7
        )
        self.white_bishop1 = pieces.White_Bishop(
            self.pieces_spritesheet, BLOCK_SIZE * 2, BLOCK_SIZE * 7
        )
        self.white_queen = pieces.White_Queen(
            self.pieces_spritesheet, BLOCK_SIZE * 3, BLOCK_SIZE * 7
        )
        self.white_king = pieces.White_King(
            self.pieces_spritesheet, BLOCK_SIZE * 4, BLOCK_SIZE * 7
        )
        self.white_bishop2 = pieces.White_Bishop(
            self.pieces_spritesheet, BLOCK_SIZE * 5, BLOCK_SIZE * 7
        )
        self.white_knight2 = pieces.White_Knight(
            self.pieces_spritesheet, BLOCK_SIZE * 6, BLOCK_SIZE * 7
        )
        self.white_rook2 = pieces.White_Rook(
            self.pieces_spritesheet, BLOCK_SIZE * 7, BLOCK_SIZE * 7
        )
        self.white_pawn1 = pieces.White_Pawn(self.pieces_spritesheet, 0, BLOCK_SIZE * 6)
        self.white_pawn2 = pieces.White_Pawn(
            self.pieces_spritesheet, BLOCK_SIZE, BLOCK_SIZE * 6
        )
        self.white_pawn3 = pieces.White_Pawn(
            self.pieces_spritesheet, BLOCK_SIZE * 2, BLOCK_SIZE * 6
        )
        self.white_pawn4 = pieces.White_Pawn(
            self.pieces_spritesheet, BLOCK_SIZE * 3, BLOCK_SIZE * 6
        )
        self.white_pawn5 = pieces.White_Pawn(
            self.pieces_spritesheet, BLOCK_SIZE * 4, BLOCK_SIZE * 6
        )
        self.white_pawn6 = pieces.White_Pawn(
            self.pieces_spritesheet, BLOCK_SIZE * 5, BLOCK_SIZE * 6
        )
        self.white_pawn7 = pieces.White_Pawn(
            self.pieces_spritesheet, BLOCK_SIZE * 6, BLOCK_SIZE * 6
        )
        self.white_pawn8 = pieces.White_Pawn(
            self.pieces_spritesheet, BLOCK_SIZE * 7, BLOCK_SIZE * 6
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
        pass


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    game = Game()

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        game.draw()
        game.update()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
