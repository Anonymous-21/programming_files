from pyray import *


class Plane:
    def __init__(self, spritesheet, sprite_dict):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.plane_blue = {
            1: "planeBlue1.png",
            2: "planeBlue2.png",
            3: "planeBlue3.png",
        }
        self.plane_green = {
            1: "planeGreen1.png",
            2: "planeGreen2.png",
            3: "planeGreen3.png",
        }
        self.plane_red = {
            1: "planeRed1.png",
            2: "planeRed2.png",
            3: "planeRed3.png",
        }
        self.plane_yellow = {
            1: "planeYellow1.png",
            2: "planeYellow2.png",
            3: "planeYellow3.png",
        }
        self.frame_num = 1
        self.current_frame = self.sprite_dict[self.plane_blue[self.frame_num]]
        self.width = self.current_frame[2]
        self.height = self.current_frame[3]
        self.x_window = self.width
        self.y_window = self.height
        self.tint = WHITE

        self.change_y = 0
        self.jump_force = -10
        self.gravity = 1
        self.is_jumping = False

        self.frames_speed = 8
        self.frames_counter = 0

    def draw(self):
        draw_texture_rec(
            self.spritesheet,
            self.current_frame,
            (self.x_window, self.y_window),
            self.tint,
        )

    def update(self):
        # update current frame
        self.current_frame = self.sprite_dict[self.plane_blue[self.frame_num]]

        # plane animation
        self.frames_counter += 1
        if self.frames_counter >= self.frames_speed:
            self.frames_counter = 0
            self.frame_num += 1
            if self.frame_num > 3:
                self.frame_num = 1

    def jump(self):
        if is_key_pressed(KeyboardKey.KEY_UP):
            self.change_y = self.jump_force
            self.is_jumping = True

        if self.is_jumping:
            self.change_y += self.gravity
            self.y_window += self.change_y
