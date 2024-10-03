import raylib as r
import os

from encode import encode
from spritesheet_xml_parser import xml_parser
from player import Player

os.chdir(
    "/home/anonymous/Downloads/programming_files/python_files/raylib/pixel_line_platformer"
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PIXEL LINE PLAFORMER"
SCREEN_BACKGROUND = r.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self) -> None:
        self.spritesheet = r.LoadTexture(encode("assets/spritesheet.png"))
        self.spritesheet_xml = "assets/spritesheet.xml"
        self.sprite_dict = xml_parser(self.spritesheet_xml)

        self.player = Player(self.spritesheet, self.sprite_dict)

    def draw(self):
        self.player.draw()

    def update(self):
        self.player.update()
        self.player.movement()


def main():
    r.InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, encode(SCREEN_TITLE))
    r.SetTargetFPS(GAME_FPS)

    game = Game()

    while not r.WindowShouldClose():
        r.BeginDrawing()
        r.ClearBackground(SCREEN_BACKGROUND)

        game.draw()
        game.update()

        r.EndDrawing()

    r.UnloadTexture(game.spritesheet)
    r.CloseWindow()


if __name__ == "__main__":
    main()
