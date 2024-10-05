from pyray import *
import os

from spritesheet_xml_parser import xml_parser
from plane import Plane
from background import Background
from ground import Ground
from rock import Rock
from fonts import Font

os.chdir("/home/anonymous/Downloads/programming_files/python_files/raylib/tappy_plane")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480
SCREEN_TITLE = "TAPPY PLANE"
SCREEN_BACKGROUND = RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self):
        self.game_over = False
        self.get_ready = True
        self.frames_counter = 0
        self.frame_num = 1
        self.score = 0
        self.change_season_score = 1000  # change season at given score

        self.spritesheet = load_texture("assets/sheet.png")
        self.spritesheet_xml = "assets/sheet.xml"
        self.sprite_dict = xml_parser(self.spritesheet_xml)

        self.plane = Plane(self.spritesheet, self.sprite_dict)
        self.background = Background(self.spritesheet, self.sprite_dict)
        self.ground = Ground(self.spritesheet, self.sprite_dict)
        self.rock = Rock(self.spritesheet, self.sprite_dict)
        self.font = Font(self.spritesheet, self.sprite_dict)

    def draw(self):
        self.background.draw()
        self.rock.draw()
        self.ground.draw()
        self.plane.draw()

        # draw Score
        draw_text(str(int(self.score)), get_screen_width() - 150, 20, 30, GRAY)

    def update(self):
        self.score += 0.1
        self.background.animation()
        self.rock.animation(self.score, self.change_season_score)
        self.ground.animation(self.score, self.change_season_score)
        self.plane.update()
        self.plane.jump()

    def check_collision(self):
        # collision between rocks (triangles) and player (Rectangle)
        # check every point of rectangle collision with triangle(Rock)
        # triangle
        if check_collision_point_triangle(
            (self.plane.x_window, self.plane.y_window),
            self.rock.triangle1[1],
            self.rock.triangle1[2],
            self.rock.triangle1[3],
        ):
            self.game_over = True
        elif check_collision_point_triangle(
            (self.plane.x_window + self.plane.width, self.plane.y_window),
            self.rock.triangle1[1],
            self.rock.triangle1[2],
            self.rock.triangle1[3],
        ):
            self.game_over = True
        elif check_collision_point_triangle(
            (self.plane.x_window, self.plane.y_window + self.plane.height),
            self.rock.triangle1[1],
            self.rock.triangle1[2],
            self.rock.triangle1[3],
        ):
            self.game_over = True
        elif check_collision_point_triangle(
            (
                self.plane.x_window + self.plane.width,
                self.plane.y_window + self.plane.height,
            ),
            self.rock.triangle1[1],
            self.rock.triangle1[2],
            self.rock.triangle1[3],
        ):
            self.game_over = True

        # triangle down
        if check_collision_point_triangle(
            (self.plane.x_window, self.plane.y_window),
            self.rock.triangle2[1],
            self.rock.triangle2[2],
            self.rock.triangle2[3],
        ):
            self.game_over = True
        elif check_collision_point_triangle(
            (self.plane.x_window + self.plane.width, self.plane.y_window),
            self.rock.triangle2[1],
            self.rock.triangle2[2],
            self.rock.triangle2[3],
        ):
            self.game_over = True
        elif check_collision_point_triangle(
            (self.plane.x_window, self.plane.y_window + self.plane.height),
            self.rock.triangle2[1],
            self.rock.triangle2[2],
            self.rock.triangle2[3],
        ):
            self.game_over = True
        elif check_collision_point_triangle(
            (
                self.plane.x_window + self.plane.width,
                self.plane.y_window + self.plane.height,
            ),
            self.rock.triangle2[1],
            self.rock.triangle2[2],
            self.rock.triangle2[3],
        ):
            self.game_over = True

    def collision_with_ground(self):
        for coordinate in self.ground.line_strip:
            if check_collision_point_rec(coordinate,
                                         self.plane.current_frame):
                self.game_over = True

    def get_ready_menu(self):
        if self.get_ready:
            self.frames_counter += 1
            if self.frames_counter > 60:
                self.frames_counter = 0
                self.frame_num += 1
                if self.frame_num > 6:
                    self.get_ready = False

            match self.frame_num:
                case 1:
                    self.font.draw_numbers(
                        5,
                        (
                            get_screen_width() / 2 - self.font.numbers_width / 2,
                            get_screen_height() / 2 - self.font.numbers_height / 2,
                        ),
                    )
                case 2:
                    self.font.draw_numbers(
                        4,
                        (
                            get_screen_width() / 2 - self.font.numbers_width / 2,
                            get_screen_height() / 2 - self.font.numbers_height / 2,
                        ),
                    )
                case 3:
                    self.font.draw_numbers(
                        3,
                        (
                            get_screen_width() / 2 - self.font.numbers_width / 2,
                            get_screen_height() / 2 - self.font.numbers_height / 2,
                        ),
                    )
                case 4:
                    self.font.draw_numbers(
                        2,
                        (
                            get_screen_width() / 2 - self.font.numbers_width / 2,
                            get_screen_height() / 2 - self.font.numbers_height / 2,
                        ),
                    )
                case 5:
                    self.font.draw_numbers(
                        1,
                        (
                            get_screen_width() / 2 - self.font.numbers_width / 2,
                            get_screen_height() / 2 - self.font.numbers_height / 2,
                        ),
                    )
                case 6:
                    self.font.draw_get_ready()

    def game_over_menu(self):
        if self.game_over:
            self.font.draw_game_over()

            if is_key_pressed(KeyboardKey.KEY_ENTER):
                self.game_over = False
                self.get_ready = True
                self.frame_num = 1
                self.frames_counter = 0
                self.score = 0
                self.plane = Plane(self.spritesheet, self.sprite_dict)
                self.background = Background(self.spritesheet, self.sprite_dict)
                self.ground = Ground(self.spritesheet, self.sprite_dict)
                self.rock = Rock(self.spritesheet, self.sprite_dict)


def main():
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    set_target_fps(GAME_FPS)

    game = Game()

    while not window_should_close():
        begin_drawing()
        clear_background(SCREEN_BACKGROUND)

        game.draw()
        if not game.game_over and not game.get_ready:
            game.update()
            game.check_collision()
            game.collision_with_ground()
        elif game.get_ready:
            game.get_ready_menu()
        elif game.game_over:
            game.game_over_menu()

        end_drawing()

    unload_texture(game.spritesheet)
    close_window()


if __name__ == "__main__":
    main()
