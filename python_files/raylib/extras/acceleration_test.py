import pyray as p

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = ""
SCREEN_BACKGROUND: p.Color = p.RAYWHITE
GAME_FPS = 60


class Player:
    def __init__(self):
        self.rect = p.Rectangle(20, 20, 30, 30)
        self.color = p.BLUE

        self.friction = 0.03
        self.acceleration = 0.1
        self.max_speed = 3

        self.change_x = 0
        self.change_y = 0

    def draw(self):
        p.draw_rectangle_rec(self.rect, self.color)

    def update(self):
        if self.change_x < self.friction:
            self.change_x += self.friction
        elif self.change_x > self.friction:
            self.change_x -= self.friction
        else:
            self.change_x = 0

        if self.change_y < self.friction:
            self.change_y += self.friction
        elif self.change_y > self.friction:
            self.change_y -= self.friction
        else:
            self.change_y = 0

        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if p.is_key_down(p.KeyboardKey.KEY_UP) and not p.is_key_down(
            p.KeyboardKey.KEY_DOWN
        ):
            self.change_y -= self.acceleration
            if p.is_key_down(p.KeyboardKey.KEY_LEFT) and not p.is_key_down(
                p.KeyboardKey.KEY_RIGHT
            ):
                self.change_x -= self.acceleration
            elif p.is_key_down(p.KeyboardKey.KEY_RIGHT) and not p.is_key_down(
                p.KeyboardKey.KEY_LEFT
            ):
                self.change_x += self.acceleration
        elif p.is_key_down(p.KeyboardKey.KEY_DOWN) and not p.is_key_down(
            p.KeyboardKey.KEY_UP
        ):
            self.change_y += self.acceleration
            if p.is_key_down(p.KeyboardKey.KEY_LEFT) and not p.is_key_down(
                p.KeyboardKey.KEY_RIGHT
            ):
                self.change_x -= self.acceleration
            elif p.is_key_down(p.KeyboardKey.KEY_RIGHT) and not p.is_key_down(
                p.KeyboardKey.KEY_LEFT
            ):
                self.change_x += self.acceleration
        elif p.is_key_down(p.KeyboardKey.KEY_LEFT) and not p.is_key_down(
            p.KeyboardKey.KEY_RIGHT
        ):
            self.change_x -= self.acceleration
        elif p.is_key_down(p.KeyboardKey.KEY_RIGHT) and not p.is_key_down(
            p.KeyboardKey.KEY_LEFT
        ):
            self.change_x += self.acceleration

        if self.change_x > self.max_speed:
            self.change_x = self.max_speed
        elif self.change_y > self.max_speed:
            self.change_y = self.max_speed

        if self.rect.x <= 0:
            self.rect.x = 0
            if self.rect.y <= 0:
                self.rect.y = 0
            elif self.rect.y >= p.get_screen_height() - self.rect.height:
                self.rect.y = p.get_screen_height() - self.rect.height
        elif self.rect.x >= p.get_screen_width() - self.rect.width:
            self.rect.x = p.get_screen_width() - self.rect.width
            if self.rect.y <= 0:
                self.rect.y = 0
            elif self.rect.y >= p.get_screen_height() - self.rect.height:
                self.rect.y = p.get_screen_height() - self.rect.height
        elif self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= p.get_screen_height() - self.rect.height:
            self.rect.y = p.get_screen_height() - self.rect.height


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    player = Player()

    while not p.window_should_close():
        player.update()

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        player.draw()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
