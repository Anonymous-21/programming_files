import pyray as p

class Player:
    def __init__(self, spritesheet, sprite_dict) -> None:
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.player_idle = self.sprite_dict["tile_0045.png"]

    def draw(self):
        p.draw_texture_pro(self.spritesheet,
                           (self.player_idle[0], self.player_idle[1], self.player_idle[2], self.player_idle[3]),
                           (20, p.get_screen_height() - 90, self.player_idle[2] * 3, self.player_idle[3] * 3),
                           (self.player_idle[2]/2, self.player_idle[3]/2),
                           0,
                           p.WHITE)
