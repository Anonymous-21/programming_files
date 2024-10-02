import raylib as r

from encode import encode
from paddle import paddle_left, paddle_right
from ball import Ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PONG"
SCREEN_BACKGROUND = r.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self) -> None:
        self.paddle_left = paddle_left
        self.paddle_right = paddle_right
        self.ball = Ball()
        
    def draw(self):
        self.paddle_left.draw()
        self.paddle_right.draw()
        self.ball.draw()
        
    def update(self):
        self.paddle_left.move(r.KEY_W, r.KEY_S)
        self.paddle_right.move(r.KEY_UP, r.KEY_DOWN)
        self.ball.move()
        

def main():
    r.InitWindow(SCREEN_WIDTH,
                 SCREEN_HEIGHT,
                 encode(SCREEN_TITLE))
    r.SetTargetFPS(GAME_FPS)
    
    game = Game()
    
    while not r.WindowShouldClose():
        r.BeginDrawing()
        r.ClearBackground(SCREEN_BACKGROUND)
        
        game.draw()
        game.update()
        
        r.EndDrawing()
        
    r.CloseWindow()
    

if __name__ == "__main__":
    main()
        