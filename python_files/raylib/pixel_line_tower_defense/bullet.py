import pyray as p


class Bullet:
    def __init__(
        self, spritesheet, sprite_dict, block_size, player_x, player_y
    ) -> None:
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict
        self.block_size = block_size

        self.gun_flash = self.sprite_dict["tile_0043.png"]
        self.bullet = self.sprite_dict["tile_0044.png"]

        self.frames_counter = 0
        self.frames_speed = 30

        self.list = []
        self.update(player_x, player_y)
        self.speed = 2
        self.rotation = 0

    def draw(self):
        for bullet in self.list:
            p.draw_texture_pro(
                self.spritesheet,
                (
                    self.gun_flash[0],
                    self.gun_flash[1],
                    self.gun_flash[2],
                    self.gun_flash[3],
                ),
                (
                    self.gun_flash_x_window,
                    self.gun_flash_y_window,
                    self.block_size,
                    self.block_size,
                ),
                (0, 0),
                0,
                p.WHITE,
            )
            p.draw_texture_pro(
                self.spritesheet,
                (self.bullet[0], self.bullet[1], self.bullet[2], self.bullet[3]),
                (bullet[0], bullet[1], self.block_size, self.block_size),
                (0, 0),
                self.rotation,
                p.WHITE,
            )

    def update(self, player_x, player_y):

        # update gun flash position
        self.gun_flash_x_window = player_x + self.block_size + 15
        self.gun_flash_y_window = player_y + self.block_size / 2
        # update bullet position
        self.bullet_x_window = self.gun_flash_x_window + self.block_size
        self.bullet_y_window = self.gun_flash_y_window
        # add new bullet
        self.frames_counter += 1
        if self.frames_counter % self.frames_speed == 0:
            self.frames_counter = 0
            self.list.append([self.bullet_x_window, self.bullet_y_window])
        # move bullet and remove offscreen bullet from list
        for bullet in self.list:
            bullet[0] += self.speed
            if bullet[0] >= p.get_screen_width() + self.block_size:
                self.list.remove(bullet)
