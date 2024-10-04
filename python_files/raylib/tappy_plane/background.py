from pyray import *


class Background:
    def __init__(self, spritesheet, sprite_dict):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.background = self.sprite_dict["background.png"]
        self.x1_window = 0
        self.y1_window = 0
        self.width = self.background[2]
        self.height = self.background[3]
        self.x2_window = self.width
        self.y2_window = 0
        self.speed = 0.5

    def draw(self):
        draw_texture_rec(
            self.spritesheet, self.background, (self.x1_window, self.y1_window), WHITE
        )
        draw_texture_rec(
            self.spritesheet, self.background, (self.x2_window, self.y2_window), WHITE
        )

    def animation(self):
        self.x1_window -= self.speed
        self.x2_window -= self.speed

        if self.x2_window == 0:
            self.x1_window = self.width
        elif self.x1_window == 0:
            self.x2_window = self.width
