import traceback
from enum import Enum

from map import Map
from player import Player

ROWS: int = 50
COLS: int = 50


class Commands(Enum):
    EXIT = ("exit", "quit", "q")
    MAP = ("map", "m")
    HELP = ("help", "h")
    NORTH = ("north", "n")
    SOUTH = ("south", "s")
    EAST = ("east", "e")
    WEST = ("west", "w")


def start_menu() -> None:
    print()
    print("Dungeon Delve")
    print()


class GameManager:
    def __init__(self) -> None:
        self.player: Player = Player()
        self.map: Map = Map(ROWS, COLS, self.player)

        start_menu()

    def print_commands(self) -> None:
        print("Exit: exit, quit, q")
        print("Help: help, h")
        print("Map: map, m")
        print("North: north, n")
        print("South: north, n")
        print("East: north, n")
        print("West: north, n")

    def execute_command(self, command: str) -> None:
        if "map" in command:
            self.map.draw()
        if "help" in command:
            self.print_commands()
        if "exit" in command:
            print("Exiting...")
            quit()

    def update(self) -> None:
        while True:
            # update map
            self.map.update()

            try:
                choice: str = input("> ").strip().lower()
                mapped_command: tuple = ()

                for command in Commands:
                    if choice in command.value:
                        mapped_command = command.value

                if mapped_command:
                    self.execute_command(mapped_command)
                else:
                    print("Command not recognized. Type 'help' for available commands")

            except Exception:
                # printing detailed traceback
                print("Detailed Error Location: ")
                traceback.print_exc()


if __name__ == "__main__":
    game_manager: GameManager = GameManager()
    game_manager.update()
