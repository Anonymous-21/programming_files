from pyray import *

from spritesheet_xml_parser import xml_parser


init_window(800, 600, "test window")
set_target_fps(60)

spritesheet = load_texture("assets/sheet.png")
spritesheet_xml = "assets/sheet.xml"
sprite_dict = xml_parser(spritesheet_xml)

ground = sprite_dict["groundDirt.png"]
ground_width = ground[2]
ground_height = ground[3]

line_vectors = [
    (0, 445 + 120),
    (29, 443 + 120),
    (37, 451 + 120),
    (88, 455 + 120),
    (129, 443 + 120),
    (153, 417 + 120),
    (245, 413 + 120),
    (303, 437 + 120),
    (346, 436 + 120),
    (370, 422 + 120),
    (432, 421 + 120),
    (466, 453 + 120),
    (505, 454 + 120),
    (530, 464 + 120),
    (569, 464 + 120),
    (594, 437 + 120),
    (632, 434 + 120),
    (654, 413 + 120),
    (740, 410 + 120),
    (759, 436 + 120),
    (800, 445 + 120),
] 

while not window_should_close():
    begin_drawing()
    clear_background(RAYWHITE)

    draw_texture_rec(spritesheet,
                     ground,
                     (0, get_screen_height() - ground_height),
                     WHITE)

    draw_line_strip(line_vectors,
                    len(line_vectors),
                    BLACK)

    end_drawing()

close_window()

