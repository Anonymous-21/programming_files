import pyray as p

from enemy import Enemy


class EnemyList:
    def __init__(self) -> None:
        self.list: list[Enemy] = []

        self.last_current_time: float = 0
        self.spawn_interval: float = 1

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
        current_time: float = p.get_time()
        if current_time - self.last_current_time >= self.spawn_interval:
            self.list.append(Enemy(spritesheet, sprite_dict))

            self.last_current_time = current_time

        for enemy in self.list:
            enemy.update(player_dest_x, player_dest_y)
