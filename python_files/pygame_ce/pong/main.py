import pygame

from paddle import Paddle
from ball import Ball

SCREEN_WIDTH, SCREEN_HEIGHT = (800, 600)
SCREEN_TITLE = "PONG"
SCREEN_BACKGROUND = "white"
GAME_FPS = 60


class Game:
    def __init__(self, screen) -> None:
        self.screen = screen
        
        self.game_over = False
        self.left_score = 0
        self.right_score = 0
        
        self.paddle = Paddle(self.screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.ball = Ball(self.screen, SCREEN_WIDTH, SCREEN_HEIGHT)

    def draw(self):
        # draw screen divider
        pygame.draw.line(self.screen,
                         "gray",
                         (SCREEN_WIDTH/2, 0),
                         (SCREEN_WIDTH/2, SCREEN_HEIGHT),
                         width=5)
        
        self.paddle.draw()
        self.ball.draw()

    def update(self):
        self.paddle.update()
        self.paddle.move()
        self.ball.update()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(SCREEN_TITLE)
    clock = pygame.time.Clock()
    running = True

    game = Game(screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(SCREEN_BACKGROUND)

        game.draw()
        game.update()

        pygame.display.flip()
        clock.tick(GAME_FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
