import pyray as p
from dataclasses import dataclass

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Flappy Bird"
SCREEN_BACKGROUND = p.RAYWHITE


class Player:
    def __init__(self):
        self.x = 200
        self.y = p.get_screen_height() / 2
        self.width = 50
        self.height = 50
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
        # jump
        if p.is_key_pressed(p.KeyboardKey.KEY_UP):
            self.change_y = self.jump_strength
            self.active = True

        # add gravity
        if self.active:
            self.change_y += self.gravity * p.get_frame_time()
            self.y += self.change_y * p.get_frame_time()

        # player bounds
        self.y = max(0, min(self.y, p.get_screen_height() - self.height))


@dataclass
class Pillar:
    x: float
    y: float
    width: float
    height: float
    scored: bool


class Pillars:
    def __init__(self):
        self.list = []
        self.vertical_gap = 200
        self.horizontal_gap = 300
        self.color = p.DARKGREEN
        self.speed = 200

    def draw(self):
        for pillar in self.list:
            # top pillar
            p.draw_rectangle_rec(
                p.Rectangle(pillar.x, pillar.y, pillar.width, pillar.height), self.color
            )

            # bottom pillar
            bottom_y = pillar.height + self.vertical_gap
            p.draw_rectangle_rec(
                p.Rectangle(
                    pillar.x,
                    bottom_y,
                    pillar.width,
                    p.get_screen_height() - bottom_y,
                ),
                self.color,
            )

    def update(self):
        # fill pillar list
        if (
            len(self.list) <= 0
            or self.list[-1].x + self.list[-1].width + self.vertical_gap
            < p.get_screen_width()
        ):
            pillar = Pillar(
                p.get_screen_width(),
                0,
                50,
                p.get_random_value(0, p.get_screen_height() - self.horizontal_gap),
                False,
            )

            self.list.append(pillar)

        # move and remove pillars
        for pillar in self.list:
            pillar.x -= self.speed * p.get_frame_time()

            # remove offscreen pillars
            if pillar.x + pillar.width + self.horizontal_gap < 0:
                self.list.remove(pillar)


class Game:
    def __init__(self):
        self.score = 0
        self.game_over = False

        self.pillars = Pillars()
        self.player = Player()

    def draw(self):
        self.pillars.draw()
        self.player.draw()

        # draw score
        p.draw_text(f"Score: {self.score}", 10, 10, 30, p.BLACK)

        if self.game_over:
            p.draw_text(
                "GAME OVER",
                p.get_screen_width() // 2 - 100,
                p.get_screen_height() // 2 - 20,
                40,
                p.BLACK,
            )
            p.draw_text(
                "Press ENTER to restart",
                p.get_screen_width() // 2 - 150,
                p.get_screen_height() // 2 + 100,
                30,
                p.BLACK,
            )

    def update(self):
        if not self.game_over:
            self.player.update()
            self.pillars.update()

            # pillars collision player
            for pillar in self.pillars.list:
                # update scores
                if self.player.x > pillar.x + pillar.width:
                    if not pillar.scored:
                        self.score += 1
                        pillar.scored = True

                if p.check_collision_recs(
                    p.Rectangle(pillar.x, pillar.y, pillar.width, pillar.height),
                    p.Rectangle(
                        self.player.x,
                        self.player.y,
                        self.player.width,
                        self.player.height,
                    ),
                ):
                    self.game_over = True

                bottom_y = pillar.height + self.pillars.vertical_gap
                if p.check_collision_recs(
                    p.Rectangle(
                        pillar.x,
                        bottom_y,
                        pillar.width,
                        p.get_screen_height() - bottom_y,
                    ),
                    p.Rectangle(
                        self.player.x,
                        self.player.y,
                        self.player.width,
                        self.player.height,
                    ),
                ):
                    self.game_over = True

            # player falling down
            if self.player.y >= p.get_screen_height() - self.player.height:
                self.game_over = True

        else:
            if p.is_key_pressed(p.KeyboardKey.KEY_ENTER):
                self.game_over = False
                self.score = 0

                self.pillars = Pillars()
                self.player = Player()


def main():
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
