import raylib as r


class Snake:
    def __init__(self, box_size) -> None:
        self.x = 0
        self.y = 0
        self.width = box_size
        self.height = box_size
        self.color = r.BLUE
        self.speed = box_size
        self.direction = "right"
        self.list = [[self.x, self.y]]
        self.frames_counter = 0

    def draw(self):
        for segment in self.list:
            r.DrawRectangle(segment[0], segment[1], self.width, self.height, self.color)

    def on_key_press(self):
        if r.IsKeyPressed(r.KEY_RIGHT) and self.direction != "left":
            self.direction = "right"
        elif r.IsKeyPressed(r.KEY_LEFT) and self.direction != "right":
            self.direction = "left"
        elif r.IsKeyPressed(r.KEY_UP) and self.direction != "down":
            self.direction = "up"
        elif r.IsKeyPressed(r.KEY_DOWN) and self.direction != "up":
            self.direction = "down"

    def update(self, food, score):
        # adjust player speed, block_size as speed is too fast
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

            # check food collision before eating so that it does not
            # consider eating food as collision (part of snake)
            if r.CheckCollisionRecs(
                (self.list[0][0], self.list[0][1], self.width, self.height),
                (food.x, food.y, food.width, food.height),
            ):
                self.list.append(self.list[-1])
                score += 1
                food.x, food.y = food.gen_random_coordinates()

            self.list.insert(0, [self.x, self.y])
            self.list.pop()

        return (food.x, food.y, score)

    def check_collision_walls(self):
        if (
            self.x < 0
            or self.x > r.GetScreenWidth() - self.width
            or self.y < 0
            or self.y > r.GetScreenHeight() - self.height
        ):
            return True

        return False

    def check_collision_itself(self):
        for segment in self.list[1:]:
            if r.CheckCollisionRecs(
                (self.list[0][0], self.list[0][1], self.width, self.height),
                (segment[0], segment[1], self.width, self.height),
            ):
                return True
            
        return False
