from pyray import *


class Ball:
    def __init__(self) -> None:
        self.radius = 10
        self.initial_x = get_screen_width()//2
        self.initial_y = get_screen_height()//2 - self.radius
        self.x = self.initial_x
        self.y = self.initial_y
        self.color = RED
        self.change_x = 5
        self.change_y = 6
        self.frames_counter = 0
        
    def draw(self):
        draw_circle(self.x,
                    self.y,
                    self.radius,
                    self.color)
        
    def ball_reset(self):
        self.x = self.initial_x
        self.y = self.initial_y
        self.change_x *= -1
        self.frames_counter = 0
        
    def move(self, score_left, score_right):
        # move ball with 1 sex delay
        self.frames_counter += 1
        if self.frames_counter > 60:
            self.x += self.change_x
            self.y += self.change_y
        
        # increase scores at x coordinates
        if self.x <= 0:
            score_right += 1
            self.ball_reset()
        elif self.x >= get_screen_width() - self.radius:
            score_left += 1
            self.ball_reset()
        
        # bounce back ball on y coordinates
        if self.y <= 0 or self.y >= get_screen_height() - self.radius:
            self.change_y *= -1
            
        return (score_left, score_right)