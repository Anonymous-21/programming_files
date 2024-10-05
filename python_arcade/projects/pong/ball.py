import arcade


class Ball:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.radius = 10
        self.initial_x = self.screen_width / 2
        self.initial_y = self.screen_height / 2
        self.center_x = self.initial_x
        self.center_y = self.initial_y
        self.color = arcade.color.RED

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)
