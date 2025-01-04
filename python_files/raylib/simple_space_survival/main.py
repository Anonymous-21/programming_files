import pyray as p
from os import chdir

from utils import xml_parser
from player import Player

chdir("python_files/raylib/simple_space_survival")

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Simple Space Survival"
SCREEN_BACKGROUND: p.Color = p.RAYWHITE


class Game:
    def __init__(self) -> None:
        self.spritesheet: p.Texture = p.load_texture("assets/simpleSpace_sheet.png")
        self.spritesheet_xml: str = "assets/simpleSpace_sheet.xml"
        self.sprite_dict: dict[str, p.Rectangle] = xml_parser(self.spritesheet_xml)

        self.background: p.Texture = p.load_texture("assets/background.png")

        self.player: Player = Player(self.spritesheet, self.sprite_dict)

        self.camera = p.Camera2D()
        self.camera.target = p.Vector2(self.player.dest.x, self.player.dest.y)
        self.camera.offset = p.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.camera.rotation = 0.0
        self.camera.zoom = 1.0

    def draw(self) -> None:
        # draw background
        p.draw_texture(self.background, 0, 0, p.WHITE)

        self.player.draw()

    def update(self) -> None:
        # camera follow player
        self.camera.target.x = max(
            p.get_screen_width() / 2,
            min(self.player.dest.x, self.background.width - p.get_screen_width() / 2),
        )
        self.camera.target.y = max(
            p.get_screen_height() / 2,
            min(self.player.dest.y, self.background.height - p.get_screen_height() / 2),
        )

        # world mouse position
        world_mouse_pos: p.Vector2 = p.get_screen_to_world_2d(
            p.get_mouse_position(), self.camera
        )

        # update player
        self.player.update(self.background, world_mouse_pos)


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    game = Game()

    while not p.window_should_close():
        game.update()

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)
        p.begin_mode_2d(game.camera)

        game.draw()

        p.end_mode_2d()
        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
