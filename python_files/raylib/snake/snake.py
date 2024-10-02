import raylib as r


class Snake:
    def __init__(self, box_size) -> None:
        self.initial_x = 0
        self.initial_y = 0
        self.x = self.initial_x
        self.y = self.initial_y
        self.width = box_size
        self.height = box_size
        self.color = r.BLUE
        self.speed = box_size
        
        self.move_right = True
        self.move_left = False
        self.move_up = False
        self.move_down = False
        
        self.list = [[self.x, self.y]]
        
    def draw(self):
        for segment in self.list:
            r.DrawRectangle(segment[0],
                            segment[1],
                            self.width,
                            self.height,
                            self.color)
    
    def move(self):
        if r.IsKeyPressed(r.KEY_RIGHT) and not self.move_left:
            self.move_right = True
        elif r.IsKeyPressed(r.KEY_LEFT) and not self.move_right:
            self.move_left = True
        elif r.IsKeyPressed(r.KEY_UP) and not self.move_down:
            self.move_up = True
        elif r.IsKeyPressed(r.KEY_DOWN) and not self.move_up:
            self.move_down = True
            
        if self.move_right:
            self.x += self.speed
        elif self.move_left:
            self.x -= self.speed
        elif self.move_up:
            self.y -= self.speed
        elif self.move_down:
            self.y += self.speed
        
        self.list.insert(0, [self.x, self.y])
        self.list.pop()
        