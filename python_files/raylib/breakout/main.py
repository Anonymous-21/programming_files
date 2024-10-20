import pyray as p
from paddle import Paddle
from ball import Ball
from bricks import Bricks


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Breakout"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self) -> None:
        self.game_over = False
        self.game_won = False
        self.lives = 5

        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = Bricks()

    def draw(self):
        # draw lives
        p.draw_text(f"Lives: {self.lives}", 10, p.get_screen_height() - 50, 30, p.GRAY)

        self.paddle.draw()
        self.ball.draw()
        self.bricks.draw()

    def update(self):
        # game win condition
        if len(self.bricks.grid) == 0:
            self.game_won = True
            
        # game over condition
        if self.lives <= 0:
            self.game_over = True

        self.paddle.update()
        self.ball.update()

        # ball collision with paddle
        if p.check_collision_circle_rec(
            (self.ball.x, self.ball.y),
            self.ball.radius,
            (self.paddle.x, self.paddle.y, self.paddle.width, self.paddle.height),
        ):
            self.ball.speed_y *= -1

        # bricks collision ball
        for segment in self.bricks.grid:
            if p.check_collision_circle_rec(
                (self.ball.x, self.ball.y),
                self.ball.radius,
                (segment[0], segment[1], self.bricks.width, self.bricks.height),
            ):
                self.ball.speed_y *= -1
                self.bricks.grid.remove(segment)

        # ball collision floor
        if self.ball.y >= p.get_screen_height() - self.ball.radius:
            self.lives -= 1
            self.ball.frames_counter = 0
            self.ball.reset()
            self.paddle.reset()

    def game_over_menu(self):
        p.draw_rectangle(
            0, 0, p.get_screen_width(), p.get_screen_height(), SCREEN_BACKGROUND
        )
        p.draw_text(
            "You Win!",
            p.get_screen_width()//2 - 70,
            p.get_screen_height()//2 - 30,
            40,
            p.BLACK,
        )
        p.draw_text(
            "Press 'Enter' to restart",
            p.get_screen_width()//2 - 130,
            p.get_screen_height()//2 + 20,
            30,
            p.BLACK,
        )
        
        if p.is_key_pressed(p.KeyboardKey.KEY_ENTER):
            self.lives = 5
            self.game_over = False
            self.paddle = Paddle()
            self.ball = Ball()
            self.bricks = Bricks()
    
    def game_won_menu(self):
        p.draw_rectangle(
            0, 0, p.get_screen_width(), p.get_screen_height(), SCREEN_BACKGROUND
        )
        p.draw_text(
            "Game Over",
            p.get_screen_width()//2 - 70,
            p.get_screen_height()//2 - 30,
            40,
            p.BLACK,
        )
        p.draw_text(
            "Press 'Enter' to restart",
            p.get_screen_width()//2 - 130,
            p.get_screen_height()//2 + 20,
            30,
            p.BLACK,
        )
        
        if p.is_key_pressed(p.KeyboardKey.KEY_ENTER):
            self.lives = 5
            self.game_won = False
            self.paddle = Paddle()
            self.ball = Ball()
            self.bricks = Bricks()

def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    game = Game()

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        if not game.game_over:
            game.draw()
            game.update()
        elif game.game_won:
            game.game_won_menu()
        elif game.game_over:
            game.game_over_menu()
            
        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
