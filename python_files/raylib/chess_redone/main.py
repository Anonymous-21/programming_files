import pyray as p
import os

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    SCREEN_BACKGROUND,
    GAME_FPS
)
from game_manager import Game_Manager

os.chdir("/home/anonymous/Downloads/programming_files/python_files/raylib/chess_redone")


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)
    
    pieces_spritesheet = p.load_texture("assets/tileset_128.png")

    game_manager = Game_Manager(pieces_spritesheet)

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        game_manager.draw()
        game_manager.update()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
