import pyray as p

from weapons import LaserBullet


class WeaponList:
    def __init__(self) -> None:
        self.list: list[LaserBullet] = []

    def draw(self) -> None:
        for weapon in self.list:
            weapon.draw()

    def update(self, target_pos: p.Vector2) -> None:
        for weapon in self.list:
            weapon.update(target_pos)
