import pyray as p

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_BACKGROUND
from balls import BallNormal
from bricks import Bricks


class Game:
    def __init__(self) -> None:
        self.gold: int = 0
        self.level: int = 1
        self.click_damage: int = 1

        self.ball_normal: BallNormal = BallNormal()
        self.bricks: Bricks = Bricks(self.level)

    def draw(self) -> None:
        # draw gold
        p.draw_text(f"Gold: {self.gold}", 10, 10, 30, p.BLACK)

        self.bricks.draw()
        self.ball_normal.draw()

    def update(self) -> None:
        mouse_pos: p.Vector2 = p.get_mouse_position()

        if len(self.bricks.list) <= 0:
            self.level += 1
            self.bricks = Bricks(self.level)

        self.ball_normal.update()

        for brick in self.bricks.list:
            # mouse collision bricks - click damage
            if p.check_collision_point_rec(mouse_pos, brick.rect):
                if p.is_mouse_button_pressed(p.MouseButton.MOUSE_BUTTON_LEFT):
                    brick.level -= 1
                    self.gold += 1

            # ball collision bricks
            if p.check_collision_circle_rec(
                self.ball_normal.pos, self.ball_normal.radius, brick.rect
            ):
                brick.level -= 1
                self.gold += 1
                
                if (
                    self.ball_normal.pos.x < brick.rect.x
                    or self.ball_normal.pos.x > brick.rect.x + brick.rect.width
                ):
                    self.ball_normal.direction.x *= -1
                if (
                    self.ball_normal.pos.y < brick.rect.y
                    or self.ball_normal.pos.y > brick.rect.y + brick.rect.height
                ):
                    self.ball_normal.direction.y *= -1

            # remove brick from list if destroyed
            if brick.level <= 0:
                self.bricks.list.remove(brick)


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    game: Game = Game()

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        game.draw()
        game.update()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
