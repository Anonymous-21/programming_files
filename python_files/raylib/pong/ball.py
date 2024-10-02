import raylib as r


class Ball:
    def __init__(self) -> None:
        self.radius = 10
        self.initial_pos = (
            r.GetScreenWidth() // 2 - self.radius,
            r.GetScreenHeight() // 2 - self.radius,
        )
        self.x, self.y = self.initial_pos
        self.color = r.RED
        self.change_x = 5
        self.change_y = 6

        self.frames_counter = 0

    def draw(self):
        r.DrawCircle(self.x, self.y, self.radius, self.color)

    def move(self, left_score, right_score):
        self.frames_counter += 1
        if self.frames_counter > 120:
            self.x += self.change_x
            self.y += self.change_y

        if self.x <= 0:
            right_score += 1
            self.x, self.y = self.initial_pos
        elif self.x >= r.GetScreenWidth() - self.radius:
            left_score += 1
            self.x, self.y = self.initial_pos
        elif self.y <= 0 or self.y >= r.GetScreenHeight() - self.radius:
            self.change_y *= -1

        return (left_score, right_score)
