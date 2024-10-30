import pyray as p


class Player:
    def __init__(self, spritesheet, sprite_dict, block_size) -> None:
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict
        self.block_size = block_size

        self.player_idle = self.sprite_dict["tile_0040.png"]
        self.player_shooting = self.sprite_dict["tile_0042.png"]

        self.current_frame = self.player_idle
        self.x_window = 20
        self.y_window = 20
        self.rotation = 0
        self.tint = p.WHITE

    def draw(self):
        p.draw_texture_pro(
            self.spritesheet,
            (
                self.current_frame[0],
                self.current_frame[1],
                self.current_frame[2],
                self.current_frame[3],
            ),
            (self.x_window, self.y_window, self.block_size + 16, self.block_size + 16),
            (0, 0),
            self.rotation,
            self.tint,
        )
