import pyray as p


p.init_window(600, 400, "Bouncing Ball Trail")
p.set_target_fps(60)

x = 20
y = 20
radius = 10
color = p.RED
speed_x = 5
speed_y = 6

trail = []

while not p.window_should_close():
    x += speed_x
    y += speed_y

    if x <= radius or x >= p.get_screen_width() - radius:
        speed_x *= -1
    elif y <= radius or y >= p.get_render_height() - radius:
        speed_y *= -1

    trail.append([x, y, radius, 1])

    for i in range(len(trail)):
        trail[i][3] -= 0.1
    
    if len(trail) > 10:
        trail.pop(0)

    p.begin_drawing()
    p.clear_background(p.SKYBLUE)

    for i in trail:
        trail_color = p.color_alpha(p.ORANGE, i[3])
        p.draw_circle_v((i[0], i[1]), i[2], trail_color)

    p.draw_circle_v((x, y), radius, color)

    p.end_drawing()

p.close_window()
