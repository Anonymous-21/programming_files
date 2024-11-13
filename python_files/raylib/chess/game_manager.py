import pyray as p

from board import Board
from pieces import Pieces, Rook, Knight, Bishop, King, Queen, Pawn


class Game_Manager:
    def __init__(self, pieces_spritesheet) -> None:
        self.board = Board()
        self.pieces = Pieces(pieces_spritesheet)
        self.rook = Rook(pieces_spritesheet)
        self.knight = Knight(pieces_spritesheet)
        self.bishop = Bishop(pieces_spritesheet)
        self.king = King(pieces_spritesheet)
        self.queen = Queen(pieces_spritesheet)
        self.pawn = Pawn(pieces_spritesheet)

    def draw(self):
        self.board.draw()
        self.rook.draw()

    def update(self):
        # self.board.update()
        pass
