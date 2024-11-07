import pyray as p


class Tower:
    def __init__(self) -> None:
        self.width = 40
        self.height = 40
        self.x = p.get_screen_width() / 2
        self.y = p.get_screen_height() / 2
        self.color = p.BLUE
        self.health = 10

        self.range_x = self.x + self.width / 2
        self.range_y = self.y + self.height / 2
        self.range_inner_radius = 100
        self.range_outer_radius = 103
        self.range_start_angle = 0
        self.range_end_angle = 360
        self.range_segments = 50
        self.range_color = p.GRAY

    def draw(self):
        # draw tower
        p.draw_rectangle_rec((self.x, self.y, self.width, self.height), self.color)
        # draw range
        p.draw_ring(
            (self.range_x, self.range_y),
            self.range_inner_radius,
            self.range_outer_radius,
            self.range_start_angle,
            self.range_end_angle,
            self.range_segments,
            self.range_color,
        )
