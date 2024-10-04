from pyray import *


class Paddle:
    def __init__(self, x):
        self.width = 10
        self.height = 100
        self.x = x
        self.y = get_screen_height()//2 - self.height//2
        self.color = BLACK
        self.speed = 8
        
    def draw(self):
        draw_rectangle(self.x,
                       self.y,
                       self.width,
                       self.height,
                       self.color)

    def move(self, key_up, key_down):
        if is_key_down(key_up) and self.y >= 0:
            self.y -= self.speed
        elif is_key_down(key_down) and self.y <= get_screen_height() - self.height:
            self.y += self.speed