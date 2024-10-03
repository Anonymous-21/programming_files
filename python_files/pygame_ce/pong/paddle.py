import pygame


class Paddle:
    def __init__(self, screen, screen_width, screen_height) -> None:
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width = 10
        self.height = 100
        self.left_x = 10
        self.left_y = self.screen_height / 2 - self.height/2
        self.right_x = self.screen_width - self.width - 10
        self.right_y = self.screen_height / 2 - self.height/2
        self.speed = 8
        self.color = "black"
        self.left_rect = pygame.Rect(self.left_x, self.left_y, self.width, self.height)
        self.right_rect = pygame.Rect(self.right_x, self.right_y, self.width, self.height)

    def draw(self):
        # left paddle
        pygame.draw.rect(
            self.screen,
            self.color,
            self.left_rect
        )
        
        # right paddle
        pygame.draw.rect(
            self.screen,
            self.color,
            self.right_rect
        )

    def update(self):
        # update rect values
        self.left_rect = pygame.Rect(self.left_x, self.left_y, self.width, self.height)
        self.right_rect = pygame.Rect(self.right_x, self.right_y, self.width, self.height)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.left_y >= 0:
            self.left_y -= self.speed
        elif keys[pygame.K_s] and self.left_y <= self.screen_height - self.height:
            self.left_y += self.speed
        elif keys[pygame.K_UP] and self.right_y >= 0:
            self.right_y -= self.speed
        elif keys[pygame.K_DOWN] and self.right_y <= self.screen_height - self.height:
            self.right_y += self.speed