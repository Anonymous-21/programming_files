import pygame

from paddle import Paddle
from ball import Ball

SCREEN_WIDTH, SCREEN_HEIGHT = (800, 600)
SCREEN_TITLE = "PONG"
SCREEN_BACKGROUND = "white"
GAME_FPS = 60


def draw_font(screen, text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


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
        self.left_score, self.right_score = self.ball.update(self.left_score, self.right_score)
        
        # ball and paddle collision

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(SCREEN_TITLE)
    clock = pygame.time.Clock()
    running = True

    game = Game(screen)
    font = pygame.font.SysFont("Ariel", 40)
    font_color = "black"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(SCREEN_BACKGROUND)
        
        # draw left score
        draw_font(screen,
                  str(game.left_score),
                  font,
                  font_color,
                  SCREEN_WIDTH/2 - 50,
                  20)
        # draw right score
        draw_font(screen,
                  str(game.right_score),
                  font,
                  font_color,
                  SCREEN_WIDTH/2 + 35,
                  20)

        game.draw()
        game.update()

        pygame.display.flip()
        clock.tick(GAME_FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
