import pyray as p
from random import randint
from math import atan2, degrees, sqrt


class Enemy:
    def __init__(self, spritesheet, sprite_dict):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.enemies = {
            "black1": self.sprite_dict["enemyBlack1.png"],
            "black2": self.sprite_dict["enemyBlack2.png"],
            "black3": self.sprite_dict["enemyBlack3.png"],
            "black4": self.sprite_dict["enemyBlack4.png"],
            "black5": self.sprite_dict["enemyBlack5.png"],
            "blue1": self.sprite_dict["enemyBlue1.png"],
            "blue2": self.sprite_dict["enemyBlue2.png"],
            "blue3": self.sprite_dict["enemyBlue3.png"],
            "blue4": self.sprite_dict["enemyBlue4.png"],
            "blue5": self.sprite_dict["enemyBlue5.png"],
            "green1": self.sprite_dict["enemyGreen1.png"],
            "green2": self.sprite_dict["enemyGreen2.png"],
            "green3": self.sprite_dict["enemyGreen3.png"],
            "green4": self.sprite_dict["enemyGreen4.png"],
            "green5": self.sprite_dict["enemyGreen5.png"],
            "red1": self.sprite_dict["enemyRed1.png"],
            "red2": self.sprite_dict["enemyRed2.png"],
            "red3": self.sprite_dict["enemyRed3.png"],
            "red4": self.sprite_dict["enemyRed4.png"],
            "red5": self.sprite_dict["enemyRed5.png"],
        }

        self.current_sprite = self.enemies["black1"]

        self.source = p.Rectangle(
            self.current_sprite.x,
            self.current_sprite.y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.dest = p.Rectangle(
            randint(0, p.get_screen_width()),
            -100,
            self.current_sprite.width / 2,
            self.current_sprite.height / 2,
        )
        self.origin = p.Vector2(self.dest.width / 2, self.dest.height / 2)
        self.rotation = 0
        self.tint = p.WHITE
        self.speed = 3

    def draw(self):
        p.draw_texture_pro(
            self.spritesheet,
            self.source,
            self.dest,
            self.origin,
            self.rotation,
            self.tint,
        )

    def rotate(self, target_x, target_y):
        dx = target_x - self.dest.x
        dy = target_y - self.dest.y
        self.rotation = degrees(atan2(dy, dx))
        self.rotation -= 90

    def move(self, target_x, target_y):
        distance_x = target_x - self.dest.x
        distance_y = target_y - self.dest.y
        distance = sqrt((distance_x**2) + (distance_y**2))

        if distance > 0:
            distance_x /= distance
            distance_y /= distance

            self.dest.x += distance_x * self.speed
            self.dest.y += distance_y * self.speed

    def update(self, target_x, target_y):
        self.rotate(target_x, target_y)
        self.move(target_x, target_y)
