import pyray as p


class Player:
    def __init__(self, spritesheet, sprite_dict, block_size) -> None:
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict
        self.block_size = block_size

        self.player_idle = self.sprite_dict["tile_0040.png"]
        self.player_jumping = self.sprite_dict["tile_0041.png"]
        self.player_shooting = self.sprite_dict["tile_0042.png"]
        self.extra_size = 16

        self.current_frame = self.player_idle
        self.x_window = 20
        self.y_window = 20
        self.rotation = 0
        self.tint = p.WHITE
        self.change_y = 0
        self.jump_force = -15
        self.gravity = 1
        self.can_jump = False

    def draw(self):
        p.draw_texture_pro(
            self.spritesheet,
            (
                self.current_frame[0],
                self.current_frame[1],
                self.current_frame[2],
                self.current_frame[3],
            ),
            (
                self.x_window,
                self.y_window,
                self.block_size + self.extra_size,
                self.block_size + self.extra_size,
            ),
            (0, 0),
            self.rotation,
            self.tint,
        )

    def update(self):
        if p.is_key_pressed(p.KeyboardKey.KEY_W) and self.can_jump:
            self.change_y = self.jump_force
            self.can_jump = False
        elif p.is_key_pressed(p.KeyboardKey.KEY_S) and self.can_jump:
            self.y_window += self.block_size * 2 + self.extra_size

        # collision with ceiling
        if self.y_window <= 0:
            self.y_window = 0

        self.change_y += self.gravity
        self.y_window += self.change_y
