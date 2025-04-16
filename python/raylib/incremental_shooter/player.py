import pyray as p


class Player:
    def __init__(self) -> None:
        self.width: float = 50.0
        self.height: float = self.width
        self.x: float = p.get_screen_width() / 2 - self.width / 2
        self.y: float = p.get_screen_height() / 2 - self.height / 2
        self.direction: p.Vector2 = p.Vector2(0, 0)
        self.speed: float = 300.0
        self.color: p.Color = p.BLUE

        self.barrel_width: float = 20.0
        self.barrel_height: float = 50.0
        self.barrel_x: float = self.x + self.width / 2 - self.barrel_width / 2
        self.barrel_y: float = self.y + self.height / 2
        self.barrel_color: p.Color = p.BLACK

    def draw(self) -> None:
        p.draw_rectangle_rec(
            p.Rectangle(self.x, self.y, self.width, self.height), self.color
        )

        # draw barrel
        p.draw_rectangle_rec(
            p.Rectangle(
                self.barrel_x, self.barrel_y, self.barrel_width, self.barrel_height
            ),
            self.barrel_color,
        )

    def update(self) -> None:
        # get input and move player
        self.direction.x = int(
            p.is_key_down(p.KeyboardKey.KEY_RIGHT) or p.is_key_down(p.KeyboardKey.KEY_D)
        ) - int(
            p.is_key_down(p.KeyboardKey.KEY_LEFT) or p.is_key_down(p.KeyboardKey.KEY_A)
        )
        self.direction.y = int(
            p.is_key_down(p.KeyboardKey.KEY_DOWN) or p.is_key_down(p.KeyboardKey.KEY_S)
        ) - int(
            p.is_key_down(p.KeyboardKey.KEY_UP) or p.is_key_down(p.KeyboardKey.KEY_W)
        )

        if self.direction.x != 0 and self.direction.y != 0:
            self.direction = p.vector2_normalize(self.direction)

        self.x += self.direction.x * self.speed * p.get_frame_time()
        self.y += self.direction.y * self.speed * p.get_frame_time()

        # player bounds
        self.x = max(0, min(self.x, p.get_screen_width() - self.width))
        self.y = max(0, min(self.y, p.get_screen_height() - self.height))
