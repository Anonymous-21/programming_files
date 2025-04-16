import pyray as p
from math import radians, cos, sin

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Radar Sweep"
SCREEN_BACKGROUND = p.SKYBLUE


class Ring:
    def __init__(self):
        self.center = p.Vector2(p.get_screen_width() / 2, p.get_screen_height() / 2)
        self.inner_radius = 250
        self.outer_radius = 260
        self.start_angle = 0
        self.end_angle = 360
        self.segments = 64
        self.color = p.DARKGREEN

    def draw(self):
        p.draw_ring(
            self.center,
            self.inner_radius,
            self.outer_radius,
            self.start_angle,
            self.end_angle,
            self.segments,
            self.color,
        )


class Line:
    def __init__(self, center_x, center_y, inner_radius):
        self.center_x = center_x
        self.center_y = center_y
        self.inner_radius = inner_radius
        self.start = p.Vector2(center_x, center_y)
        self.end = p.Vector2(0, 0)
        self.thickness = 10
        self.color = p.YELLOW
        self.angle = 0
        self.speed = 50

    def draw(self):
        p.draw_line_ex(self.start, self.end, self.thickness, self.color)

    def update(self):
        self.angle += self.speed * p.get_frame_time()
        if self.angle >= 360:
            self.angle = 0

        self.end.x = self.center_x + cos(radians(self.angle)) * self.inner_radius
        self.end.y = self.center_y + sin(radians(self.angle)) * self.inner_radius


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    ring = Ring()
    line = Line(ring.center.x, ring.center.y, ring.inner_radius)

    while not p.window_should_close():
        line.update()

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        ring.draw()
        line.draw()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
