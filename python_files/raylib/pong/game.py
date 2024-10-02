import raylib as r

from encode import encode
from paddle import Paddle
from ball import Ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PONG"
SCREEN_BACKGROUND = r.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self) -> None:
        self.game_over = False
        
        self.paddle = Paddle()
        self.ball = Ball()
        
    def draw(self):
        # screen divider
        r.DrawLineEx((r.GetScreenWidth()//2,
                   0),
                   (r.GetScreenWidth()//2,
                   r.GetScreenHeight()),
                   2,
                   r.GRAY)
        
        self.paddle.draw()
        self.ball.draw()
        
    def update(self):
        if not self.game_over:
            self.paddle.move()
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
        