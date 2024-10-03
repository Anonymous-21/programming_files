import pygame


class Ball:
    def __init__(self, screen, screen_width, screen_height) -> None:
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.radius = 10
        self.initial_x = self.screen_width/2
        self.initial_y = self.screen_height/2
        self.x = self.initial_x
        self.y = self.initial_y
        self.color = "red"
        self.speed_x = 5
        self.speed_y = 6
        
        self.frames_counter = 0
        
    def draw(self):
        pygame.draw.circle(self.screen,
                           self.color,
                           (self.x, self.y),
                           self.radius)
        
    def reset_ball(self):
        self.x = self.initial_x
        self.y = self.initial_y
        
    def update(self, left_score, right_score):
        # move ball with 2 seconds delay
        self.frames_counter += 1
        if self.frames_counter > 120:
            self.x += self.speed_x
            self.y += self.speed_y
        
        if self.x <= self.radius:
            right_score += 1
            self.reset_ball()
        elif self.x >= self.screen_width - self.radius:
            left_score += 1
            self.reset_ball()
        elif self.y <= self.radius or self.y >= self.screen_height - self.radius:
            self.speed_y *= -1
            
        return (left_score, right_score)
            
        