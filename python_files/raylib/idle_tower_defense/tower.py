import pyray as p


class Tower:
    def __init__(self, SCREEN_BACKGROUND) -> None:
        self.width = 30
        self.height = 30
        self.x = p.get_screen_width() // 2 - self.width // 2
        self.y = p.get_screen_height() // 2 - self.height // 2
        self.color = p.BLUE

        self.range_x = self.x + self.width // 2
        self.range_y = self.y + self.height // 2
        self.range_radius = 100
        self.range_color = SCREEN_BACKGROUND

        self.range_ring_x = self.range_x
        self.range_ring_y = self.range_y
        self.range_ring_inner_radius = self.range_radius
        self.range_ring_outer_radius = self.range_ring_inner_radius + 3
        self.range_ring_start_angle = 0
        self.range_ring_end_angle = 360
        self.range_ring_segments = 32
        self.range_ring_color = p.BLACK

    def draw(self):
        # draw range circle before tower
        p.draw_circle(self.range_x, self.range_y, self.range_radius, self.range_color)
        # range outline
        p.draw_ring(
            (self.range_ring_x, self.range_ring_y),
            self.range_ring_inner_radius,
            self.range_ring_outer_radius,
            self.range_ring_start_angle,
            self.range_ring_end_angle,
            self.range_ring_segments,
            self.range_ring_color,
        )
        # draw tower
        p.draw_rectangle(self.x, self.y, self.width, self.height, self.color)
