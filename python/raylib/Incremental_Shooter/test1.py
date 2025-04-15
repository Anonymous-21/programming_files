import pyray as rl
import math

# Initialization
screen_width = 800
screen_height = 600
rl.init_window(screen_width, screen_height, b"Rotate Towards Mouse")
rl.set_target_fps(60)

# Rectangle properties
rect_size = rl.Vector2(100, 40)
rect_origin = rl.Vector2(rect_size.x / 2, rect_size.y / 2)
rect_position = rl.Vector2(screen_width / 2, screen_height / 2)

while not rl.window_should_close():
    # Get mouse position
    mouse_pos = rl.get_mouse_position()

    # Calculate direction vector from rectangle to mouse
    dir_x = mouse_pos.x - rect_position.x
    dir_y = mouse_pos.y - rect_position.y

    # Calculate angle in degrees using atan2
    angle_rad = math.atan2(dir_y, dir_x)
    angle_deg = math.degrees(angle_rad)

    # Drawing
    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)

    # Draw the rotating rectangle
    rect = rl.Rectangle(
        rect_position.x - rect_origin.x,
        rect_position.y - rect_origin.y,
        rect_size.x,
        rect_size.y,
    )
    rl.draw_rectangle_pro(rect, rect_origin, angle_deg, rl.BLUE)

    # Debug visuals
    rl.draw_circle_v(mouse_pos, 5, rl.RED)
    rl.draw_line_v(rect_position, mouse_pos, rl.DARKGRAY)

    rl.end_drawing()

rl.close_window()
