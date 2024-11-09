import pyray as p
import random


class Enemy:
    def __init__(self) -> None:
        self.small_width = 20
        self.small_height = 20
        self.small_color = p.GRAY
        self.small_speed = 1

        self.medium_width = 30
        self.medium_height = 30
        self.medium_color = p.ORANGE
        self.medium_speed = 0.5

        self.list = []

        self.frames_counter = 0
        self.enemy_count = 0

        self.update()

    def draw(self):
        for enemy in self.list:
            p.draw_rectangle_rec((enemy[0], enemy[1], enemy[2], enemy[3]), enemy[4])

    def update(self):
        self.frames_counter += 1

        # Add enemies at different positions based on frame count
        if self.frames_counter % 60 == 0:
            # Spawn an enemy at a random location from any edge
            edge_choice = random.randint(0, 3)
            if edge_choice == 0:  # Left edge
                x = 0
                y = random.randint(0, p.get_screen_height() - 1)
            elif edge_choice == 1:  # Top edge
                x = random.randint(0, p.get_screen_width() - 1)
                y = 0
            elif edge_choice == 2:  # Right edge
                x = p.get_screen_width()
                y = random.randint(0, p.get_screen_height() - 1)
            elif edge_choice == 3:  # Bottom edge
                x = random.randint(0, p.get_screen_width() - 1)
                y = p.get_screen_height()

            self.enemy_count += 1
            if self.enemy_count % 10 == 0:
                self.list.append(
                    [
                        x,
                        y,
                        self.medium_width,
                        self.medium_height,
                        self.medium_color,
                        self.medium_speed,
                    ]
                )
            else:
                self.list.append(
                    [
                        x,
                        y,
                        self.small_width,
                        self.small_height,
                        self.small_color,
                        self.small_speed,
                    ]
                )

        # Reset counter to avoid overflow, but this can be adjusted if needed
        if self.frames_counter >= 240:
            self.frames_counter = 0
