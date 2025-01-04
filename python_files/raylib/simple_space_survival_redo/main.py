import pyray as p
from os import chdir

from utils import xml_parser
from player import Player
from enemy_list import EnemyList

chdir(
    "/home/anonymous/Downloads/programming_files/python_files/raylib/simple_space_survival_redo"
)

SCREEN_WIDTH: int = 1000
SCREEN_HEIGHT: int = 800
SCREEN_TITLE: str = "Simple Space Survival"
SCREEN_BACKGROUND: p.Color = p.RAYWHITE
GAME_FPS: int = 60


class Game:
    def __init__(self) -> None:
        self.spritesheet: p.Texture = p.load_texture("assets/simpleSpace_sheet.png")
        self.spritesheet_xml: str = "assets/simpleSpace_sheet.xml"
        self.sprite_dict: dict[str, p.Rectangle] = xml_parser(self.spritesheet_xml)

        self.background: p.Texture = p.load_texture("assets/background.png")

        self.game_over: bool = False

        self.camera = p.Camera2D()
        self.camera.rotation = 0
        self.camera.zoom = 1

        self.player = Player(self.spritesheet, self.sprite_dict, self.background)
        self.enemy_list = EnemyList()

    def draw(self) -> None:
        # draw background
        p.draw_texture(self.background, 0, 0, p.WHITE)

        self.player.draw()
        self.enemy_list.draw()

        if self.game_over:
            p.draw_text(
                "Game Over",
                p.get_screen_width() // 2 - 70,
                p.get_screen_height() // 2 + 100,
                30,
                p.WHITE,
            )

    def update_camera(self) -> None:
        # set and update camera attributes
        self.camera.offset = p.Vector2(
            p.get_screen_width() / 2, p.get_screen_height() / 2
        )

        self.camera.target.x = max(
            p.get_screen_width() / 2,
            min(self.player.dest.x, self.background.width - p.get_screen_width() / 2),
        )
        self.camera.target.y = max(
            p.get_screen_height() / 2,
            min(self.player.dest.y, self.background.height - p.get_screen_height() / 2),
        )

    def update(self) -> None:
        if not self.game_over:
            self.update_camera()

            # world mouse position
            mouse_x: float = (
                p.get_mouse_x() - p.get_screen_width() / 2 + self.camera.target.x
            )
            mouse_y: float = (
                p.get_mouse_y() - p.get_screen_height() / 2 + self.camera.target.y
            )

            # update entities
            self.player.update(mouse_x, mouse_y)
            self.enemy_list.update(
                self.spritesheet,
                self.sprite_dict,
                self.player.dest.x,
                self.player.dest.y,
            )

            # enemy collision player
            for enemy in self.enemy_list.list:
                if p.check_collision_recs(self.player.dest, enemy.dest):
                    if self.player.is_alive():
                        self.player.health -= enemy.damage
                    elif not self.player.is_alive():
                        self.game_over = True

            # enemy collision bullet
            for enemy in self.enemy_list.list:
                for bullet in self.player.bullets.list:
                    if p.check_collision_recs(bullet.dest, enemy.dest):
                        self.player.bullets.list.remove(bullet)
                        enemy.health -= bullet.damage

                        if not enemy.is_alive():
                            self.enemy_list.list.remove(enemy)

        else:
            if p.is_key_pressed(p.KeyboardKey.KEY_ENTER):
                self.game_over = False
                self.player = Player(
                    self.spritesheet, self.sprite_dict, self.background
                )
                self.enemy_list = EnemyList()


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    game = Game()

    while not p.window_should_close():
        game.update()

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)
        p.begin_mode_2d(game.camera)

        game.draw()

        p.end_mode_2d()
        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
