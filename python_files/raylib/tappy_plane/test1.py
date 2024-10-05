from pyray import * 
import os
from spritesheet_xml_parser import xml_parser

os.chdir("/home/anonymous/Downloads/programming_files/python_files/raylib/tappy_plane")

init_window(800, 600, "test")
set_target_fps(60)

spritesheet = load_texture("assets/sheet.png")
spritesheet_xml = "assets/sheet.xml"
sprite_dict = xml_parser(spritesheet_xml)

ground = sprite_dict["groundDirt.png"]
ground_width = ground[2]
ground_height = ground[3]
ground_x = 0
ground_y = get_screen_height() - ground_height 

while not window_should_close():
    begin_drawing()
    clear_background(RAYWHITE)

    draw_texture_rec(spritesheet,
                     ground,
                     (ground_x, ground_y),
                     WHITE)    

    draw_rectangle_lines_ex((0, 600, 100, 100), 2, PURPLE)


    end_drawing()

close_window()
