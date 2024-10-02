import raylib as r


class Paddle:
    def __init__(self) -> None:
        self.width = 10
        self.height = 100
        self.left_x = 10
        self.right_x = r.GetScreenWidth() - self.width - 10
        self.initial_y = r.GetScreenHeight()//2 - self.height//2
        self.left_y = self.initial_y
        self.right_y = self.initial_y
        self.color = r.BLACK
        self.speed = 5

    def draw(self):
        # draw left paddle
        r.DrawRectangle(self.left_x,
                        self.left_y,
                        self.width,
                        self.height,
                        self.color)
        # draw right paddle
        r.DrawRectangle(self.right_x,
                        self.right_y,
                        self.width,
                        self.height,
                        self.color)
    
    def move(self):
        # left paddle
        if r.IsKeyDown(r.KEY_W) and self.left_y >= 0:
            self.left_y -= self.speed
        elif r.IsKeyDown(r.KEY_S) and self.left_y <= r.GetScreenHeight() - self.height:
            self.left_y += self.speed
        
        # right paddle
        if r.IsKeyDown(r.KEY_UP) and self.right_y >= 0:
            self.right_y -= self.speed
        elif r.IsKeyDown(r.KEY_DOWN) and self.right_y <= r.GetScreenHeight() - self.height:
            self.right_y += self.speed
            