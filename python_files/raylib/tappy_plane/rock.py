from pyray import *


class Rock:
    def __init__(self, spritesheet, sprite_dict):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.rock = {
            1: "rock.png",
            2: "rockGrass.png",
            3: "rockSnow.png",
            4: "rockIce.png",
        }
        self.rock_down = {
            1: "rockDown.png",
            2: "rockGrassDown.png",
            3: "rockSnowDown.png",
            4: "rockIceDown.png",
        }

        self.frame_num = 1
        self.current_rock = self.sprite_dict[self.rock[self.frame_num]]
        self.current_rock_down = self.sprite_dict[self.rock_down[self.frame_num]]
        self.width = self.current_rock[2]
        self.height = self.current_rock[3]
        self.x1_window = get_screen_width() / 2
        self.y1_window = get_screen_height() - self.height
        self.gap_between_rocks = 400  # 400
        self.x2_window = self.x1_window + self.gap_between_rocks
        self.y2_window = 0

        self.speed = 4

        # triangles for collision detection
        self.triangle1 = {
            1: (self.x1_window + self.width / 2 + 8, self.y1_window),
            2: (self.x1_window, self.y1_window + self.height),
            3: (self.x1_window + self.width, self.y1_window + self.height),
        }
        self.triangle2 = {
            1: (self.x2_window, self.y2_window),
            2: (self.x2_window + self.width / 2 + 8, self.y2_window + self.height),
            3: (self.x2_window + self.width, self.y2_window),
        }

    def draw(self):
        # draw triangles
        # rock
        draw_triangle_lines(
            self.triangle1[1], self.triangle1[2], self.triangle1[3], BLACK
        )
        # rock down
        draw_triangle_lines(
            self.triangle2[1], self.triangle2[2], self.triangle2[3], BLACK
        )

        # rock
        draw_texture_rec(
            self.spritesheet, self.current_rock, (self.x1_window, self.y1_window), WHITE
        )

        # rock down
        draw_texture_rec(
            self.spritesheet,
            self.current_rock_down,
            (self.x2_window, self.y2_window),
            WHITE,
        )

    def animation(self, score, change_season_score):
        # update rocks
        self.current_rock = self.sprite_dict[self.rock[self.frame_num]]
        self.current_rock_down = self.sprite_dict[self.rock_down[self.frame_num]]

        # update triangles
        self.triangle1 = {
            1: (self.x1_window + self.width / 2 + 13, self.y1_window),
            2: (self.x1_window, self.y1_window + self.height),
            3: (self.x1_window + self.width, self.y1_window + self.height),
        }
        self.triangle2 = {
            1: (self.x2_window, self.y2_window),
            2: (self.x2_window + self.width / 2 + 13, self.y2_window + self.height),
            3: (self.x2_window + self.width, self.y2_window),
        }

        # move rocks
        self.x1_window -= self.speed
        self.x2_window -= self.speed

        if self.x1_window < -self.width:
            self.x1_window = get_screen_width() + self.width
        elif self.x2_window < -self.width:
            self.x2_window = self.x1_window + self.gap_between_rocks + self.width

        # change rocks
        if score % change_season_score == 0:
            self.frame_num += 1
            if self.frame_num > 4:
                self.frame_num = 1
