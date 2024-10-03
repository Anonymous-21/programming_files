import pygame


class Ball:
    def __init__(self, screen, screen_width, screen_height) -> None:
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.radius = 10
        self.x = self.screen_width/2
        self.y = self.screen_height/2
        self.color = "red"
        self.speed_x = 5
        self.speed_y = 6
        
    def draw(self):
        pygame.draw.circle(self.screen,
                           self.color,
                           (self.x, self.y),
                           self.radius)
        
    def update(self):
        # move ball
        self.x += self.speed_x
        self.y += self.speed_y
        
        if self.x <= self.radius or self.x >= self.screen_width - self.radius:
            self.speed_x *= -1
        elif self.y <= self.radius or self.y >= self.screen_height - self.radius:
            self.speed_y *= -1
            
        