import pyray as rl
import math

# Initialize window
rl.init_window(640, 360, b"Array Cosine Wave")
rl.set_target_fps(60)

# Create coswave array
coswave = [0.0] * 640
for i in range(640):
    amount = rl.remap(i, 0, 640, 0, math.pi)
    coswave[i] = abs(math.cos(amount))

# Main game loop
while not rl.window_should_close():
    # Begin drawing
    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)

    # Draw first third (black to white)
    y1 = 0
    y2 = rl.get_screen_height() // 3
    for i in range(640):
        color = rl.Color(
            int(coswave[i] * 255), int(coswave[i] * 255), int(coswave[i] * 255), 255
        )
        rl.draw_line(i, y1, i, y2, color)

    # Draw second third (dark gray)
    y1 = y2
    y2 = y1 * 2
    for i in range(640):
        color = rl.Color(
            int(coswave[i] * 255 / 4),
            int(coswave[i] * 255 / 4),
            int(coswave[i] * 255 / 4),
            255,
        )
        rl.draw_line(i, y1, i, y2, color)

    # Draw last third (white to black)
    y1 = y2
    y2 = rl.get_screen_height()
    for i in range(640):
        color = rl.Color(
            255 - int(coswave[i] * 255),
            255 - int(coswave[i] * 255),
            255 - int(coswave[i] * 255),
            255,
        )
        rl.draw_line(i, y1, i, y2, color)

    rl.end_drawing()

# Close window
rl.close_window()
