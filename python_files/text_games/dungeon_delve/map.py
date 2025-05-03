from random import randint, choice

import room
from utils import Vector2


class Map:
    def __init__(self, rows: int, cols: int, player: object) -> None:
        self.rows: int = rows
        self.cols: int = cols
        self.map: list[room.Room] = []
        self.player: object = player

        self.gen_map()

    def gen_map(self) -> None:
        for i in range(self.rows):
            for j in range(self.cols):
                current_room: room.Room = None

                if j == 0 and i == 0:
                    current_room = room.StartingRoom(position=Vector2(j, i))
                else:
                    random_num: int = randint(1, 100)

                    if random_num > 95:
                        current_room = room.TreasureRoom(position=Vector2(j, i))
                    else:
                        room_choices: list[room.Room] = [
                            room.EmptyRoom(position=Vector2(j, i)),
                            room.EnemyRoom(position=Vector2(j, i)),
                            room.TrapRoom(position=Vector2(j, i)),
                        ]
                        current_room = choice(room_choices)

                self.map.append(current_room)

    def draw(self) -> None:
        for i in range(self.rows):
            for j in range(self.cols):
                current_room: room.Room = self.map[i * self.cols + j]

                if self.player.position.x == j and self.player.position.y == i:
                    print("P", end=" ")
                elif current_room.visited:
                    if isinstance(current_room, room.StartingRoom):
                        print("S", end=" ")
                    if isinstance(current_room, room.TreasureRoom):
                        print("T", end=" ")
                else:
                    print(".", end=" ")

            print()

    def update(self) -> None:
        # update rooms visited by player on map
        for current_room in self.map:
            if self.player.position == current_room.position:
                current_room.visited = True
