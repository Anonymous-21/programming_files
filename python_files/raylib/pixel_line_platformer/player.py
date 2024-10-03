import raylib as r


class Player:
    def __init__(self, spritesheet, sprite_dict) -> None:
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.player = {
            1: "tile_0045.png",
            2: "tile_0046.png",
            3: "tile_0040.png",
            4: "tile_0041.png",
            5: "tile_0042.png",
        }
        self.frame_num = 1
        self.current_frame = self.sprite_dict[self.player[self.frame_num]]
        self.ground_level = r.GetScreenHeight() - 85
        self.player_width = self.current_frame[2]
        self.player_height = self.current_frame[3]
        self.player_x_window = 10
        self.player_y_window = self.ground_level
        self.player_scale = 5
        self.player_change_x = 5
        self.player_change_y = 0
        self.jump_force = -20
        self.gravity = 1
        self.look_left = False
        self.is_jumping = False
        self.can_jump = True
        self.run_animation = False

        self.source_rec = (
            self.current_frame[0],
            self.current_frame[1],
            self.current_frame[2],
            self.current_frame[3],
        )

        self.frames_counter = 0
        self.frames_speed = 8

    def draw(self):
        r.DrawTexturePro(
            self.spritesheet,
            self.source_rec,
            (
                self.player_x_window,
                self.player_y_window,
                self.player_width * self.player_scale,
                self.player_height * self.player_scale,
            ),
            (0, 0),
            0,
            r.WHITE,
        )

    def update(self):
        if self.look_left:
            self.source_rec = (
                self.current_frame[0],
                self.current_frame[1],
                -self.current_frame[2],
                self.current_frame[3],
            )
        else:
            self.source_rec = (
                self.current_frame[0],
                self.current_frame[1],
                self.current_frame[2],
                self.current_frame[3],
            )

        if self.run_animation:
            self.frames_counter += 1
            if self.frames_counter >= self.frames_speed:
                self.frames_counter = 0
                self.frame_num += 1
                if self.frame_num > 2:
                    self.frame_num = 1

        self.current_frame = self.sprite_dict[self.player[self.frame_num]]

    def movement(self):
        # move and jump
        if (
            r.IsKeyDown(r.KEY_RIGHT)
            and self.player_x_window
            <= r.GetScreenWidth() - self.player_width * self.player_scale
        ):
            self.player_x_window += self.player_change_x
            self.run_animation = True

            if r.IsKeyPressed(r.KEY_UP) and self.can_jump:
                self.player_change_y = self.jump_force
                self.is_jumping = True

        elif r.IsKeyDown(r.KEY_LEFT) and self.player_x_window >= 0:
            self.player_x_window -= self.player_change_x
            self.look_left = True
            self.run_animation = True

            if r.IsKeyPressed(r.KEY_UP) and self.can_jump:
                self.player_change_y = self.jump_force
                self.is_jumping = True

        elif r.IsKeyPressed(r.KEY_UP) and self.can_jump:
            self.player_change_y = self.jump_force
            self.run_animation = True
            self.is_jumping = True
        else:
            self.look_left = False
            self.run_animation = False
            self.frame_num = 1

        # jumping
        if self.is_jumping:
            self.player_change_y += self.gravity
            self.player_y_window += self.player_change_y
            self.can_jump = False

        # collision with ground
        if self.player_y_window >= self.ground_level:
            self.player_y_window = self.ground_level
            self.can_jump = True
