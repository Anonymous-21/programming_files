import pyray as p

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "TEST"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


def gen_grid(rows, cols, block_size):
    grid = []
    for i in range(rows):
        for j in range(cols):
            x = j * block_size
            y = i * block_size

            grid.append([x, y])

    return grid


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    rows = 8
    cols = 8
    block_size = 100

    rect_width = 100
    rect_height = 100
    rect_x = 0
    rect_y = 0
    rect_color = p.BLUE
    offset_x = 0
    offset_y = 0
    is_dragging = False
    show_movement_options = False

    grid = gen_grid(rows, cols, block_size)
    grid_color = p.BLACK

    while not p.window_should_close():
        show_movement_options = False
        active_block = None
        mouse_x = p.get_mouse_x()
        mouse_y = p.get_mouse_y()

        for block in grid:
            if p.check_collision_point_rec(
                (mouse_x, mouse_y), (block[0], block[1], block_size, block_size)
            ):
                active_block = block

        if p.check_collision_point_rec(
            (mouse_x, mouse_y), (rect_x, rect_y, rect_width, rect_height)
        ):
            if (
                p.is_mouse_button_pressed(p.MouseButton.MOUSE_BUTTON_LEFT)
                and not is_dragging
            ):
                is_dragging = True
                offset_x = mouse_x - rect_x
                offset_y = mouse_y - rect_y
                current_position = (rect_x, rect_y)
            elif (
                p.is_mouse_button_down(p.MouseButton.MOUSE_BUTTON_LEFT) and is_dragging
            ):
                rect_x = mouse_x - offset_x
                rect_y = mouse_y - offset_y
                show_movement_options = True
            elif p.is_mouse_button_released(p.MouseButton.MOUSE_BUTTON_LEFT):
                is_dragging = False
                offset_x = 0
                offset_y = 0
                
                # Find the nearest grid position (round to the nearest block)
                grid_x = (rect_x // block_size) * block_size
                grid_y = (rect_y // block_size) * block_size

                # Correcting for any potential small floating point errors
                if rect_x % block_size > block_size / 2:
                    grid_x += block_size
                if rect_y % block_size > block_size / 2:
                    grid_y += block_size

                # Set the new snapped position
                rect_x = grid_x
                rect_y = grid_y

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        for block in grid:
            p.draw_rectangle_lines_ex(
                (block[0], block[1], block_size, block_size), 1, grid_color
            )
            if active_block:
                p.draw_rectangle_lines_ex(
                    (active_block[0], active_block[1], block_size, block_size), 5, p.RED
                )

        if show_movement_options:
            p.draw_rectangle_lines_ex(
                (
                    current_position[0] - block_size,
                    current_position[1],
                    block_size,
                    block_size,
                ),
                5,
                p.GRAY,
            )
            p.draw_rectangle_lines_ex(
                (
                    current_position[0] + block_size,
                    current_position[1],
                    block_size,
                    block_size,
                ),
                5,
                p.GRAY,
            )
            p.draw_rectangle_lines_ex(
                (
                    current_position[0],
                    current_position[1] - block_size,
                    block_size,
                    block_size,
                ),
                5,
                p.GRAY,
            )
            p.draw_rectangle_lines_ex(
                (
                    current_position[0],
                    current_position[1] + block_size,
                    block_size,
                    block_size,
                ),
                5,
                p.GRAY,
            )

        p.draw_rectangle_rec((rect_x, rect_y, rect_width, rect_height), rect_color)

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
