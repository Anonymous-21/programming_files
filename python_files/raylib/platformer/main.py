import raylib as r
import os

from encode import encode
from spritesheet_xml_parser import xml_parser
from player import Player

os.chdir("/home/anonymous/Downloads/programming_files/python_files/raylib/platformer")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PLATFORMER"
SCREEN_BACKGROUND = r.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self) -> None:
        self.spritesheet = r.LoadTexture(encode("assets/spritesheet_complete.png"))
        self.spritesheet_xml = "assets/spritesheet_complete.xml"
        self.sprite_dict = xml_parser(self.spritesheet_xml)

        self.player = Player()

    def draw(self):
        self.player.draw()


def main():
    r.InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, encode(SCREEN_TITLE))
    r.SetTargetFPS(GAME_FPS)

    game = Game()

    while not r.WindowShouldClose():
        r.BeginDrawing()
        r.ClearBackground(SCREEN_BACKGROUND)

        game.draw()

        r.EndDrawing()

    r.CloseWindow()


if __name__ == "__main__":
    main()
