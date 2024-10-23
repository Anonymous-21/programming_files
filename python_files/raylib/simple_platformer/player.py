import pyray as p

class Player:
    def __init__(self, spritesheet, sprite_dict) -> None:
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.player_idle = self.sprite_dict["tile_0045.png"]
        
        self.x_window = 20
        self.y_window = p.get_screen_height() - 95
        self.change_x = 5
        self.change_y = 0
        self.gravity = 1
        self.jump_force = -20
        self.can_jump = True
        
        self.current_frame = self.player_idle
        self.current_frame_width = self.current_frame[2]
        self.current_frame_height = self.current_frame[3]

    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.current_frame[0], self.current_frame[1], self.current_frame_width, self.current_frame_height),
                           (self.x_window, self.y_window, self.current_frame_width * 3, self.current_frame_height * 3),
                           (self.current_frame_width/2, self.current_frame_height/2),
                           0,
                           p.WHITE)
        
    def update(self):
        # horizontal movement
        if p.is_key_down(p.KeyboardKey.KEY_RIGHT):
            self.x_window += self.change_x
        elif p.is_key_down(p.KeyboardKey.KEY_LEFT):
            self.x_window -= self.change_x
            
        # vertical movement
        if p.is_key_pressed(p.KeyboardKey.KEY_SPACE) and self.can_jump:
            self.change_y = self.jump_force
            self.can_jump = False
        
        self.change_y += self.gravity
        self.y_window += self.change_y
        
