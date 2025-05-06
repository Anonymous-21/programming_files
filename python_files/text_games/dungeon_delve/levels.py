from random import randint, choice

import tiles


class Level:
    def __init__(self, player: object) -> None:
        self.player: object = player
        self.area_level = 1

        self.map_rows: int = randint(10, 20)
        self.map_cols: int = randint(10, 20)
        self.map: list[tiles.Tile] = []

        for i in range(self.map_rows):
            for j in range(self.map_cols):
                if j == 0 and i == 0:
                    self.map.append(tiles.Start(j, i))
                else:
                    random_num: int = randint(1, 100)

                    if random_num > 95:
                        self.map.append(tiles.Treasure(j, i))
                    else:
                        random_tile: tiles.Tile = choice(
                            [tiles.Empty(j, i), tiles.Enemy(j, i), tiles.Trap(j, i)]
                        )
                        self.map.append(random_tile)

    def check_available_room(self, room_x: int, room_y: int) -> bool:
        for tile in self.map:
            if room_x == tile.x and room_y == tile.y:
                return True

        print("No room found.")

        return False

    def display_map(self) -> None:
        for i in range(self.map_rows):
            for j in range(self.map_cols):
                current_tile: tiles.Tile = self.map[i * self.map_cols + j]

                if current_tile.x == self.player.x and current_tile.y == self.player.y:
                    print("P", end=" ")
                else:
                    if isinstance(current_tile, tiles.Start):
                        print("S", end=" ")
                    elif isinstance(current_tile, tiles.Treasure):
                        print("T", end=" ")
                    else:
                        print(".", end=" ")
            print()
