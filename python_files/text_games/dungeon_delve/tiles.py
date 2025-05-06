from abc import ABC


class Tile(ABC):
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y


class Empty(Tile):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)


class Start(Tile):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)


class Enemy(Tile):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)


class Treasure(Tile):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)


class Trap(Tile):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
