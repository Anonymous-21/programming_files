import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = (800, 600)
SCREEN_TITLE = "BASIC WINDOW"
SCREEN_BACKGROUND = "white"
GAME_FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

ball_radius = 10
ball_x = SCREEN_WIDTH/2 - ball_radius
ball_y = SCREEN_HEIGHT/2 - ball_radius
ball_color = "red"
ball_speed = 8

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            
    screen.fill(SCREEN_BACKGROUND)
    pygame.display.set_caption(SCREEN_TITLE)
    
    pygame.draw.circle(screen,
                       ball_color,
                       (ball_x, ball_y),
                       ball_radius)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y >= ball_radius:
        ball_y -= ball_speed
    elif keys[pygame.K_DOWN] and ball_y <= SCREEN_HEIGHT - ball_radius:
        ball_y += ball_speed
    elif keys[pygame.K_RIGHT] and ball_x <= SCREEN_WIDTH - ball_radius:
        ball_x += ball_speed
    elif keys[pygame.K_LEFT] and ball_x >= ball_radius:
        ball_x -= ball_speed
    
    pygame.display.flip()
    clock.tick(GAME_FPS)
    
pygame.quit()