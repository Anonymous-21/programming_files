import pyray as p

from constants import BLOCK_SIZE


class Pieces:
    def __init__(self, pieces_spritesheet) -> None:
        self.spritesheet = pieces_spritesheet
        self.source_width = self.spritesheet.width / 6
        self.source_height = self.spritesheet.height / 2
        
        self.offset_x = 0
        self.offset_y = 0
        self.is_dragging = False
        
# BLACK PIECES

class BlackRook(Pieces):
    def __init__(self, pieces_spritesheet, window_x, window_y):
        super().__init__(pieces_spritesheet)
        
        self.source_x = 0
        self.source_y = 0
        self.window_x = window_x
        self.window_y = window_y
    
    def draw(self):
        p.draw_texture_pro(self.spritesheet, 
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.window_x, self.window_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class BlackKnight(Pieces):
    def __init__(self, pieces_spritesheet, window_x, window_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width
        self.source_y = 0
        self.window_x = window_x
        self.window_y = window_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.window_x, self.window_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class BlackBishop(Pieces):
    def __init__(self, pieces_spritesheet, window_x, window_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width * 2
        self.source_y = 0
        self.window_x = window_x
        self.window_y = window_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.window_x, self.window_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class BlackQueen(Pieces):
    def __init__(self, pieces_spritesheet, window_x, window_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width * 3
        self.source_y = 0
        self.window_x = window_x
        self.window_y = window_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.window_x, self.window_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class BlackKing(Pieces):
    def __init__(self, pieces_spritesheet, window_x, window_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width * 4
        self.source_y = 0
        self.window_x = window_x
        self.window_y = window_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.window_x, self.window_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class BlackPawn(Pieces):
    def __init__(self, pieces_spritesheet, window_x, window_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width * 5
        self.source_y = 0
        self.window_x = window_x
        self.window_y = window_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.window_x, self.window_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
# WHITE PIECES

class WhiteRook(Pieces):
    def __init__(self, pieces_spritesheet, window_x, window_y):
        super().__init__(pieces_spritesheet)
        
        self.source_x = 0
        self.source_y = self.source_height
        self.window_x = window_x
        self.window_y = window_y
    
    def draw(self):
        p.draw_texture_pro(self.spritesheet, 
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.window_x, self.window_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class WhiteKnight(Pieces):
    def __init__(self, pieces_spritesheet, window_x, window_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width
        self.source_y = self.source_height
        self.window_x = window_x
        self.window_y = window_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.window_x, self.window_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class WhiteBishop(Pieces):
    def __init__(self, pieces_spritesheet, window_x, window_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width * 2
        self.source_y = self.source_height
        self.window_x = window_x
        self.window_y = window_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.window_x, self.window_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class WhiteQueen(Pieces):
    def __init__(self, pieces_spritesheet, window_x, window_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width * 3
        self.source_y = self.source_height
        self.window_x = window_x
        self.window_y = window_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.window_x, self.window_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class WhiteKing(Pieces):
    def __init__(self, pieces_spritesheet, window_x, window_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width * 4
        self.source_y = self.source_height
        self.window_x = window_x
        self.window_y = window_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.window_x, self.window_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class WhitePawn(Pieces):
    def __init__(self, pieces_spritesheet, window_x, window_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width * 5
        self.source_y = self.source_height
        self.window_x = window_x
        self.window_y = window_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.window_x, self.window_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
