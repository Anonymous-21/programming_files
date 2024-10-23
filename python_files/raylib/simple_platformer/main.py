import pyray as p
import os

from xml_parser import xml_parser
from levels import Levels
from player import Player

os.chdir(
    "/home/anonymous/Downloads/programming_files/python_files/raylib/simple_platformer"
)


SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 960
SCREEN_TITLE = "Simple Platformer"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self) -> None:
        self.spritesheet = p.load_texture("assets/pixel_line.png")
        self.spritesheet_xml = "assets/pixel_line.xml"
        self.sprite_dict = xml_parser(self.spritesheet_xml)

        self.levels = Levels(self.spritesheet, self.sprite_dict)
        self.player = Player(self.spritesheet, self.sprite_dict)

    def draw(self):
        self.levels.draw()
        self.player.draw()

    def update(self):
        self.player.update()

        # player collision environment
        for i in range(self.levels.rows):
            for j in range(self.levels.cols):
                x = j * self.levels.block_size
                y = j * self.levels.block_size

                if self.levels.level[i][j] in self.levels.level1_one_digit:
                    self.current_sprite = self.sprite_dict[
                        f"tile_000{self.levels.level[i][j]}.png"
                    ]
                else:
                    self.current_sprite = self.sprite_dict[
                        f"tile_00{self.levels.level[i][j]}.png"
                    ]

                if self.levels.level[i][j] in [20, 21, 22]:
                    if p.check_collision_recs(
                        (x, y, self.current_sprite[2], self.current_sprite[3]),
                        (
                            self.player.x_window,
                            self.player.y_window,
                            self.player.current_frame_width,
                            self.player.current_frame_height,
                        ),
                    ):
                        self.player.y_window = (
                            self.current_sprite[1] - self.player.current_frame[3]
                        )
                        self.player.change_y = 0
                        self.player.can_jump = True


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    game = Game()

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        game.draw()
        game.update()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
