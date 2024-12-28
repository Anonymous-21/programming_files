import pyray as p


from player import Player
from enemy_list import EnemyList


class CollisionHandler:
    def __init__(self, spritesheet, sprite_dict):
        self.player = Player()
        self.enemy_list = EnemyList(spritesheet, sprite_dict, self.player)
        