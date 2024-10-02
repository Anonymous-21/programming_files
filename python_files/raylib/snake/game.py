import raylib as r

from encode import encode
from snake import Snake


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "SNAKE"
SCREEN_BACKGROUND = r.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self) -> None:
        self.game_over = False
        
        self.rows = 20
        self.cols = 20
        self.box_size = 40
        
        self.snake = Snake(self.box_size)
        
    def draw_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                y = i * self.box_size
                x = j * self.box_size 
                
                r.DrawRectangleLines(x,
                                     y,
                                     self.box_size,
                                     self.box_size,
                                     r.BLACK)
                
    def draw(self):
        self.snake.draw()
        
    def update(self):
        if not self.game_over:
            self.snake.move()
            self.game_over = self.snake.check_collision(self.game_over)
            
    def game_over_menu(self):
        if self.game_over:
            r.DrawRectangle(0,
                            0,
                            r.GetScreenWidth(),
                            r.GetScreenHeight(),
                            SCREEN_BACKGROUND)
            r.DrawText(encode("GAME OVER"),
                       r.GetScreenWidth()//2 - 100,
                       r.GetScreenHeight()//2 - 70,
                       30,
                       r.BLACK)
            r.DrawText(encode("Press 'ENTER' to continue"),
                       r.GetScreenWidth()//2 - 130,
                       r.GetScreenHeight()//2 ,
                       20,
                       r.BLACK)
        
        if r.IsKeyPressed(r.KEY_ENTER):
            self.game_over = False
            self.snake = Snake(self.box_size)  
        


def main():
    r.InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, encode(SCREEN_TITLE))
    r.SetTargetFPS(GAME_FPS)
    
    game = Game()
    
    while not r.WindowShouldClose():
        r.BeginDrawing()
        r.ClearBackground(SCREEN_BACKGROUND)
        
        game.draw_grid()
        game.draw()
        game.update()
        game.game_over_menu()
        
        r.EndDrawing()
        
    r.CloseWindow()
    

if __name__ == "__main__":
    main()