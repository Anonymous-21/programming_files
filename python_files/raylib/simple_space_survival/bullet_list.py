import pyray as p
from math import sqrt

from bullet import Bullet

BULLET_RANGE = 400


class BulletList:
    def __init__(self, spritesheet, sprite_dict):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.list = []
        self.last_current_time = 0
        self.move_interval = 0.5

    def draw(self):
        for bullet in self.list:
            bullet.draw()

    def update(self, owner_x, owner_y, world_mouse_x, world_mouse_y):
        current_time = p.get_time()
        if current_time - self.last_current_time >= self.move_interval:
            self.list.append(
                Bullet(
                    self.spritesheet,
                    self.sprite_dict,
                    owner_x,
                    owner_y,
                    world_mouse_x,
                    world_mouse_y,
                )
            )

            self.last_current_time = current_time

        for bullet in self.list:
            bullet.update()

            distance_x = bullet.dest.x - owner_x
            distance_y = bullet.dest.y - owner_y
            distance = sqrt((distance_x**2) + (distance_y**2))
            if distance > BULLET_RANGE:
                self.list.remove(bullet)
