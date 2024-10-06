import pyray as pr
import os

from spritesheet_xml_parser import xml_parser

os.chdir("/home/anonymous/Downloads/programming_files/python_files/raylib/tappy_plane")

screen_width = 800
screen_height = 480
screen_title = "test window"

pr.init_window(screen_width, screen_height, screen_title)
pr.set_target_fps(60)

spritesheet = pr.load_texture("assets/sheet.png")
spritesheet_xml = "assets/sheet.xml"
sprite_dict = xml_parser(spritesheet_xml)

ground = sprite_dict["groundDirt.png"]
ground_width = ground[2]
ground_height = ground[3]
ground_x = 0
ground_y = pr.get_screen_height() - ground_height

speed = 4

collision_rect_list = [
    (0, 445, 35, 35),
    (35, 450, 120, 30),
    (155, 417, 100, 64),
    (255, 435, 117, 45),
    (372, 422, 60, 58),
    (432, 454, 73, 26),
    (505, 465, 90, 15),
    (595, 434, 60, 46),
    (655, 411, 85, 69),
    (740, 435, 60, 45),
]
collision_triangle_list = [
    {
        1: (155, 417),
        2: (115, 452),
        3: (155, 452),
    },
    {
        1: (255, 415),
        2: (255, 435),
        3: (299, 435),
    },
    {
        1: (372, 422),
        2: (348, 436),
        3: (372, 436),
    },
    {
        1: (432, 420),
        2: (432, 454),
        3: (468, 454),
    },
    {
        1: (505, 455),
        2: (505, 465),
        3: (535, 465),
    },
    {
        1: (595, 434),
        2: (568, 464),
        3: (595, 464),
    },
    {
        1: (655, 411),
        2: (634, 433),
        3: (655, 433),
    },
    {
        1: (740, 408),
        2: (740, 435),
        3: (762, 435),
    },
]

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)

    pr.draw_texture_rec(spritesheet, ground, (ground_x, ground_y), pr.WHITE)


    for rect in collision_rect_list:
        pr.draw_rectangle_lines_ex(rect, 1, pr.BLACK)
        
    for triangle in collision_triangle_list:
        pr.draw_triangle_lines(triangle[1], triangle[2], triangle[3], pr.BLACK)

    pr.end_drawing()

pr.close_window()
