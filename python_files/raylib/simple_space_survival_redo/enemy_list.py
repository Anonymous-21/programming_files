import pyray as p
from random import uniform
from math import radians, cos, sin

from enemy import Enemy

SPAWN_DISTANCE_FROM_PLAYER: int = 600


class EnemyList:
    def __init__(self) -> None:
        self.list: list[Enemy] = []

        self.wave: int = 0
        self.enemy_count: int = 0

        self.new_wave: bool = False

    def draw(self) -> None:
        for enemy in self.list:
            enemy.draw()

    def update(
        self,
        spritesheet: p.Texture,
        sprite_dict: dict[str, p.Rectangle],
        player_dest_x: float,
        player_dest_y: float,
    ) -> None:
        
        if len(self.list) == 0:
            self.wave += 1
            self.enemy_count = self.wave * 5
            self.new_wave = True
        elif len(self.list) > 0:
            self.new_wave = False

        if self.new_wave:
            for i in range(self.enemy_count):
                random_angle: float = uniform(0, 360)
                random_distance: float = uniform(
                    SPAWN_DISTANCE_FROM_PLAYER, SPAWN_DISTANCE_FROM_PLAYER * 2
                )
                spawn_x: float = (
                    random_distance * cos(radians(random_angle)) + player_dest_x
                )
                spawn_y: float = (
                    random_distance * sin(radians(random_angle)) + player_dest_y
                )

                random_enemy_type: float = uniform(0, 100)
                if random_enemy_type < 50:
                    enemy_type: str = "basic"
                elif random_enemy_type < 75:
                    enemy_type = "fast"
                elif random_enemy_type < 90:
                    enemy_type = "strong"
                elif random_enemy_type < 95:
                    enemy_type = "tank"
                else:
                    enemy_type = "boss"

                self.list.append(
                    Enemy(spritesheet, sprite_dict, spawn_x, spawn_y, enemy_type)
                )

        for enemy in self.list:
            enemy.update(player_dest_x, player_dest_y)
