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
        self.change_x = 5
        self.change_y = 6

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.center_x <= self.radius or self.center_x >= self.screen_width - self.radius:
            self.change_x *= -1
        elif self.center_y <= self.radius or self.center_y >= self.screen_height - self.radius:
            self.change_y *= -1
        
