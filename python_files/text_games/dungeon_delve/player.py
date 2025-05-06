from abc import ABC

player_types: list[str] = [
    "warrior",
    "ranger",
    "mage",
    "cleric",
    "rogue",
    "paladin",
    "berserker",
    "necromancer",
    "druid",
    "monk",
]


class Player(ABC):
    def __init__(self) -> None:
        self.x: int = 0
        self.y: int = 0
        self.level: int = 1
        self.gold: int = 0

    def is_alive(self) -> bool:
        return self.base_health > 0

    def move_north(self) -> None:
        self.y -= 1

    def move_south(self) -> None:
        self.y += 1

    def move_east(self) -> None:
        self.x += 1

    def move_west(self) -> None:
        self.x -= 1


class Warrior(Player):
    def __init__(self) -> None:
        super().__init__()

        self.base_health: int = 90
        self.base_damage: int = 8
        self.health_growth_rate: int = 1.12
        self.damage_growth_rate: int = 1.06


class Ranger(Player):
    def __init__(self) -> None:
        super().__init__()

        self.base_health: int = 60
        self.base_damage: int = 11
        self.health_growth_rate: int = 1.08
        self.damage_growth_rate: int = 1.12


class Mage(Player):
    def __init__(self) -> None:
        super().__init__()

        self.base_health: int = 50
        self.base_damage: int = 14
        self.health_growth_rate: int = 1.05
        self.damage_growth_rate: int = 1.15


class Cleric(Player):
    def __init__(self) -> None:
        super().__init__()

        self.base_health: int = 65
        self.base_damage: int = 6
        self.health_growth_rate: int = 1.10
        self.damage_growth_rate: int = 1.04


class Rogue(Player):
    def __init__(self) -> None:
        super().__init__()

        self.base_health: int = 55
        self.base_damage: int = 13
        self.health_growth_rate: int = 1.07
        self.damage_growth_rate: int = 1.14


class Paladin(Player):
    def __init__(self) -> None:
        super().__init__()

        self.base_health: int = 80
        self.base_damage: int = 9
        self.health_growth_rate: int = 1.11
        self.damage_growth_rate: int = 1.08


class Berserker(Player):
    def __init__(self) -> None:
        super().__init__()

        self.base_health: int = 70
        self.base_damage: int = 12
        self.health_growth_rate: int = 1.10
        self.damage_growth_rate: int = 1.13


class Necromancer(Player):
    def __init__(self) -> None:
        super().__init__()

        self.base_health: int = 50
        self.base_damage: int = 10
        self.health_growth_rate: int = 1.06
        self.damage_growth_rate: int = 1.10


class Druid(Player):
    def __init__(self) -> None:
        super().__init__()

        self.base_health: int = 65
        self.base_damage: int = 9
        self.health_growth_rate: int = 1.10
        self.damage_growth_rate: int = 1.09


class Monk(Player):
    def __init__(self) -> None:
        super().__init__()

        self.base_health: int = 60
        self.base_damage: int = 10
        self.health_growth_rate: int = 1.09
        self.damage_growth_rate: int = 1.10
