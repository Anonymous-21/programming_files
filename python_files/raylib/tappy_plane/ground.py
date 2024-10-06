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

        collision_rect_list = [
            [0, 445, 35, 35],
            [35, 450, 120, 30],
            [155, 417, 100, 64],
            [255, 435, 117, 45],
            [372, 422, 60, 58],
            [432, 454, 73, 26],
            [505, 465, 90, 15],
            [595, 434, 60, 46],
            [655, 411, 85, 69],
            [740, 435, 60, 45],
        ]
        collision_triangle_list = [
            {
                1: [155, 417],
                2: [115, 452],
                3: [155, 452],
            },
            {
                1: [255, 415],
                2: [255, 435],
                3: [299, 435],
            },
            {
                1: [372, 422],
                2: [348, 436],
                3: [372, 436],
            },
            {
                1: [432, 420],
                2: [432, 454],
                3: [468, 454],
            },
            {
                1: [505, 455],
                2: [505, 465],
                3: [535, 465],
            },
            {
                1: [595, 434],
                2: [568, 464],
                3: [595, 464],
            },
            {
                1: [655, 411],
                2: [634, 433],
                3: [655, 433],
            },
            {
                1: [740, 408],
                2: [740, 435],
                3: [762, 435],
            },
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
