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

collision_objects_list= []

rect1_width = ground_width/10 + 80
rect1_height = ground_height/2
rect1_x = ground_x
rect1_y = ground_y + rect1_height

triangle2  = {
    1:(rect1_width, ground_y + 9),
    2:(rect1_width - 30, rect1_y),
    3:(rect1_width, rect1_y),
}

rect3_width = ground_width/10 + 10
rect3_height = ground_height - 8
rect3_x = rect1_width
rect3_y = ground_y + 8

rect4_width = rect3_x + rect3_width
rect4_height = ground_height - 8
rect4_x = rect1_width
rect4_y = ground_y + 8

while not window_should_close():
    begin_drawing()
    clear_background(RAYWHITE)

    draw_texture_rec(spritesheet,
                     ground,
                     (ground_x, ground_y),
                     WHITE)    

    draw_rectangle_lines_ex((rect1_x, rect1_y, rect1_width, rect1_height), 2, BLACK)

    draw_triangle_lines(triangle2[1],
                        triangle2[2],
                        triangle2[3],
                        BLACK)

    draw_rectangle_lines_ex((rect3_x, rect3_y, rect3_width, rect3_height), 2, BLACK)

    draw_rectangle_lines_ex((rect4_x, rect4_y, rect4_width, rect4_height), 2, BLACK)
        
    end_drawing()

close_window()
