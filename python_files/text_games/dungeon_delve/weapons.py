from abc import ABC

weapon_types: list[str] = [
    "sword",
    "bow",
    "staff",
    "dagger",
    "mace",
    "axe",
    "spear",
    "hammer",
    "flail",
    "wand",
    "scythe",
]


class Weapon(ABC):
    def __init__(self) -> None:
        pass


class Sword(Weapon):
    def __init__(self) -> None:
        pass


class Bow(Weapon):
    def __init__(self) -> None:
        pass


class Staff(Weapon):
    def __init__(self) -> None:
        pass


class Dagger(Weapon):
    def __init__(self) -> None:
        pass


class Mace(Weapon):
    def __init__(self) -> None:
        pass


class Axe(Weapon):
    def __init__(self) -> None:
        pass


class Spear(Weapon):
    def __init__(self) -> None:
        pass


class Hammer(Weapon):
    def __init__(self) -> None:
        pass


class Flail(Weapon):
    def __init__(self) -> None:
        pass


class Wand(Weapon):
    def __init__(self) -> None:
        pass


class Scythe(Weapon):
    def __init__(self) -> None:
        pass
