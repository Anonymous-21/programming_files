import pyray as pr

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
        self.y1_window = pr.get_screen_height() - self.height
        self.x2_window = self.width
        self.y2_window = pr.get_screen_height() - self.height
        self.speed = 4

        self.line_strip = [
            (0, 445),
            (29, 443),
            (37, 451),
            (88, 455),
            (129, 443),
            (153, 417),
            (245, 413),
            (303, 437),
            (346, 436),
            (370, 422),
            (432, 421),
            (466, 453),
            (505, 454),
            (530, 464),
            (569, 464),
            (594, 437),
            (632, 434),
            (654, 413),
            (740, 410),
            (759, 436),
            (800, 445),
        ]

    def draw(self):
        pr.draw_texture_rec(
            self.spritesheet,
            self.current_ground,
            (self.x1_window, self.y1_window),
            pr.WHITE,
        )
        pr.draw_texture_rec(
            self.spritesheet,
            self.current_ground,
            (self.x2_window, self.y2_window),
            pr.WHITE,
        )

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
