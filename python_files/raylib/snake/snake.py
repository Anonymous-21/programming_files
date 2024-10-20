import pyray as p


class Snake:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.x = self.grid.margin
        self.y = self.grid.margin
        self.width = self.grid.block_size
        self.height = self.grid.block_size
        self.color = p.BLUE
        self.speed = self.grid.block_size
        self.frames_counter = 0
        self.direction = "right"
        self.list = [[self.x, self.y]]

    def draw(self):
        for segment in self.list:
            p.draw_rectangle_rec(
                (segment[0], segment[1], self.width, self.height), self.color
            )

    def get_direction(self):
        if p.is_key_pressed(p.KeyboardKey.KEY_RIGHT) and self.direction != "left":
            self.direction = "right"
        elif p.is_key_pressed(p.KeyboardKey.KEY_LEFT) and self.direction != "right":
            self.direction = "left"
        elif p.is_key_pressed(p.KeyboardKey.KEY_UP) and self.direction != "down":
            self.direction = "up"
        elif p.is_key_pressed(p.KeyboardKey.KEY_DOWN) and self.direction != "up":
            self.direction = "down"

    def move(self, food, score):
        self.frames_counter += 1
        if self.frames_counter % 5 == 0:
            if self.frames_counter > 1000:
                self.frames_counter = 0

            if self.direction == "right":
                self.x += self.speed
            elif self.direction == "left":
                self.x -= self.speed
            elif self.direction == "up":
                self.y -= self.speed
            elif self.direction == "down":
                self.y += self.speed

            # food collision snake head
            if p.check_collision_recs(
                (self.list[0][0], self.list[0][1], self.width, self.height),
                (food.x, food.y, food.width, food.height),
            ):
                score += 1
                self.list.append(self.list[-1])
                food.x, food.y = food.gen_random_food()

            self.list.insert(0, [self.x, self.y])
            self.list.pop()

        return score

    def collision_walls(self, game_over):
        if (
            self.x < self.grid.margin
            or self.x > p.get_screen_width() - self.width - self.grid.margin
        ):
            game_over = True
        elif (
            self.y < self.grid.margin
            or self.y > p.get_screen_height() - self.height - self.grid.margin
        ):
            game_over = True

        return game_over

    def collision_itself(self, game_over):
        for segment in self.list[1:]:
            if p.check_collision_recs(
                (self.list[0][0], self.list[0][1], self.width, self.height),
                (segment[0], segment[1], self.width, self.height),
            ):
                game_over = True
                return game_over
