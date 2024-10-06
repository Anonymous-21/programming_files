from pyray import * 

screen_width = 800
screen_height = 480
screen_title = "test window"

init_window(screen_width, screen_height, screen_title)
set_target_fps(60)

line_strip = [
    (0, 445),
    (29, 443),
    (37, 451),
    (88, 455),
    (129, 443),
    (153, 417),
    (245, 413),
    (303, 437),
    (346, 436),
    (370, 422),
    (432, 421),
    (466, 453),
    (505, 454),
    (530, 464),
    (569, 464),
    (594, 437),
    (632, 434),
    (654, 413),
    (740, 410),
    (759, 436),
    (800, 445),
]

rect1_x = line_strip[0][0]
rect1_y = line_strip[0][1]
rect1_width = 35
rect1_height = 35
rect1_color = BLACK

rect2_x = rect1_x + rect1_width
rect2_y = rect1_y + 5
rect2_width = 120
rect2_height = 30
rect2_color = BLACK

rect3_x = rect2_x + rect2_width
rect3_y = rect1_y - 30
rect3_width = 100
rect3_height = 64
rect3_color = BLACK

rect4_x = rect3_x + rect3_width
rect4_y = rect1_y - 10
rect4_width = 117
rect4_height = 45
rect4_color = BLACK

rect5_x = rect4_x + rect4_width
rect5_y = rect1_y - 23
rect5_width = 60
rect5_height = 58
rect5_color = BLACK

rect6_x = rect5_x + rect5_width
rect6_y = rect1_y + 9
rect6_width = 73
rect6_height = 26
rect6_color = BLACK

rect7_x = rect6_x + rect6_width
rect7_y = rect1_y + 20
rect7_width = 90
rect7_height = 15
rect7_color = BLACK

rect8_x = rect7_x + rect7_width
rect8_y = rect1_y - 11
rect8_width = 60
rect8_height = 46
rect8_color = BLACK

rect9_x = rect8_x + rect8_width
rect9_y = rect1_y - 34
rect9_width = 85
rect9_height = 69
rect9_color = BLACK

rect10_x = rect9_x + rect9_width
rect10_y = rect1_y - 10
rect10_width = 60
rect10_height = 45
rect10_color = BLACK

speed = 4

while not window_should_close():
        
    begin_drawing()
    clear_background(RAYWHITE)

    draw_line_strip(line_strip, len(line_strip), BLACK)

    draw_rectangle_lines_ex((rect1_x, rect1_y, rect1_width, rect1_height), 1, rect1_color)
    draw_rectangle_lines_ex((rect2_x, rect2_y, rect2_width, rect2_height), 1, rect2_color)
    draw_rectangle_lines_ex((rect3_x, rect3_y, rect3_width, rect3_height), 1, rect3_color)
    draw_rectangle_lines_ex((rect4_x, rect4_y, rect4_width, rect4_height), 1, rect4_color)
    draw_rectangle_lines_ex((rect5_x, rect5_y, rect5_width, rect5_height), 1, rect5_color)
    draw_rectangle_lines_ex((rect6_x, rect6_y, rect6_width, rect6_height), 1, rect6_color)
    draw_rectangle_lines_ex((rect7_x, rect7_y, rect7_width, rect7_height), 1, rect7_color)
    draw_rectangle_lines_ex((rect8_x, rect8_y, rect8_width, rect8_height), 1, rect8_color)
    draw_rectangle_lines_ex((rect9_x, rect9_y, rect9_width, rect9_height), 1, rect9_color)
    draw_rectangle_lines_ex((rect10_x, rect10_y, rect10_width, rect10_height), 1, rect10_color)

    end_drawing()

close_window()
