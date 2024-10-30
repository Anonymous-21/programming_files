import pyray as p
import os

from spritesheet_xml_parser import xml_parser
from map import Map
from player import Player
from bullet import Bullet
from enemy import Enemy

os.chdir(
    "/home/anonymous/Downloads/programming_files/python_files/raylib/pixel_line_tower_defense"
)

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
SCREEN_TITLE = "Pixel Line Defense"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self) -> None:
        self.spritesheet = p.load_texture("assets/pixel_line.png")
        self.spritesheet_xml = "assets/pixel_line.xml"
        self.sprite_dict = xml_parser(self.spritesheet_xml)

        self.rows = 20
        self.cols = 30
        self.block_size = 32

        self.map = Map(
            self.spritesheet, self.sprite_dict, self.rows, self.cols, self.block_size
        )
        self.player = Player(self.spritesheet, self.sprite_dict, self.block_size)
        self.bullet = Bullet(
            self.spritesheet,
            self.sprite_dict,
            self.block_size,
            self.player.x_window,
            self.player.y_window,
        )
        self.enemy = Enemy(self.spritesheet, self.sprite_dict, self.block_size)

    def draw(self):
        self.map.draw()
        self.player.draw()
        self.bullet.draw()
        self.enemy.draw()

    def update(self):
        # player movement
        self.player.update()
        # player collision ground
        for row in range(self.rows):
            for col in range(self.cols):
                x_window = col * self.block_size
                y_window = row * self.block_size

                if self.map.map[row][col] in [20, 21, 22]:
                    if p.check_collision_recs(
                        (
                            self.player.x_window,
                            self.player.y_window,
                            self.block_size + self.player.extra_size,
                            self.block_size + self.player.extra_size,
                        ),
                        (x_window, y_window, self.block_size, self.block_size),
                    ):
                        if self.player.y_window <= y_window:
                            self.player.y_window = (
                                y_window - self.block_size - self.player.extra_size
                            )
                            if self.player.change_y > 0:
                                self.player.change_y = 0
                            self.player.can_jump = True
        # update bullet
        self.bullet.update(self.player.x_window, self.player.y_window)
        # update enemy
        self.enemy.update()


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
