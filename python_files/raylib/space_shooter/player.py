import pyray as p
from math import atan2, degrees

from laser_list import LaserList


class Player:
    def __init__(self, spritesheet, sprite_dict):
        self.life = 3

        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.player = {
            "ship1_blue": self.sprite_dict["playerShip1_blue.png"],
            "ship1_damage1": self.sprite_dict["playerShip1_damage1.png"],
            "ship1_damage2": self.sprite_dict["playerShip1_damage2.png"],
            "ship1_damage3": self.sprite_dict["playerShip1_damage3.png"],
            "ship1_green": self.sprite_dict["playerShip1_green.png"],
            "ship1_orange": self.sprite_dict["playerShip1_orange.png"],
            "ship1_red": self.sprite_dict["playerShip1_red.png"],
            "ship2_blue": self.sprite_dict["playerShip2_blue.png"],
            "ship2_damage1": self.sprite_dict["playerShip2_damage1.png"],
            "ship2_damage2": self.sprite_dict["playerShip2_damage2.png"],
            "ship2_damage3": self.sprite_dict["playerShip2_damage3.png"],
            "ship2_green": self.sprite_dict["playerShip2_green.png"],
            "ship2_orange": self.sprite_dict["playerShip2_orange.png"],
            "ship2_red": self.sprite_dict["playerShip2_red.png"],
            "ship3_blue": self.sprite_dict["playerShip3_blue.png"],
            "ship3_damage1": self.sprite_dict["playerShip3_damage1.png"],
            "ship3_damage2": self.sprite_dict["playerShip3_damage2.png"],
            "ship3_damage3": self.sprite_dict["playerShip3_damage3.png"],
            "ship3_green": self.sprite_dict["playerShip3_green.png"],
            "ship3_orange": self.sprite_dict["playerShip3_orange.png"],
            "ship3_red": self.sprite_dict["playerShip3_red.png"],
        }
        self.player_life = {
            "blue1": self.sprite_dict["playerLife1_blue.png"],
            "green1": self.sprite_dict["playerLife1_green.png"],
            "orange1": self.sprite_dict["playerLife1_orange.png"],
            "red1": self.sprite_dict["playerLife1_red.png"],
            "blue2": self.sprite_dict["playerLife2_blue.png"],
            "green2": self.sprite_dict["playerLife2_green.png"],
            "orange2": self.sprite_dict["playerLife2_orange.png"],
            "red2": self.sprite_dict["playerLife2_red.png"],
            "blue3": self.sprite_dict["playerLife3_blue.png"],
            "green3": self.sprite_dict["playerLife3_green.png"],
            "orange3": self.sprite_dict["playerLife3_orange.png"],
            "red3": self.sprite_dict["playerLife3_red.png"],
        }

        self.current_sprite = self.player["ship1_red"]
        self.current_life_sprite = self.player_life["red1"]

        self.life_position = p.Vector2(20, 20)

        self.source = p.Rectangle(
            self.current_sprite.x,
            self.current_sprite.y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.dest = p.Rectangle(
            p.get_screen_width() / 2,
            p.get_screen_height() - 100,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.origin = p.Vector2(self.dest.width / 2, self.dest.height / 2)
        self.rotation = 0
        self.tint = p.WHITE
        self.speed = 5
        self.rotation_speed = 3

        self.laser_list = LaserList(self.spritesheet, self.sprite_dict)

    def draw(self):
        # draw player life
        self.life_position.x = 20
        for i in range(self.life):
            p.draw_texture_rec(
                self.spritesheet,
                (
                    self.current_life_sprite.x,
                    self.current_life_sprite.y,
                    self.current_life_sprite.width,
                    self.current_life_sprite.height,
                ),
                self.life_position,
                p.WHITE,
            )

            self.life_position.x += self.current_life_sprite.width + 5

        # draw player laser list
        self.laser_list.draw()

        # draw player ship
        p.draw_texture_pro(
            self.spritesheet,
            self.source,
            self.dest,
            self.origin,
            self.rotation,
            self.tint,
        )

    def rotate(self):
        dx = p.get_mouse_x() - self.dest.x
        dy = p.get_mouse_y() - self.dest.y
        self.rotation = degrees(atan2(dy, dx))
        self.rotation += 90

    def move(self):
        if p.is_key_down(p.KeyboardKey.KEY_A) and self.dest.x >= self.dest.width / 2:
            self.dest.x -= self.speed
        elif (
            p.is_key_down(p.KeyboardKey.KEY_D)
            and self.dest.x <= p.get_screen_width() - self.dest.width / 2
        ):
            self.dest.x += self.speed
        elif p.is_key_down(p.KeyboardKey.KEY_W) and self.dest.y >= self.dest.height / 2:
            self.dest.y -= self.speed
        elif (
            p.is_key_down(p.KeyboardKey.KEY_S)
            and self.dest.y <= p.get_screen_height() - self.dest.height / 2
        ):
            self.dest.y += self.speed

    def update(self):
        self.rotate()
        self.move()

        mouse_pos = p.get_mouse_position()
        self.laser_list.update(self.dest.x, self.dest.y, mouse_pos.x, mouse_pos.y)
