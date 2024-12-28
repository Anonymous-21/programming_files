import pyray as p
from os import chdir

from utils import xml_parser
from background import Background
from player import Player
from enemy_list import EnemyList
from collision_handler import Collision_handler

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Simple Space Survival"
SCREEN_BACKGROUND: p.Color = p.BLACK
GAME_FPS: int = 60


class Game:
    def __init__(self) -> None:
        chdir(
            "/home/anonymous/Downloads/programming_files/python_files/raylib/simple_space_survival"
        )
        self.spritesheet: p.Texture = p.load_texture("assets/simpleSpace_sheet.png")
        self.spritesheet_xml: str = "assets/simpleSpace_sheet.xml"
        self.sprite_dict: dict[str, p.Rectangle] = xml_parser(self.spritesheet_xml)

        self.background: Background = Background(self.spritesheet, self.sprite_dict)
        self.player: Player = Player(self.spritesheet, self.sprite_dict)
        self.enemy_list: EnemyList = EnemyList()
        self.collision_handler: Collision_handler = Collision_handler(
            self.player, self.enemy_list
        )

    def draw(self) -> None:
        self.background.draw()
        self.player.draw()
        self.enemy_list.draw()

    def update(self) -> None:
        self.background.update()
        self.player.update()
        self.enemy_list.update(
            self.spritesheet, self.sprite_dict, self.player.dest.x, self.player.dest.y
        )

        self.collision_handler.enemy_collision_bullet()


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    game: Game = Game()

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        game.draw()
        game.update()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
