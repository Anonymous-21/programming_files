import pyray as p
from os import chdir

from utils import spritesheet_xml_parser
from entities.player_ship import PlayerShip

chdir("/home/anonymous/Downloads/programming_files/python_files/raylib/space_survival")


SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Space Survival"
SCREEN_BACKGROUND: p.Color = p.BLACK
GAME_FPS: int = 60


class Game:
    def __init__(self) -> None:
        self.spritesheet: p.Texture = p.load_texture("assets/sheet.png")
        self.spritesheet_xml: str = "assets/sheet.xml"
        self.sprite_dict: dict[str, p.Rectangle] = spritesheet_xml_parser(
            self.spritesheet_xml
        )

        self.player_ship: PlayerShip = PlayerShip(
            self.spritesheet, self.sprite_dict, 5, 1, "blue"
        )

    def draw(self) -> None:
        self.player_ship.draw()

    def update(self) -> None:
        self.player_ship.update(p.get_mouse_x(), p.get_mouse_y())


def main() -> None:
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
