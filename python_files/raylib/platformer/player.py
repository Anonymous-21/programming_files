import raylib as r


class Player:
    def __init__(self, sprite_dict, spritesheet) -> None:
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict
        
        self.alien_biege = {
            1: "alienBeige_front.png",
            2: "alienBeige_stand.png",
            3: "alienBeige_walk1.png",
            4: "alienBeige_walk2.png",
            5: "alienBeige_jump.png",
            6: "alienBeige_duck.png",
            7: "alienBeige_hit.png",
            8: "alienBeige_climb1.png",
            9: "alienBeige_climb2.png",
            10: "alienBeige_swim1.png",
            11: "alienBeige_swim2.png",
        }
        self.alien_blue = {
            1: "alienBlue_front.png",
            2: "alienBlue_stand.png",
            3: "alienBlue_walk1.png",
            4: "alienBlue_walk2.png",
            5: "alienBlue_jump.png",
            6: "alienBlue_duck.png",
            7: "alienBlue_hit.png",
            8: "alienBlue_climb1.png",
            9: "alienBlue_climb2.png",
            10: "alienBlue_swim1.png",
            11: "alienBlue_swim2.png",
        }
        self.alien_green = {
            1: "alienGreen_front.png",
            2: "alienGreen_stand.png",
            3: "alienGreen_walk1.png",
            4: "alienGreen_walk2.png",
            5: "alienGreen_jump.png",
            6: "alienGreen_duck.png",
            7: "alienGreen_hit.png",
            8: "alienGreen_climb1.png",
            9: "alienGreen_climb2.png",
            10: "alienGreen_swim1.png",
            11: "alienGreen_swim2.png",
        }
        self.alien_pink = {
            1: "alienPink_front.png",
            2: "alienPink_stand.png",
            3: "alienPink_walk1.png",
            4: "alienPink_walk2.png",
            5: "alienPink_jump.png",
            6: "alienPink_duck.png",
            7: "alienPink_hit.png",
            8: "alienPink_climb1.png",
            9: "alienPink_climb2.png",
            10: "alienPink_swim1.png",
            11: "alienPink_swim2.png",
        }
        self.alien_yellow = {
            1: "alienYellow_front.png",
            2: "alienYellow_stand.png",
            3: "alienYellow_walk1.png",
            4: "alienYellow_walk2.png",
            5: "alienYellow_jump.png",
            6: "alienYellow_duck.png",
            7: "alienYellow_hit.png",
            8: "alienYellow_climb1.png",
            9: "alienYellow_climb2.png",
            10: "alienYellow_swim1.png",
            11: "alienYellow_swim2.png",
        }
        
        self.frames_counter = 0
        self.frames_speed = 8
        self.frame_num = 1
        self.current_frame = self.alien_blue[self.frame_num]

    def draw(self):
        r.DrawTextureRec(self.spritesheet,
                         self.sprite_dict[self.current_frame],
                         (r.GetScreenWidth()//2,
                          r.GetScreenHeight()//2),
                         r.WHITE)
        
    def update(self):
        self.frames_counter += 1
        if self.frames_counter % self.frames_speed == 0:
            self.frame_num += 1
            if self.frame_num > 11:
                self.frame_num = 1
