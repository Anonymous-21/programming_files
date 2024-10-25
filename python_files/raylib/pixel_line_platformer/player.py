import pyray as p


class Player:
    def __init__(self, spritesheet, sprite_dict, block_size) -> None:
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict
        self.block_size = block_size

        self.player_idle = self.sprite_dict["tile_0045.png"]
        self.player_jump = self.sprite_dict["tile_0046.png"]
        self.player_gun_idle = self.sprite_dict["tile_0040.png"]
        self.player_gun_jump = self.sprite_dict["tile_0041.png"]
        self.player_gun_land = self.sprite_dict["tile_0042.png"]

        self.current_frame = self.player_idle
        self.frame_num = 1
        self.frames_counter = 0
        self.frames_speed = 8

        self.x_window = 10
        self.y_window = p.get_screen_height() - (self.block_size * 2)
        self.change_x = 5
        self.change_y = 0
        self.gravity = 1
        self.jump_force = -15
        self.moving = False
        self.have_gun = False
        self.can_jump = True

        self.collision_rec_x = self.x_window
        self.collision_rec_y = self.y_window
        self.collision_rec_width = self.block_size
        self.collision_rec_height = self.block_size
        self.collision_rec_color = p.BLACK

    def draw(self):
        if p.is_key_down(p.KeyboardKey.KEY_LEFT):
            p.draw_texture_pro(
                self.spritesheet,
                (
                    self.current_frame[0],
                    self.current_frame[1],
                    -self.current_frame[2],
                    self.current_frame[3],
                ),
                (self.x_window, self.y_window, self.block_size, self.block_size),
                (0, 0),
                0,
                p.WHITE,
            )
        else:
            p.draw_texture_pro(
                self.spritesheet,
                (
                    self.current_frame[0],
                    self.current_frame[1],
                    self.current_frame[2],
                    self.current_frame[3],
                ),
                (self.x_window, self.y_window, self.block_size, self.block_size),
                (0, 0),
                0,
                p.WHITE,
            )

        p.draw_rectangle_lines_ex(
            (
                self.collision_rec_x,
                self.collision_rec_y,
                self.collision_rec_width,
                self.collision_rec_height,
            ),
            1,
            self.collision_rec_color,
        )

    def update(self):
        # update current frame
        match self.frame_num:
            case 1:
                self.current_frame = self.player_idle
            case 2:
                self.current_frame = self.player_jump
            case 3:
                self.current_frame = self.player_gun_idle
            case 4:
                self.current_frame = self.player_gun_jump
            case 5:
                self.current_frame = self.player_gun_land

        # player movement
        if (
            p.is_key_down(p.KeyboardKey.KEY_LEFT)
            and p.is_key_pressed(p.KeyboardKey.KEY_UP)
            and self.can_jump
            and self.x_window >= 0
        ):
            self.moving = True
            self.x_window -= self.change_x
            self.change_y = self.jump_force
            self.can_jump = False
        elif (
            p.is_key_down(p.KeyboardKey.KEY_RIGHT)
            and p.is_key_pressed(p.KeyboardKey.KEY_UP)
            and self.can_jump
            and self.x_window <= p.get_screen_width() - self.block_size
        ):
            self.moving = True
            self.x_window += self.change_x
            self.change_y = self.jump_force
            self.can_jump = False
        elif p.is_key_down(p.KeyboardKey.KEY_LEFT) and self.x_window >= 0:
            self.moving = True
            self.x_window -= self.change_x
        elif (
            p.is_key_down(p.KeyboardKey.KEY_RIGHT)
            and self.x_window <= p.get_screen_width() - self.block_size
        ):
            self.moving = True
            self.x_window += self.change_x
        elif p.is_key_pressed(p.KeyboardKey.KEY_UP) and self.can_jump:
            self.can_jump = False
            self.change_y = self.jump_force
        else:
            self.moving = False
            if not self.have_gun:
                self.frame_num = 1
            elif self.have_gun:
                self.frame_num = 3

        self.change_y += self.gravity
        self.y_window += self.change_y

        # update collision rec values
        self.collision_rec_x = self.x_window
        self.collision_rec_y = self.y_window
        self.collision_rec_width = self.block_size
        self.collision_rec_height = self.block_size

        # player animation
        self.frames_counter += 1
        if self.frames_counter >= self.frames_speed:
            self.frames_counter = 0
            self.frame_num += 1
            if self.frame_num > 2 and not self.have_gun:
                self.frame_num = 1
            elif self.frame_num > 5 and self.have_gun:
                self.frame_num = 3
