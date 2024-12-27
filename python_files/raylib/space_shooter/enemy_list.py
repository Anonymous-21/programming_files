import pyray as p

from enemy import Enemy


class EnemyList:
    def __init__(self, spritesheet, sprite_dict, player):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict
        self.player = player

        self.list = []

        self.last_current_time = 0
        self.enemy_spawn_interval = 2

    def draw(self):
        for enemy in self.list:
            enemy.draw()

    def update(self):
        current_time = p.get_time()
        if current_time - self.last_current_time >= self.enemy_spawn_interval:
            self.list.append(Enemy(self.spritesheet, self.sprite_dict))

            self.last_current_time = current_time

        for enemy in self.list:
            enemy.update(self.player.dest.x, self.player.dest.y)
