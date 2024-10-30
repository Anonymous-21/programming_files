import pyray as rl
import noise
import random

# Constants
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 16
MAP_WIDTH = WIDTH // TILE_SIZE
MAP_HEIGHT = HEIGHT // TILE_SIZE
AMPLITUDE = 0.3   # Controls terrain height variation
FREQUENCY = 0.1   # Controls how "stretched" the noise is horizontally
DIRT_LAYER_HEIGHT = 5  # Number of blocks below surface as dirt
STONE_START_DEPTH = 10  # Depth at which stone begins
SEED = random.randint(0, 100)  # Randomize for different maps each run

# Initialize Raylib
rl.init_window(WIDTH, HEIGHT, "Terraria-like Map Generation with Perlin Noise")
rl.set_target_fps(60)

# Generate 2D map with Perlin noise
def generate_terrain():
    terrain = []
    for x in range(MAP_WIDTH):
        # Generate surface level using Perlin noise
        noise_value = noise.pnoise1(x * FREQUENCY + SEED)
        surface_y = int((noise_value * AMPLITUDE + 0.5) * MAP_HEIGHT / 2)

        # Create air above surface
        for y in range(surface_y):
            terrain.append((x, y, "air"))

        # Create dirt layer below surface
        for y in range(surface_y, surface_y + DIRT_LAYER_HEIGHT):
            terrain.append((x, y, "dirt"))

        # Create stone layer below the dirt layer
        for y in range(surface_y + DIRT_LAYER_HEIGHT, MAP_HEIGHT):
            terrain.append((x, y, "stone"))

    return terrain

# Draw the generated map
def draw_terrain(terrain):
    for (x, y, block_type) in terrain:
        if block_type == "dirt":
            color = rl.DARKBROWN
        elif block_type == "stone":
            color = rl.GRAY
        else:
            continue  # Skip drawing air blocks
        rl.draw_rectangle(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE, color)

# Main game loop
terrain = generate_terrain()
while not rl.window_should_close():
    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)
    
    # Draw terrain blocks
    draw_terrain(terrain)
    
    rl.end_drawing()

# Close Raylib
rl.close_window()
