import raylib as r


class Snake:
    def __init__(self, box_size) -> None:
        self.initial_x = 0
        self.initial_y = 0
        self.x = self.initial_x
        self.y = self.initial_y
        self.width = box_size
        self.height = box_size
        self.color = r.BLUE
        self.speed = box_size

        self.direction = "right"

        self.frames_counter = 0

        self.list = [[self.x, self.y]]

    def draw(self):
        for segment in self.list:
            r.DrawRectangle(segment[0], segment[1], self.width, self.height, self.color)

    def move(self):
        if r.IsKeyPressed(r.KEY_RIGHT) and self.direction != "left":
            self.direction = "right"
        elif r.IsKeyPressed(r.KEY_LEFT) and self.direction != "right":
            self.direction = "left"
        elif r.IsKeyPressed(r.KEY_UP) and self.direction != "down":
            self.direction = "up"
        elif r.IsKeyPressed(r.KEY_DOWN) and self.direction != "up":
            self.direction = "down"

        self.frames_counter += 1
        if self.frames_counter % 5 == 0:
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

    def check_collision(self, game_over, food):
        # with walls
        if self.x < 0 or self.x > r.GetScreenWidth():
            game_over = True
        elif self.y < 0 or self.y > r.GetScreenHeight():
            game_over = True

        # with food
        if r.CheckCollisionRecs(
            (self.list[0][0], self.list[0][1], self.width, self.height),
            (food.x, food.y, food.width, food.height),
        ):
            self.list.append(self.list[-1])
            food.x, food.y = food.gen_random_coordinates()

        return (game_over, food.x, food.y)
