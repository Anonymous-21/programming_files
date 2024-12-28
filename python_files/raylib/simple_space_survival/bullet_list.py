import pyray as p
from math import sqrt

from bullet import Bullet

BULLET_RANGE = 1000


class BulletList:
    def __init__(
        self, spritesheet: p.Texture, sprite_dict: dict[str, p.Rectangle]
    ) -> None:
        self.spritesheet: p.Texture = spritesheet
        self.sprite_dict: dict[str, p.Rectangle] = sprite_dict

        self.list: list[Bullet] = []

        self.last_current_time: float = 0
        self.spawn_interval: float = 0.18

    def draw(self) -> None:
        for bullet in self.list:
            bullet.draw()

    def update(
        self,
        player_dest_x: float,
        player_dest_y: float,
        target_x: float,
        target_y: float,
    ) -> None:
        current_time: float = p.get_time()
        if current_time - self.last_current_time >= self.spawn_interval:
            self.list.append(
                Bullet(
                    self.spritesheet,
                    self.sprite_dict,
                    player_dest_x,
                    player_dest_y,
                    target_x,
                    target_y,
                )
            )

            self.last_current_time = current_time

        for bullet in self.list:
            bullet.update()

            distance_x: float = player_dest_x - bullet.dest.x
            distance_y: float = player_dest_y - bullet.dest.y
            distance: float = sqrt((distance_x**2) + (distance_y**2))

            if distance > BULLET_RANGE:
                self.list.remove(bullet)
