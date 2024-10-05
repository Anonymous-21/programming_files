from pyray import *  # noqa: F403
from spritesheet_xml_parser import xml_parser
import os

os.chdir("/home/anonymous/Downloads/programming_files/python_files/raylib/tappy_plane")

init_window(800, 600, "test")
set_target_fps(60)

spritesheet = load_texture("assets/sheet.png")
spritesheet_xml = "assets/sheet.xml"
sprite_dict = xml_parser(spritesheet_xml)

plane = sprite_dict["planeBlue1.png"]
plane_width = plane[2]
plane_height = plane[3]
plane_speed = 8

x_window = 0
y_window = 0

ground = sprite_dict["groundDirt.png"]
ground_width = ground[2]
ground_height =ground[3]

while not window_should_close():
    # move rectangle
    if is_key_down(KeyboardKey.KEY_RIGHT):
        x_window += plane_speed
    elif is_key_down(KeyboardKey.KEY_LEFT):
        x_window -= plane_speed
    elif is_key_down(KeyboardKey.KEY_UP):
        y_window -= plane_speed
    elif is_key_down(KeyboardKey.KEY_DOWN):
        y_window += plane_speed

    begin_drawing()
    clear_background(RAYWHITE)

    draw_texture_rec(spritesheet, plane, (x_window, y_window), WHITE)

    draw_texture_rec(spritesheet, ground, (0, get_screen_height() - ground_width), WHITE)

    end_drawing()

unload_texture(spritesheet)
close_window()
