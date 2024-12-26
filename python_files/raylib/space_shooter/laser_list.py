import pyray as p
from math import sqrt

from laser import Laser

BULLET_RANGE = 1000


class LaserList:
    def __init__(
        self,
        spritesheet,
        sprite_dict,
    ):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict
        self.list = []

        self.last_current_time = 0
        self.shooting_interval = 0.18

    def draw(self):
        for laser in self.list:
            laser.draw()

    def update(self, spawn_x, spawn_y, target_x, target_y):
        current_time = p.get_time()
        if current_time - self.last_current_time >= self.shooting_interval:
            self.list.append(
                Laser(
                    self.spritesheet,
                    self.sprite_dict,
                    spawn_x,
                    spawn_y,
                    target_x,
                    target_y,
                )
            )

            self.last_current_time = current_time

        # remove laser after reaching bullet range
        for laser in self.list:
            laser.update()

            distance_x = spawn_x - laser.dest.x
            distance_y = spawn_y - laser.dest.y
            distance = sqrt((distance_x**2) + (distance_y**2))

            if distance > BULLET_RANGE:
                self.list.remove(laser)
