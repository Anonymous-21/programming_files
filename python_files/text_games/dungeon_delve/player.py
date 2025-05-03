from utils import Vector2


class Player:
    def __init__(self) -> None:
        self.position: Vector2 = Vector2(0, 0)
        self.health: int = 100
        self.damage: int = 1
        self.gold: int = 0

    def is_alive(self) -> None:
        return self.health > 0

    def move_north(self) -> None:
        self.position.y -= 1

    def move_south(self) -> None:
        self.position.y += 1

    def move_east(self) -> None:
        self.position.x += 1

    def move_west(self) -> None:
        self.position.x -= 1
