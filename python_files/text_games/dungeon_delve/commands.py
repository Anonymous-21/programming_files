from enum import Enum


class CommandMap(Enum):
    HELP: list[str] = ["help", "h"]
    MAP: list[str] = ["map", "m"]
    POS: list[str] = ["position", "pos", "p"]
    NORTH: list[str] = ["north", "n"]
    SOUTH: list[str] = ["south", "s"]
    EAST: list[str] = ["east", "e"]
    WEST: list[str] = ["west", "w"]


class CommandHandler:
    def __init__(self, user_input: str, level: object, player: object) -> None:
        self.level: object = level
        self.player: object = player
        self.user_input: str = user_input
        self.execute_commands()

    def print_commands(self) -> None:
        print()
        for command in CommandMap:
            print(f"{command.name}: {command.value}")
        print()
        print("Type 'quit' or 'exit' to exit game")
        print()

    def execute_commands(self) -> None:
        if self.user_input in CommandMap.HELP.value:
            self.print_commands()
        elif self.user_input in CommandMap.MAP.value:
            self.level.display_map()
        elif self.user_input in CommandMap.POS.value:
            print(f"({self.player.x}, {self.player.y})")
        elif self.user_input in CommandMap.NORTH.value:
            if self.level.check_available_room(self.player.x, self.player.y - 1):
                self.player.move_north()
                self.level.display_map()
        elif self.user_input in CommandMap.SOUTH.value:
            if self.level.check_available_room(self.player.x, self.player.y + 1):
                self.player.move_south()
                self.level.display_map()
        elif self.user_input in CommandMap.EAST.value:
            if self.level.check_available_room(self.player.x + 1, self.player.y):
                self.player.move_east()
                self.level.display_map()
        elif self.user_input in CommandMap.WEST.value:
            if self.level.check_available_room(self.player.x - 1, self.player.y):
                self.player.move_west()
                self.level.display_map()
        else:
            print("Invalid command. Type 'help' for available commands")
