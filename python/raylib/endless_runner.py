import pyray as p
from dataclasses import dataclass

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 200
SCREEN_TITLE = "Endless Runner"
SCREEN_BACKGROUND = p.SKYBLUE


class Player:
    def __init__(self):
        self.width = 20
        self.height = 80
        self.x = 100
        self.y = p.get_screen_height() - self.height
        self.color = p.RED
        self.change_y = 0
        self.gravity = 1500
        self.jump_strength = -500
        self.active = False

    def draw(self):
        p.draw_rectangle_rec(
            p.Rectangle(self.x, self.y, self.width, self.height), self.color
        )

    def update(self):
        if p.is_key_pressed(p.KeyboardKey.KEY_UP):
            self.active = True
            self.change_y = self.jump_strength

        if self.active:
            self.change_y += self.gravity * p.get_frame_time()
            self.y += self.change_y * p.get_frame_time()

        self.y = max(0, min(self.y, p.get_screen_height() - self.height))


@dataclass
class Pillar:
    x: float
    y: float
    width: float
    height: float
    scored: int


class Pillars:
    def __init__(self):
        self.list = []
        self.color = p.DARKGREEN
        self.speed = 200.0

    def draw(self):
        for pillar in self.list:
            p.draw_rectangle_rec(
                p.Rectangle(pillar.x, pillar.y, pillar.width, pillar.height),
                self.color,
            )

    def update(self):
        self.horizontal_gap = p.get_random_value(150, 250)
        if (
            len(self.list) <= 0
            or self.list[-1].x + self.list[-1].width
            < p.get_screen_width() - self.horizontal_gap
        ):
            random_height = p.get_random_value(20, 50)
            pillar = Pillar(
                width=p.get_random_value(10, 40),
                height=random_height,
                x=p.get_screen_width(),
                y=p.get_screen_height() - random_height,
                scored=False,
            )

            self.list.append(pillar)

        for pillar in self.list:
            pillar.x -= self.speed * p.get_frame_time()

            if pillar.x + pillar.width < 0:
                self.list.remove(pillar)


class Game:
    def __init__(self):
        self.score = 0
        self.game_over = False

        self.player = Player()
        self.pillars = Pillars()

    def draw(self):
        self.player.draw()
        self.pillars.draw()

        p.draw_text(f"Score: {self.score}", 10, 10, 30, p.BLACK)

        if self.game_over:
            p.draw_text(
                "GAME OVER",
                p.get_screen_width() // 2 - 120,
                p.get_screen_height() // 2 - 40,
                40,
                p.BLACK,
            )

    def update(self):
        if not self.game_over:
            self.player.update()
            self.pillars.update()

            # player collision pillars
            for pillar in self.pillars.list:
                if p.check_collision_recs(
                    p.Rectangle(
                        self.player.x,
                        self.player.y,
                        self.player.width,
                        self.player.height,
                    ),
                    p.Rectangle(pillar.x, pillar.y, pillar.width, pillar.height),
                ):
                    self.game_over = True

                if self.player.x > pillar.x + pillar.width:
                    if not pillar.scored:
                        pillar.scored = True
                        self.score += 1

        else:
            if p.is_key_pressed(p.KeyboardKey.KEY_ENTER):
                self.game_over = False
                self.score = 0

                self.player = Player()
                self.pillars = Pillars()


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    game = Game()

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        game.draw()
        game.update()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
