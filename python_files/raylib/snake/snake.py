import pyray as pr


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
        self.color = pr.BLUE
        self.direction = "right"
        self.speed = self.block_size  # move block length
        self.real_speed = 5  # real speed of snake on screen
        self.eating = False

        self.list = [[self.x, self.y]]

        self.frames_counter = 0

    def draw(self):
        for segment in self.list:
            pr.draw_rectangle_rec(
                (segment[0], segment[1], self.width, self.height), self.color
            )

    def reset_snake(self):
        self.x = self.initial_x
        self.y = self.initial_y

    def update(self):
        # get direction from player
        if pr.is_key_pressed(pr.KeyboardKey.KEY_RIGHT) and self.direction != "left":
            self.direction = "right"
        elif pr.is_key_pressed(pr.KeyboardKey.KEY_LEFT) and self.direction != "right":
            self.direction = "left"
        elif pr.is_key_pressed(pr.KeyboardKey.KEY_UP) and self.direction != "down":
            self.direction = "up"
        elif pr.is_key_pressed(pr.KeyboardKey.KEY_DOWN) and self.direction != "up":
            self.direction = "down"

        # move snake
        self.frames_counter += 1
        if self.frames_counter % self.real_speed == 0:
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

        # snake collision with walls
        if (
            self.x < self.margin_x
            or self.x > pr.get_screen_width() - self.margin_x - self.width
        ):
            return True
        elif (
            self.y < self.margin_y
            or self.y > pr.get_screen_height() - self.margin_y - self.width
        ):
            return True

        # # snake collision with itself
        # if not self.eating:
        #     snake_head = self.list[0]
        #     for segment in self.list[1:]:
        #         if pr.check_collision_recs(
        #             (snake_head[0], snake_head[1], self.width, self.height),
        #             (segment[0], segment[1], self.width, self.height),
        #         ):
        #             return True