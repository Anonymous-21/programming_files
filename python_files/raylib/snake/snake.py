from pyray import *


class Snake:
    def __init__(self, rows, cols, margin_x, margin_y, block_size) -> None:
        self.rows = rows
        self.cols = cols
        self.margin_x = margin_x
        self.margin_y = margin_y
        self.block_size = block_size

        self.initial_x = self.margin_x
        self.initial_y = self.margin_y
        self.x = self.initial_x
        self.y = self.initial_y
        self.width = self.block_size
        self.height = self.block_size
        self.color = BLUE
        self.direction = "right"
        self.speed = self.block_size

        self.list = [[self.x, self.y]]

    def draw(self):
        for segment in self.list:
            draw_rectangle_rec(
                (segment[0], segment[1], self.width, self.height), self.color
            )
    
    def move(self):
        # get direction from player
        if is_key_pressed(KeyboardKey.KEY_RIGHT) and self.direction != "left":
            self.direction = "right"
        elif is_key_pressed(KeyboardKey.KEY_LEFT) and self.direction != "right":
            self.direction = "left"
        elif is_key_pressed(KeyboardKey.KEY_UP) and self.direction != "down":
            self.direction = "up"
        elif is_key_pressed(KeyboardKey.KEY_DOWN) and self.direction != "up":
            self.direction = "down"
            
        # move snake
        if self.direction == "right":
            self.x += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
            
        self.list.insert(0, [self.x, self.y])
        self.list.pop()