import pygame


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_TITLE = "Pong"
SCREEN_BACKGROUND = "white"
GAME_FPS = 60


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(SCREEN_BACKGROUND)
    
    pygame.display.flip()
    
    clock.tick(GAME_FPS)
    
pygame.quit()