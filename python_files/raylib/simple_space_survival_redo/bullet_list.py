import pyray as p
from math import sqrt

from bullet import Bullet

BULLET_RANGE: float = 400


class BulletList:
    def __init__(self) -> None:
        self.list: list[Bullet] = []

        self.last_current_time: float = 0
        self.movement_interval: float = 0.08

    def draw(self) -> None:
        for bullet in self.list:
            bullet.draw()

    def update(
        self,
        spritesheet: p.Texture,
        sprite_dict: dict[str, p.Rectangle],
        mouse_x: float,
        mouse_y: float,
        spawn_x: float,
        spawn_y: float,
    ) -> None:
        
        current_time: float = p.get_time()
        if current_time - self.last_current_time >= self.movement_interval:
            self.list.append(
                Bullet(
                    spritesheet,
                    sprite_dict,
                    spawn_x,
                    spawn_y,
                    mouse_x,
                    mouse_y,
                )
            )

            self.last_current_time = current_time

        for bullet in self.list:
            bullet.update(mouse_x, mouse_y)

            distance_x: float = spawn_x - bullet.dest.x
            distance_y: float = spawn_y - bullet.dest.y
            distance: float = sqrt((distance_x**2) + (distance_y**2))
            if distance > BULLET_RANGE:
                self.list.remove(bullet)
