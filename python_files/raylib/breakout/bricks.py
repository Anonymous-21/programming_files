import pyray as p


class Bricks:
    def __init__(self) -> None:
        self.rows = 5
        self.cols = 10
        self.width = 79
        self.height = 30
        self.gap = 2
        self.color = p.GRAY
        self.grid = []
        
        self.gen_grid()
    
    def gen_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                x = j * (self.width + self.gap)
                y = i * (self.height + self.gap)
                
                self.grid.append([x, y])
                
        
    def draw(self):
        for segment in self.grid:
            p.draw_rectangle_rec((segment[0], segment[1], self.width, self.height), self.color)
