import pyray as p

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    SCREEN_BACKGROUND,
    GAME_FPS,
)
from game_manager import Game_Manager


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    pieces_spritesheet = p.load_texture(
        "/home/anonymous/Downloads/programming_files/python_files/raylib/chess/assets/tileset_128.png"
    )
    
    game_manager = Game_Manager(pieces_spritesheet)

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        game_manager.draw()
        game_manager.update()

        p.end_drawing()

    p.unload_texture(pieces_spritesheet)
    p.close_window()


if __name__ == "__main__":
    main()
