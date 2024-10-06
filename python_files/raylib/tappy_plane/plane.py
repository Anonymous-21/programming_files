import pyray as pr


class Plane:
    def __init__(self, spritesheet, sprite_dict):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.plane_blue = {
            1: self.sprite_dict["planeBlue1.png"],
            2: self.sprite_dict["planeBlue2.png"],
            3: self.sprite_dict["planeBlue3.png"],
        }
        self.plane_green = {
            1: self.sprite_dict["planeGreen1.png"],
            2: self.sprite_dict["planeGreen2.png"],
            3: self.sprite_dict["planeGreen3.png"],
        }
        self.plane_red = {
            1: self.sprite_dict["planeRed1.png"],
            2: self.sprite_dict["planeRed2.png"],
            3: self.sprite_dict["planeRed3.png"],
        }
        self.plane_yellow = {
            1: self.sprite_dict["planeYellow1.png"],
            2: self.sprite_dict["planeYellow2.png"],
            3: self.sprite_dict["planeYellow3.png"],
        }
        self.frame_num = 1
        self.current_frame = self.plane_blue[self.frame_num]
        self.width = self.current_frame[2]
        self.height = self.current_frame[3]
        self.x_window = self.width
        self.y_window = self.height
        self.tint = pr.WHITE

        self.change_y = 0
        self.jump_force = -10
        self.gravity = 1

        self.frames_speed = 8
        self.frames_counter = 0

    def draw(self):
        pr.draw_texture_rec(
            self.spritesheet,
            self.current_frame,
            (self.x_window, self.y_window),
            self.tint,
        )

    def update(self):
        # update current frame
        self.current_frame = self.plane_blue[self.frame_num]

        # plane animation
        self.frames_counter += 1
        if self.frames_counter >= self.frames_speed:
            self.frames_counter = 0
            self.frame_num += 1
            if self.frame_num > 3:
                self.frame_num = 1

    def jump(self):
        if pr.is_key_pressed(pr.KeyboardKey.KEY_UP):
            self.change_y = self.jump_force

        self.change_y += self.gravity
        self.y_window += self.change_y
