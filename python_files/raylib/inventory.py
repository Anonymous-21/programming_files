import pyray as p

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Inventory"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60

ROWS = 5
COLS = 5
BLOCK_SIZE = 80
SPACE_BETWEEN_BLOCKS = 10
MARGIN_X = 185
MARGIN_Y = 85


def genGrid(ROWS, COLS, BLOCK_SIZE, SPACE_BETWEEN_BLOCKS, MARGIN_X, MARGIN_Y):
    grid = []
    for i in range(ROWS):
        for j in range(COLS):
            x = j * (BLOCK_SIZE + SPACE_BETWEEN_BLOCKS) + MARGIN_X
            y = i * (BLOCK_SIZE + SPACE_BETWEEN_BLOCKS) + MARGIN_Y

            grid.append([x, y])

    return grid


class Item:
    def __init__(self, texture, name, x, y, width, height) -> None:
        self.texture = texture
        self.name = name
        self.rect = p.Rectangle(x, y, width, height)
        self.offset_x = 0
        self.offset_y = 0
        self.is_dragging = False


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    wooden_sword_texture = p.load_texture(
        "/home/anonymous/Downloads/programming_files/assets/Pixel Art Icon Pack - RPG/Weapon & Tool/Wooden Sword.png"
    )
    wooden_armor_texture = p.load_texture(
        "/home/anonymous/Downloads/programming_files/assets/Pixel Art Icon Pack - RPG/Equipment/Wooden Armor.png"
    )
    red_potion_texture = p.load_texture(
        "/home/anonymous/Downloads/programming_files/assets/Pixel Art Icon Pack - RPG/Potion/Red Potion.png"
    )

    grid = genGrid(ROWS, COLS, BLOCK_SIZE, SPACE_BETWEEN_BLOCKS, MARGIN_X, MARGIN_Y)
    grid_color = p.GRAY
    grid_highlight_thickness = 8
    grid_hightlight_color = p.RED

    inner_padding_block = 10
    item_width = BLOCK_SIZE - (inner_padding_block * 2)
    item_height = BLOCK_SIZE - (inner_padding_block * 2)
    wooden_sword = Item(
        wooden_sword_texture,
        "Wooden Sword",
        grid[0][0] + inner_padding_block,
        grid[0][1] + inner_padding_block,
        item_width,
        item_height,
    )
    wooden_armor = Item(
        wooden_armor_texture,
        "Wooden Armor",
        grid[1][0] + inner_padding_block,
        grid[1][1] + inner_padding_block,
        item_width,
        item_height,
    )
    red_potion = Item(
        red_potion_texture,
        "Red Potion",
        grid[2][0] + inner_padding_block,
        grid[2][1] + inner_padding_block,
        item_width,
        item_height,
    )
    inv = [wooden_sword, wooden_armor, red_potion]

    while not p.window_should_close():
        active_block = None

        mouse_x = p.get_mouse_x()
        mouse_y = p.get_mouse_y()

        for block in grid:
            if p.check_collision_point_rec(
                (mouse_x, mouse_y), (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE)
            ):
                active_block = block

        for item in inv:
            if p.check_collision_point_rec((mouse_x, mouse_y), item.rect):
                active_item = item
        
        # drag and drop items with mouse
        if (
            p.is_mouse_button_pressed(p.MouseButton.MOUSE_BUTTON_LEFT)
            and not active_item.is_dragging
        ):
            active_item.is_dragging = True
            active_item.offset_x = mouse_x - active_item.rect.x
            active_item.offset_y = mouse_y - active_item.rect.y
        elif (
            p.is_mouse_button_down(p.MouseButton.MOUSE_BUTTON_LEFT)
            and active_item.is_dragging
        ):
            active_item.rect.x = mouse_x - active_item.offset_x
            active_item.rect.y = mouse_y - active_item.offset_y
        elif p.is_mouse_button_released(p.MouseButton.MOUSE_BUTTON_LEFT):
            active_item.is_dragging = False
            active_item.offset_x = 0
            active_item.offset_y = 0
            if active_block:
                active_item.rect.x = active_block[0] + inner_padding_block
                active_item.rect.y = active_block[1] + inner_padding_block

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        for block in grid:
            p.draw_rectangle_rec(
                (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE), grid_color
            )
            if active_block:
                p.draw_rectangle_lines_ex(
                    (active_block[0], active_block[1], BLOCK_SIZE, BLOCK_SIZE),
                    grid_highlight_thickness,
                    grid_hightlight_color,
                )

        for item in inv:
            p.draw_texture_pro(
                item.texture,
                (0, 0, item.texture.width, item.texture.height),
                (item.rect.x, item.rect.y, item.rect.width, item.rect.height),
                (0, 0),
                0,
                p.WHITE,
            )

        p.end_drawing()

    p.unload_texture(wooden_sword)
    p.unload_texture(wooden_armor)
    p.unload_texture(red_potion)
    p.close_window()


if __name__ == "__main__":
    main()
