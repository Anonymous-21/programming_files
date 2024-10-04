from pyray import *


class Font:
    def __init__(self, spritesheet, sprite_dict):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.game_over = self.sprite_dict["textGameOver.png"]
        self.game_over_width = self.game_over[2]
        self.game_over_height = self.game_over[3]
        self.get_ready = self.sprite_dict["textGetReady.png"]
        self.get_ready_width = self.get_ready[2]
        self.get_ready_height = self.get_ready[3]

    def draw_game_over(self):
        draw_texture_rec(
            self.spritesheet,
            self.game_over,
            (
                get_screen_width() / 2 - self.game_over_width / 2,
                get_screen_height() / 2 - self.game_over_height / 2,
            ),
            WHITE,
        )

    def draw_get_ready(self):
        draw_texture_rec(
            self.spritesheet,
            self.get_ready,
            (
                get_screen_width() / 2 - self.get_ready_width / 2,
                get_screen_height() / 2 - self.get_ready_height / 2,
            ),
            WHITE,
        )
