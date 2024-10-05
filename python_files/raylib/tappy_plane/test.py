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

triangle = {
    1: [300, 300],
    2: [150, 450],
    3: [450, 450],
}
triangle_color = GREEN
triangle_speed = 5

while not window_should_close():
    begin_drawing()
    clear_background(RAYWHITE)

    draw_triangle(triangle[1], triangle[2], triangle[3], triangle_color)

    draw_texture_rec(spritesheet, plane, (x_window, y_window), WHITE)

    # move triangle
    triangle[2][0] -= triangle_speed
    triangle[1][0] = triangle[2][0] + 150
    triangle[3][0] = triangle[2][0] + 300

    if triangle[2][0] < -300:
        triangle[2][0] = get_screen_width() + 300

    # move rectangle
    if is_key_down(KeyboardKey.KEY_RIGHT):
        x_window += plane_speed
    elif is_key_down(KeyboardKey.KEY_LEFT):
        x_window -= plane_speed
    elif is_key_down(KeyboardKey.KEY_UP):
        y_window -= plane_speed
    elif is_key_down(KeyboardKey.KEY_DOWN):
        y_window += plane_speed

    if check_collision_point_triangle(
        (x_window, y_window), triangle[1], triangle[2], triangle[3]
    ):
        draw_text("collision detected", 600, 100, 30, GRAY)
    elif check_collision_point_triangle(
        (x_window + plane_width, y_window), triangle[1], triangle[2], triangle[3]
    ):
        draw_text("collision detected", 600, 100, 30, GRAY)
    elif check_collision_point_triangle(
        (x_window, y_window + plane_height), triangle[1], triangle[2], triangle[3]
    ):
        draw_text("collision detected", 600, 100, 30, GRAY)
    elif check_collision_point_triangle(
        (x_window + plane_width, y_window + plane_height),
        triangle[1],
        triangle[2],
        triangle[3],
    ):
        draw_text("collision detected", 600, 100, 30, GRAY)

    end_drawing()

unload_texture(spritesheet)
close_window()
