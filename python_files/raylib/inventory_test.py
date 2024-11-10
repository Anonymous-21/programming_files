import pyray as p

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Inventory"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60

p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
p.set_target_fps(GAME_FPS)

sword_arcane = p.load_texture(
    "/home/anonymous/Downloads/programming_files/assets/Elemental Weapons Effect/Arcane/01.png"
)
sword_blood = p.load_texture(
    "/home/anonymous/Downloads/programming_files/assets/Elemental Weapons Effect/Blood/13.png"
)
sword_fire = p.load_texture(
    "/home/anonymous/Downloads/programming_files/assets/Elemental Weapons Effect/Fire/25.png"
)
sword_ice = p.load_texture(
    "/home/anonymous/Downloads/programming_files/assets/Elemental Weapons Effect/Ice/13.png"
)
sword_light = p.load_texture(
    "/home/anonymous/Downloads/programming_files/assets/Elemental Weapons Effect/Light/25.png"
)
sword_nature = p.load_texture(
    "/home/anonymous/Downloads/programming_files/assets/Elemental Weapons Effect/Nature/01.png"
)
inv = [sword_arcane, sword_blood, sword_fire, sword_ice, sword_light, sword_nature]
inv_x = 100
inv_y = 100
inv_width = 600
inv_height = 400
inv_color = p.BROWN
show_inventory = False

inv_section_gap_x = 20
inv_section_gap_y = 20
inv_section_rows = 3
inv_section_cols = 4
inv_section_width = (inv_width - (inv_section_gap_x * 5)) / 4
inv_section_height = (inv_height - (inv_section_gap_y * 4)) / 3
inv_sections = [
    # Row 1
    [inv_x + inv_section_gap_x, inv_y + inv_section_gap_y],
    [inv_x + (inv_section_gap_x * 2) + inv_section_width, inv_y + inv_section_gap_y],
    [
        inv_x + (inv_section_gap_x * 3) + (inv_section_width * 2),
        inv_y + inv_section_gap_y,
    ],
    [
        inv_x + (inv_section_gap_x * 4) + (inv_section_width * 3),
        inv_y + inv_section_gap_y,
    ],
    # Row 2
    [inv_x + inv_section_gap_x, inv_y + (inv_section_gap_y * 2) + inv_section_height],
    [
        inv_x + (inv_section_gap_x * 2) + (inv_section_width),
        (inv_section_height * 2) + (inv_section_gap_y * 2),
    ],
]
inv_section_color = p.WHITE


while not p.window_should_close():
    if p.is_key_pressed(p.KeyboardKey.KEY_I) and not show_inventory:
        show_inventory = True
    elif (
        p.is_key_pressed(p.KeyboardKey.KEY_I)
        or p.is_key_pressed(p.KeyboardKey.KEY_ESCAPE)
    ) and show_inventory:
        show_inventory = False

    p.begin_drawing()
    p.clear_background(SCREEN_BACKGROUND)

    if show_inventory:
        p.draw_rectangle_rec((inv_x, inv_y, inv_width, inv_height), inv_color)
        for section in inv_sections:
            p.draw_rectangle_rec(
                (section[0], section[1], inv_section_width, inv_section_height),
                inv_section_color,
            )

    p.end_drawing()

p.unload_texture(sword_arcane)
p.unload_texture(sword_blood)
p.unload_texture(sword_fire)
p.unload_texture(sword_ice)
p.unload_texture(sword_light)
p.unload_texture(sword_nature)
p.close_window()
