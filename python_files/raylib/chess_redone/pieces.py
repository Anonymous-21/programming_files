import pyray as p

from constants import BLOCK_SIZE


class Pieces:
    def __init__(self, pieces_spritesheet) -> None:
        self.spritesheet = pieces_spritesheet
        self.source_width = self.spritesheet.width / 6
        self.source_height = self.spritesheet.height / 2
        

class Black_Rook(Pieces):
    def __init__(self, pieces_spritesheet, dest_x, dest_y):
        super().__init__(pieces_spritesheet)
        
        self.source_x = 0
        self.source_y = 0
        self.dest_x = dest_x
        self.dest_y = dest_y
    
    def draw(self):
        p.draw_texture_pro(self.spritesheet, 
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.dest_x, self.dest_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class Black_Knight(Pieces):
    def __init__(self, pieces_spritesheet, dest_x, dest_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width
        self.source_y = 0
        self.dest_x = dest_x
        self.dest_y = dest_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.dest_x, self.dest_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class Black_Bishop(Pieces):
    def __init__(self, pieces_spritesheet, dest_x, dest_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width * 2
        self.source_y = 0
        self.dest_x = dest_x
        self.dest_y = dest_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.dest_x, self.dest_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class Black_Queen(Pieces):
    def __init__(self, pieces_spritesheet, dest_x, dest_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width * 3
        self.source_y = 0
        self.dest_x = dest_x
        self.dest_y = dest_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.dest_x, self.dest_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class Black_King(Pieces):
    def __init__(self, pieces_spritesheet, dest_x, dest_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width * 4
        self.source_y = 0
        self.dest_x = dest_x
        self.dest_y = dest_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.dest_x, self.dest_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class Black_Pawn(Pieces):
    def __init__(self, pieces_spritesheet, dest_x, dest_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width * 5
        self.source_y = 0
        self.dest_x = dest_x
        self.dest_y = dest_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.dest_x, self.dest_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
# white pieces

class White_Rook(Pieces):
    def __init__(self, pieces_spritesheet, dest_x, dest_y):
        super().__init__(pieces_spritesheet)
        
        self.source_x = 0
        self.source_y = self.source_height
        self.dest_x = dest_x
        self.dest_y = dest_y
    
    def draw(self):
        p.draw_texture_pro(self.spritesheet, 
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.dest_x, self.dest_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class White_Knight(Pieces):
    def __init__(self, pieces_spritesheet, dest_x, dest_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width
        self.source_y = self.source_height
        self.dest_x = dest_x
        self.dest_y = dest_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.dest_x, self.dest_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class White_Bishop(Pieces):
    def __init__(self, pieces_spritesheet, dest_x, dest_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width * 2
        self.source_y = self.source_height
        self.dest_x = dest_x
        self.dest_y = dest_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.dest_x, self.dest_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class White_Queen(Pieces):
    def __init__(self, pieces_spritesheet, dest_x, dest_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width * 3
        self.source_y = self.source_height
        self.dest_x = dest_x
        self.dest_y = dest_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.dest_x, self.dest_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class White_King(Pieces):
    def __init__(self, pieces_spritesheet, dest_x, dest_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width * 4
        self.source_y = self.source_height
        self.dest_x = dest_x
        self.dest_y = dest_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.dest_x, self.dest_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        
class White_Pawn(Pieces):
    def __init__(self, pieces_spritesheet, dest_x, dest_y) -> None:
        super().__init__(pieces_spritesheet)
        
        self.source_x = self.source_width * 5
        self.source_y = self.source_height
        self.dest_x = dest_x
        self.dest_y = dest_y
        
    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.source_x, self.source_y, self.source_width, self.source_height),
                           (self.dest_x, self.dest_y, BLOCK_SIZE, BLOCK_SIZE),
                           (0, 0),
                           0,
                           p.WHITE)
        