from pyray import *


class Ground:
    def __init__(self, spritesheet, sprite_dict):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.ground = {
            1: self.sprite_dict["groundDirt.png"],
            2: self.sprite_dict["groundGrass.png"],
            3: self.sprite_dict["groundSnow.png"],
            4: self.sprite_dict["groundIce.png"],
            5: self.sprite_dict["groundRock.png"],
        }
        self.frame_num = 1
        self.current_ground = self.ground[self.frame_num]

        self.width = self.current_ground[2]
        self.height = self.current_ground[3]

        self.x1_window = 0
        self.y1_window = get_screen_height() - self.height
        self.x2_window = self.width
        self.y2_window = get_screen_height() - self.height
        self.speed = 4

        self.line_strip = [
            (0, 445 + 120),
            (29, 443 + 120),
            (37, 451 + 120),
            (88, 455 + 120),
            (129, 443 + 120),
            (153, 417 + 120),
            (245, 413 + 120),
            (303, 437 + 120),
            (346, 436 + 120),
            (370, 422 + 120),
            (432, 421 + 120),
            (466, 453 + 120),
            (505, 454 + 120),
            (530, 464 + 120),
            (569, 464 + 120),
            (594, 437 + 120),
            (632, 434 + 120),
            (654, 413 + 120),
            (740, 410 + 120),
            (759, 436 + 120),
            (800, 445 + 120),
        ]

    def draw(self):
        draw_texture_rec(
            self.spritesheet,
            self.current_ground,
            (self.x1_window, self.y1_window),
            WHITE,
        )
        draw_texture_rec(
            self.spritesheet,
            self.current_ground,
            (self.x2_window, self.y2_window),
            WHITE,
        )

        draw_line_strip(self.line_strip,
                        len(self.line_strip),
                        BLACK)

    def animation(self, score, change_season_score):
        # update current frame
        self.current_ground = self.ground[self.frame_num]

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
