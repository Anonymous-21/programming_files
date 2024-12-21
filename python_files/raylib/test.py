import pyray as p


p.init_window(500, 500, "test")
p.set_target_fps(60)

while not p.window_should_close():
    p.begin_drawing()
    p.clear_background(p.RAYWHITE)

    for i in range(5):
        for j in range(5):
            x = j * 100
            y = i * 100

            p.draw_rectangle_lines_ex((x, y, 100, 100), 2, p.BLACK)

    p.end_drawing()

p.close_window()
