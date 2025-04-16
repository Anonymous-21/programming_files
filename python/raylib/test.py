from pyray import *

init_window(800, 600, "test")
set_target_fps(60)

while not window_should_close():
    begin_drawing()
    clear_background(RAYWHITE)
    end_drawing()

close_window()

