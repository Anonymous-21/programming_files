import arcade


class Paddle:
    def __init__(self,screen_width, screen_height, center_x):
        self.screen_width = screen_width
        self.screen_height =screen_height
        self.width = 10
        self.height = 100
        self.center_x = center_x + self.width / 2
        self.center_y = self.screen_height / 2
        self.color = arcade.color.BLACK
        self.change_y = 0
        self.speed = 8

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

    def update(self):
        self.center_y += self.change_y

        if self.center_y <= self.height / 2:
            self.center_y = self.height / 2
        elif self.center_y >= self.screen_height - self.height / 2:
            self.center_y = self.screen_height - self.height / 2

