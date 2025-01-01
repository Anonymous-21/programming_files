import pyray as p
from os import chdir

from utils import xml_parser
from player import Player

chdir(
    "/home/anonymous/Downloads/programming_files/python_files/raylib/simple_space_survival"
)


class Game:
    def __init__(self) -> None:
        self.spritesheet = p.load_texture("assets/simpleSpace_sheet.png")
        self.spritesheet_xml = "assets/simpleSpace_sheet.xml"
        self.sprite_dict = xml_parser(self.spritesheet_xml)

        self.world_background = p.load_texture("assets/background.png")
        self.player = Player(self.spritesheet, self.sprite_dict, self.world_background)

        self.camera = p.Camera2D()
        self.camera.rotation = 0
        self.camera.zoom = 1

    def draw(self):
        # draw world_background
        p.draw_texture(self.world_background, 0, 0, p.WHITE)

        self.player.draw()

    def update(self):
        # update camera
        self.camera.target.x = max(
            p.get_screen_width() / 2,
            min(
                self.player.dest.x,
                self.world_background.width - p.get_screen_width() / 2,
            ),
        )
        self.camera.target.y = max(
            p.get_screen_height() / 2,
            min(
                self.player.dest.y,
                self.world_background.height - p.get_screen_height() / 2,
            ),
        )
        self.camera.offset = p.Vector2(
            p.get_screen_width() / 2, p.get_screen_height() / 2
        )

        # mouse position according to world space (world_background)
        mouse_x = p.get_mouse_x() - p.get_screen_width() / 2 + self.camera.target.x
        mouse_y = p.get_mouse_y() - p.get_screen_height() / 2 + self.camera.target.y

        self.player.update(mouse_x, mouse_y)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Simple Space Survival"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    game = Game()

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)
        p.begin_mode_2d(game.camera)

        game.draw()
        game.update()

        p.end_mode_2d()
        p.end_drawing()

    p.unload_texture(game.world_background)
    p.unload_texture(game.spritesheet)
    p.close_window()


if __name__ == "__main__":
    main()
