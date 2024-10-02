import raylib as r


class Paddle:
    def __init__(self, x, y, width, height, color, speed) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def draw(self):
        r.DrawRectangle(self.x,
                        self.y,
                        self.width,
                        self.height,
                        self.color)
    
    def move(self, key_up, key_down):
        if r.IsKeyDown(key_up) and self.y >= 0:
            self.y -= self.speed
        elif r.IsKeyDown(key_down) and self.y <= r.GetScreenHeight() - self.height:
            self.y += self.speed
            

WIDTH = 10
HEIGHT = 100
COLOR = r.BLACK
SPEED = 4

LEFT_X = 10
RIGHT_X = r.GetScreenWidth() - WIDTH - 10
Y = r.GetScreenHeight()//2 

paddle_left = Paddle(x=LEFT_X,
                     y=Y,
                     width=WIDTH,
                     height=HEIGHT,
                     color=COLOR,
                     speed=SPEED)

paddle_right = Paddle(x=RIGHT_X,
                     y=Y,
                     width=WIDTH,
                     height=HEIGHT,
                     color=COLOR,
                     speed=SPEED)
