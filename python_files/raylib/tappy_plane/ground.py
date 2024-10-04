from pyray import *


class Ground:
    def __init__(self, spritesheet, sprite_dict):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.ground = {
            1:"groundDirt.png",
            2:"groundGrass.png",
            3:"groundSnow.png",
            4:"groundIce.png",
            # 5:"groundRock.png",
        }
        self.frame_num = 1
        self.current_ground = self.sprite_dict[self.ground[self.frame_num]]

        self.width = self.current_ground[2]
        self.height = self.current_ground[3]

        self.x1_window = 0
        self.y1_window = get_screen_height() - self.height
        self.x2_window = self.width
        self.y2_window = get_screen_height() - self.height
        self.speed = 2

    def draw(self):
        draw_texture_rec(self.spritesheet,
                         self.current_ground,
                         (self.x1_window, self.y1_window),
                         WHITE)
        draw_texture_rec(self.spritesheet,
                         self.current_ground,
                         (self.x2_window, self.y2_window),
                         WHITE)
        
    def animation(self, score, change_season_score):
        # move ground
        self.x1_window -= self.speed
        self.x2_window -= self.speed
        
        if self.x2_window == 0:
            self.x1_window = self.width
        elif self.x1_window == 0:
            self.x2_window = self.width

        # update frame number
        if score % change_season_score == 0:
            self.frame_num += 1
            if self.frame_num > 4:
                self.frame_num = 1

        # update current frame
        self.current_ground = self.sprite_dict[self.ground[self.frame_num]]
