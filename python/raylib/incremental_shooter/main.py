import pyray as p

from player import Player

SCREEN_WIDTH: int = 1200
SCREEN_HEIGHT: int = 800
SCREEN_TITLE: str = "Incremental Shooter"
SCREEN_BACKGROUND: p.Color = p.RAYWHITE


class Game:
    def __init__(self) -> None:
        self.player: Player = Player()

    def draw(self) -> None:
        self.player.draw()

    def update(self) -> None:
        self.player.update()


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
