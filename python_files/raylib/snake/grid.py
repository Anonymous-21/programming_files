import raylib as r


class Grid:
    def __init__(self, rows, cols, box_size) -> None:
        self.rows = rows
        self.cols = cols
        self.box_size = box_size
        self.width = self.box_size
        self.height = self.box_size
        self.color = r.BLACK
    
    def draw(self):
        for i in range(self.rows):
            for j in range(self.cols):
                x = j * self.box_size
                y = i * self.box_size
                
                r.DrawRectangleLines(x,
                                     y,
                                     self.width,
                                     self.height,
                                     self.color)
                