import pyray as p

from player import Player
from enemy_list import EnemyList
from enemy_list import Enemy


class Collision_handler:
    def __init__(self, player: Player, enemy_list: EnemyList) -> None:
        self.player: Player = player
        self.enemy_list: EnemyList = enemy_list

    def enemy_collision_bullet(self) -> None:
        dead_enemy_list: list[Enemy] = []
        for enemy in self.enemy_list.list:
            enemy.tint = p.WHITE # default enemy tint
            for bullet in self.player.bullet_list.list:
                if p.check_collision_recs(enemy.dest, bullet.dest):
                    enemy.tint = p.RED # change tint to red per collision
                    self.player.attack(enemy)
                    if not enemy.is_alive():
                        dead_enemy_list.append(enemy)

        for dead_enemy in dead_enemy_list:
            if dead_enemy in self.enemy_list.list:
                self.enemy_list.list.remove(dead_enemy)
