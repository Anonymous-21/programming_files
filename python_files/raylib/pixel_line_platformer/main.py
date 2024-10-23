import pyray as p
import os

from xml_parser import spritesheet_xml_parser
from levels import Levels
from player import Player

os.chdir(
    "/home/anonymous/Downloads/programming_files/python_files/raylib/pixel_line_platformer"
)


SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 960
SCREEN_TITLE = "Pixel Line Platformer"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self) -> None:
        self.spritesheet = p.load_texture("assets/pixel_line.png")
        self.spritesheet_xml = "assets/pixel_line.xml"
        self.sprite_dict = spritesheet_xml_parser(self.spritesheet_xml)

        self.rows = 20
        self.cols = 30
        self.block_size = 48

        self.levels = Levels(
            self.spritesheet, self.sprite_dict, self.rows, self.cols, self.block_size
        )
        self.player = Player(self.spritesheet, self.sprite_dict, self.block_size)

    def draw(self):
        self.levels.draw()
        self.player.draw()

    def update(self):
        self.player.update()

        # player collision environment
        for i in range(self.levels.rows):
            for j in range(self.levels.cols):
                x_window = j * self.levels.block_size
                y_window = i * self.levels.block_size

                if self.levels.level[i][j] in [3, 4, 5, 6, 7, 8, 9, 20, 21, 22]:
                    if p.check_collision_recs(
                        (
                            self.player.x_window,
                            self.player.y_window,
                            self.player.current_frame_width * 3,
                            self.player.current_frame_height * 3,
                        ),
                        (
                            x_window,
                            y_window,
                            self.levels.block_size,
                            self.levels.block_size,
                        ),
                    ):
                        self.player.y_window = (
                            y_window - self.player.current_frame_height * 3
                        )
                        if self.player.change_y > 0:
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
