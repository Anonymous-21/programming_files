import raylib as r


class Ball:
    def __init__(self) -> None:
        self.radius = 10
        self.x = r.GetScreenWidth()//2 - self.radius
        self.y = r.GetScreenHeight()//2 - self.radius
        self.color = r.RED
        self.change_x = 5
        self.change_y = 6
        
    def draw(self):
        r.DrawCircle(self.x,
                     self.y,
                     self.radius,
                     self.color)
    
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        
        if self.x <= 0 or self.x >= r.GetScreenWidth() - self.radius:
            self.change_x *= -1
        elif self.y <= 0 or self.y >= r.GetScreenHeight() - self.radius:
            self.change_y *= -1
            
        