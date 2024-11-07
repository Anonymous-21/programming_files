import pygame
import noise
import random

# Initialize Pygame
pygame.init()

# Parameters for the map
WIDTH = 800
HEIGHT = 600
TILE_SIZE = 10
MAP_WIDTH = WIDTH // TILE_SIZE
MAP_HEIGHT = HEIGHT // TILE_SIZE
NOISE_SCALE = 0.1
NOISE_OCTAVES = 6
NOISE_PERSISTENCE = 0.5
NOISE_LACUNARITY = 2.0
START_HEIGHT = HEIGHT // 2

# Colors
BACKGROUND_COLOR = (135, 206, 235)  # Sky blue
GROUND_COLOR = (139, 69, 19)       # Brown for ground
PLATFORM_COLOR = (34, 139, 34)      # Green for platforms

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Terraria-like Map Generation')

# Generate the map using Perlin noise
def generate_map():
    terrain = []
    for x in range(MAP_WIDTH):
        # Use Perlin noise to calculate the height of the terrain at this point
        noise_value = noise.pnoise2(
            x * NOISE_SCALE,
            START_HEIGHT * NOISE_SCALE,
            octaves=NOISE_OCTAVES,
            persistence=NOISE_PERSISTENCE,
            lacunarity=NOISE_LACUNARITY,
            repeatx=1024,
            repeaty=1024,
            base=42
        )
        
        # Scale the noise value to fit the map height
        height = int((noise_value + 1) / 2 * MAP_HEIGHT)  # Normalize the noise value to [0, 1]
        
        terrain.append(height)
    
    return terrain

# Draw the map
def draw_map(terrain):
    screen.fill(BACKGROUND_COLOR)
    
    for x in range(MAP_WIDTH):
        height = terrain[x]
        
        # Draw the ground (a brown rectangle at the bottom)
        for y in range(height, MAP_HEIGHT):
            pygame.draw.rect(screen, GROUND_COLOR, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        
        # Draw some platforms randomly (green rectangles in the air)
        if random.random() > 0.9:  # 10% chance to draw a platform in the air
            platform_height = random.randint(0, height)
            pygame.draw.rect(screen, PLATFORM_COLOR, (x * TILE_SIZE, platform_height * TILE_SIZE, TILE_SIZE, TILE_SIZE))

# Main loop
def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Generate and draw the map
        terrain = generate_map()
        draw_map(terrain)
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
