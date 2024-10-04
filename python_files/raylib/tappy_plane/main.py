from pyray import *
import os

from spritesheet_xml_parser import xml_parser
from plane import Plane
from background import Background

os.chdir("/home/anonymous/Downloads/programming_files/python_files/raylib/tappy_plane")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480
SCREEN_TITLE = "TAPPY PLANE"
SCREEN_BACKGROUND = RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self):
        self.game_over =False
        
        self.spritesheet = load_texture(
            "assets/sheet.png"
        )
        self.spritesheet_xml = "assets/sheet.xml"
        self.sprite_dict = xml_parser(self.spritesheet_xml)

        self.plane = Plane(self.spritesheet, self.sprite_dict)
        self.background = Background(self.spritesheet,
                                     self.sprite_dict)

    def draw(self):
        self.background.draw()
        self.plane.draw()

    def update(self):
        self.background.animation()
        self.plane.update()
        self.plane.jump()

    def game_over_menu(self):
        pass


def main():
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    set_target_fps(GAME_FPS)

    game = Game()

    while not window_should_close():
        begin_drawing()
        clear_background(SCREEN_BACKGROUND)

        if not game.game_over:
            game.draw()
            game.update()
        else:
            game.game_over_menu()
        
        end_drawing()

    close_window()


if __name__ == "__main__":
    main()
        
