import pyray as p

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Drag and Drop"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    rect = p.Rectangle(20, 20, 100, 100)
    color = p.BLUE
    is_dragging = False
    offset_x = 0
    offset_y = 0

    while not p.window_should_close():
        mouse_pos = p.get_mouse_position()

        if (
            p.is_mouse_button_pressed(p.MouseButton.MOUSE_BUTTON_LEFT)
            and p.check_collision_point_rec(mouse_pos, rect)
            and not is_dragging
        ):
            is_dragging = True
            offset_x = mouse_pos.x - rect.x
            offset_y = mouse_pos.y - rect.y

        if p.is_mouse_button_down(p.MouseButton.MOUSE_BUTTON_LEFT) and is_dragging:
            rect.x = mouse_pos.x - offset_x
            rect.y = mouse_pos.y - offset_y

        if p.is_mouse_button_released(p.MouseButton.MOUSE_BUTTON_LEFT) and is_dragging:
            is_dragging = False
            offset_x = 0
            offset_y = 0

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        p.draw_rectangle_rec(rect, color)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
