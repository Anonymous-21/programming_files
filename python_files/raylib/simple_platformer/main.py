import pyray as p
import os

from xml_parser import xml_parser
from levels import Levels
from player import Player

os.chdir("/home/anonymous/Downloads/programming_files/python_files/raylib/simple_platformer")


SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 960
SCREEN_TITLE = "Simple Platformer"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self) -> None:
        self.spritesheet = p.load_texture("assets/pixel_line.png")
        self.spritesheet_xml = "assets/pixel_line.xml"
        self.sprite_dict = xml_parser(self.spritesheet_xml)
        
        self.levels = Levels(self.spritesheet, self.sprite_dict)
        self.player = Player(self.spritesheet, self.sprite_dict)
        
    def draw(self):
        self.levels.draw()
        self.player.draw()
        
    def update(self):
        pass
    
    
def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)
    
    game = Game()
    
    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)
        
        game.draw()
        game.update()
        
        p.end_drawing()
        
    p.close_window()
    

if __name__ == "__main__":
    main()
    