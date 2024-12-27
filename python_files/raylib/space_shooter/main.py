import pyray as p

from spritesheet_xml_parser import xml_parser
from player import Player
from background import Background
from enemy_list import EnemyList

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Space Shooter"
SCREEN_BACKGROUND: p.Color = p.BLACK
GAME_FPS = 60


class Game:
    def __init__(self):
        self.spritesheet = p.load_texture(
            "/home/anonymous/Downloads/programming_files/python_files/raylib/space_shooter/sheet.png"
        )
        self.spritesheet_xml = "/home/anonymous/Downloads/programming_files/python_files/raylib/space_shooter/sheet.xml"
        self.sprite_dict = xml_parser(self.spritesheet_xml)

        self.background = Background(self.spritesheet, self.sprite_dict)
        self.player = Player(self.spritesheet, self.sprite_dict)
        self.enemy_list = EnemyList(self.spritesheet, self.sprite_dict, self.player)

    def draw(self):
        self.background.draw()
        self.player.draw()
        self.enemy_list.draw()

    def update(self):
        self.background.update()
        self.player.update()
        self.enemy_list.update()


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    game = Game()

    while not p.window_should_close():
        game.update()

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        game.draw()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
