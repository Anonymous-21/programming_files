from abc import ABC


class Enemy(ABC):
    def __init__(self, x: int, y: int, level: int) -> None:
        self.x: int = x
        self.y: int = y
        self.level: int = level
    
    def is_alive(self) -> bool:
        return self.base_health > 0


class Zombie(Enemy):
    def __init__(self, x, y, level) -> None:
        super().__init__(x, y, level)

        self.base_health: int = 50
        self.base_damage: int = 5
        self.health_growth_rate: int = 1.10
        self.damage_growth_rate: int = 1.05


class Goblin(Enemy):
    def __init__(self, x, y, level) -> None:
        super().__init__(x, y, level)
        self.base_health: int = 40
        self.base_damage: int = 7
        self.health_growth_rate: int = 1.08
        self.damage_growth_rate: int = 1.06


class Skeleton(Enemy):
    def __init__(self, x, y, level) -> None:
        super().__init__(x, y, level)
        self.base_health: int = 45
        self.base_damage: int = 6
        self.health_growth_rate: int = 1.09
        self.damage_growth_rate: int = 1.05


class Orc(Enemy):
    def __init__(self, x, y, level) -> None:
        super().__init__(x, y, level)
        self.base_health: int = 70
        self.base_damage: int = 10
        self.health_growth_rate: int = 1.12
        self.damage_growth_rate: int = 1.08


class Troll(Enemy):
    def __init__(self, x, y, level) -> None:
        super().__init__(x, y, level)
        self.base_health: int = 100
        self.base_damage: int = 8
        self.health_growth_rate: int = 1.15
        self.damage_growth_rate: int = 1.04


class Vampire(Enemy):
    def __init__(self, x, y, level) -> None:
        super().__init__(x, y, level)
        self.base_health: int = 65
        self.base_damage: int = 12
        self.health_growth_rate: int = 1.10
        self.damage_growth_rate: int = 1.10


class Werewolf(Enemy):
    def __init__(self, x, y, level) -> None:
        super().__init__(x, y, level)
        self.base_health: int = 80
        self.base_damage: int = 11
        self.health_growth_rate: int = 1.12
        self.damage_growth_rate: int = 1.09


class Demon(Enemy):
    def __init__(self, x, y, level) -> None:
        super().__init__(x, y, level)
        self.base_health: int = 90
        self.base_damage: int = 14
        self.health_growth_rate: int = 1.13
        self.damage_growth_rate: int = 1.12


class Dragon(Enemy):
    def __init__(self, x, y, level) -> None:
        super().__init__(x, y, level)
        self.base_health: int = 150
        self.base_damage: int = 20
        self.health_growth_rate: int = 1.18
        self.damage_growth_rate: int = 1.15


class Bandit(Enemy):
    def __init__(self, x, y, level) -> None:
        super().__init__(x, y, level)
        self.base_health: int = 55
        self.base_damage: int = 9
        self.health_growth_rate: int = 1.09
        self.damage_growth_rate: int = 1.07


class Witch(Enemy):
    def __init__(self, x, y, level) -> None:
        super().__init__(x, y, level)
        self.base_health: int = 60
        self.base_damage: int = 13
        self.health_growth_rate: int = 1.08
        self.damage_growth_rate: int = 1.13
