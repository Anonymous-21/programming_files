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

rect1_x = 0
rect1_y = 445
rect1_width = 35
rect1_height = 35
rect1_color = pr.BLACK

rect2_x = rect1_x + rect1_width
rect2_y = rect1_y + 5
rect2_width = 120
rect2_height = 30
rect2_color = pr.BLACK

rect3_x = rect2_x + rect2_width
rect3_y = rect1_y - 28
rect3_width = 100
rect3_height = 64
rect3_color = pr.BLACK

triangle1 = {
    1: (rect3_x, rect3_y),
    2: (rect3_x - 40, rect3_y + 35),
    3: (rect3_x, rect3_y + 35),
}
triangle1_color = pr.BLACK

rect4_x = rect3_x + rect3_width
rect4_y = rect1_y - 10
rect4_width = 117
rect4_height = 45
rect4_color = pr.BLACK

triangle2 = {
    1: (rect4_x, rect4_y - 20),
    2: (rect4_x, rect4_y),
    3: (rect4_x + 44, rect4_y),
}
triangle2_color = pr.BLACK

rect5_x = rect4_x + rect4_width
rect5_y = rect1_y - 23
rect5_width = 60
rect5_height = 58
rect5_color = pr.BLACK

triangle3 = {
    1: (rect5_x, rect5_y),
    2: (rect5_x - 24, rect5_y + 14),
    3: (rect5_x, rect5_y + 14),
}
triangle3_color = pr.BLACK

rect6_x = rect5_x + rect5_width
rect6_y = rect1_y + 9
rect6_width = 73
rect6_height = 26
rect6_color = pr.BLACK

triangle4 = {
    1: (rect6_x, rect6_y - 34),
    2: (rect6_x, rect6_y),
    3: (rect6_x + 36, rect6_y),
}
triangle4_color = pr.BLACK

rect7_x = rect6_x + rect6_width
rect7_y = rect1_y + 20
rect7_width = 90
rect7_height = 15
rect7_color = pr.BLACK

triangle5 = {
    1: (rect7_x, rect7_y - 10),
    2: (rect7_x, rect7_y),
    3: (rect7_x + 30, rect7_y),
}
triangle5_color = pr.BLACK

rect8_x = rect7_x + rect7_width
rect8_y = rect1_y - 11
rect8_width = 60
rect8_height = 46
rect8_color = pr.BLACK

triangle6 = {
    1: (rect8_x, rect8_y),
    2: (rect8_x - 27, rect8_y + 30),
    3: (rect8_x, rect8_y + 30),
}
triangle6_color = pr.BLACK

rect9_x = rect8_x + rect8_width
rect9_y = rect1_y - 34
rect9_width = 85
rect9_height = 69
rect9_color = pr.BLACK

triangle7 = {
    1: (rect9_x, rect9_y),
    2: (rect9_x - 21, rect9_y + 22),
    3: (rect9_x, rect9_y + 22),
}
triangle7_color = pr.BLACK

rect10_x = rect9_x + rect9_width
rect10_y = rect1_y - 10
rect10_width = 60
rect10_height = 45
rect10_color = pr.BLACK

triangle8 = {
    1: (rect10_x, rect10_y - 27),
    2: (rect10_x, rect10_y),
    3: (rect10_x + 22, rect10_y),
}
triangle8_color = pr.BLACK

speed = 4

collision_rect_list = [
    (0, 445, 35, 35),
    (rect1_x + rect1_width, rect1_y + 5, 120, 30),
    (rect2_x + rect2_width, rect1_y - 28, 100, 64),
    (rect3_x + rect3_width, rect1_y - 10, 117, 45),
    (rect4_x + rect4_width, rect1_y - 23, 60, 58),
    (rect5_x + rect5_width, rect1_y + 9, 73, 26),
    (rect6_x + rect6_width, rect1_y + 20, 90, 15),
    (rect7_x + rect7_width, rect1_y - 11, 60, 46),
    (rect8_x + rect8_width, rect1_y - 34, 85, 69),
    (rect9_x + rect9_width, rect1_y - 10, 60, 45),
]

collision_triangle_list = [
    {
        1: (rect3_x, rect3_y),
        2: (rect3_x - 40, rect3_y + 35),
        3: (rect3_x, rect3_y + 35),
    },
    {
        1: (rect4_x, rect4_y - 20),
        2: (rect4_x, rect4_y),
        3: (rect4_x + 44, rect4_y),
    },
    {
        1: (rect5_x, rect5_y),
        2: (rect5_x - 24, rect5_y + 14),
        3: (rect5_x, rect5_y + 14),
    },
    {
        1: (rect6_x, rect6_y - 34),
        2: (rect6_x, rect6_y),
        3: (rect6_x + 36, rect6_y),
    },
    {
        1: (rect7_x, rect7_y - 10),
        2: (rect7_x, rect7_y),
        3: (rect7_x + 30, rect7_y),
    },
    {
        1: (rect8_x, rect8_y),
        2: (rect8_x - 27, rect8_y + 30),
        3: (rect8_x, rect8_y + 30),
    },
    {
        1: (rect9_x, rect9_y),
        2: (rect9_x - 21, rect9_y + 22),
        3: (rect9_x, rect9_y + 22),
    },
    {
        1: (rect10_x, rect10_y - 27),
        2: (rect10_x, rect10_y),
        3: (rect10_x + 22, rect10_y),
    },
]

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)

    # pr.draw_line_strip(line_strip, len(line_strip), pr.RED)
    pr.draw_texture_rec(spritesheet, ground, (ground_x, ground_y), pr.WHITE)

    pr.draw_triangle_lines(triangle1[1], triangle1[2], triangle1[3], triangle1_color)
    pr.draw_triangle_lines(triangle2[1], triangle2[2], triangle2[3], triangle2_color)
    pr.draw_triangle_lines(triangle3[1], triangle3[2], triangle3[3], triangle3_color)
    pr.draw_triangle_lines(triangle4[1], triangle4[2], triangle4[3], triangle4_color)
    pr.draw_triangle_lines(triangle5[1], triangle5[2], triangle5[3], triangle5_color)
    pr.draw_triangle_lines(triangle6[1], triangle6[2], triangle6[3], triangle6_color)
    pr.draw_triangle_lines(triangle7[1], triangle7[2], triangle7[3], triangle7_color)
    pr.draw_triangle_lines(triangle8[1], triangle8[2], triangle8[3], triangle8_color)

    pr.draw_rectangle_lines_ex(
        (rect1_x, rect1_y, rect1_width, rect1_height), 1, rect1_color
    )
    pr.draw_rectangle_lines_ex(
        (rect2_x, rect2_y, rect2_width, rect2_height), 1, rect2_color
    )
    pr.draw_rectangle_lines_ex(
        (rect3_x, rect3_y, rect3_width, rect3_height), 1, rect3_color
    )
    pr.draw_rectangle_lines_ex(
        (rect4_x, rect4_y, rect4_width, rect4_height), 1, rect4_color
    )
    pr.draw_rectangle_lines_ex(
        (rect5_x, rect5_y, rect5_width, rect5_height), 1, rect5_color
    )
    pr.draw_rectangle_lines_ex(
        (rect6_x, rect6_y, rect6_width, rect6_height), 1, rect6_color
    )
    pr.draw_rectangle_lines_ex(
        (rect7_x, rect7_y, rect7_width, rect7_height), 1, rect7_color
    )
    pr.draw_rectangle_lines_ex(
        (rect8_x, rect8_y, rect8_width, rect8_height), 1, rect8_color
    )
    pr.draw_rectangle_lines_ex(
        (rect9_x, rect9_y, rect9_width, rect9_height), 1, rect9_color
    )
    pr.draw_rectangle_lines_ex(
        (rect10_x, rect10_y, rect10_width, rect10_height), 1, rect10_color
    )

    pr.end_drawing()

pr.close_window()
