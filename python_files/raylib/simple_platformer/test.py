import pyray as rl

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 40  # Size of a tile (40x40 pixels)

# Define map data (1 = wall, 0 = empty space)
# game_map = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
#     [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
#     [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# ]

game_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


# Define player
player = rl.Rectangle(80, 80, TILE_SIZE / 2, TILE_SIZE / 2)  # Player rectangle

# Define movement speed
player_speed = 200  # pixels per second

# Initialize the window
rl.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tile Map with Collision")
rl.set_target_fps(60)

def is_colliding_with_wall(rect):
    """Check if a rectangle is colliding with any wall in the map."""
    for row in range(len(game_map)):
        for col in range(len(game_map[row])):
            if game_map[row][col] == 1:  # Wall
                wall_rect = rl.Rectangle(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if rl.check_collision_recs(rect, wall_rect):
                    return True
    return False

# Game loop
while not rl.window_should_close():
    # Time-based movement (for consistent movement regardless of frame rate)
    dt = rl.get_frame_time()

    # Handle player movement
    movement_x = 0
    movement_y = 0
    if rl.is_key_down(rl.KEY_RIGHT):
        movement_x += player_speed * dt
    if rl.is_key_down(rl.KEY_LEFT):
        movement_x -= player_speed * dt
    if rl.is_key_down(rl.KEY_UP):
        movement_y -= player_speed * dt
    if rl.is_key_down(rl.KEY_DOWN):
        movement_y += player_speed * dt

    # Calculate the player's new position
    new_player_pos = rl.Rectangle(player.x + movement_x, player.y + movement_y, player.width, player.height)

    # Check collision with walls
    if not is_colliding_with_wall(new_player_pos):
        player.x += movement_x
        player.y += movement_y

    # Drawing
    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)

    # Draw the map
    for row in range(len(game_map)):
        for col in range(len(game_map[row])):
            tile_color = rl.GRAY if game_map[row][col] == 1 else rl.LIGHTGRAY
            rl.draw_rectangle(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE, tile_color)

    # Draw the player
    rl.draw_rectangle_rec(player, rl.RED)

    rl.end_drawing()

# Close the window
rl.close_window()
