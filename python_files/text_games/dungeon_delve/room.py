from abc import ABC

from utils import Vector2


class Room(ABC):
    def __init__(self, position: Vector2) -> None:
        self.position: Vector2 = position
        self.visited: bool = False


class StartingRoom(Room):
    def __init__(self, position) -> None:
        super().__init__(position)

        self.name: str = "Starting Room"
        self.description: str = "Player starts here"


class EnemyRoom(Room):
    def __init__(self, position) -> None:
        super().__init__(position)

        self.name: str = "Enemy Room"
        self.description: str = "Enemy spawn here"


class TreasureRoom(Room):
    def __init__(self, position) -> None:
        super().__init__(position)

        self.name: str = "Treasure Room"
        self.description: str = "Treasure spawn here"

class TrapRoom(Room):
    def __init__(self, position) -> None:
        super().__init__(position)

        self.name: str = "Trap Room"
        self.description: str = "Traps spawn here"


class EmptyRoom(Room):
    def __init__(self, position) -> None:
        super().__init__(position)

        self.name: str = "Empty Room"
        self.description: str = "Empty room"

