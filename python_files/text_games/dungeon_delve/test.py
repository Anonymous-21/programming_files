from enum import Enum


class Commands(Enum):
    EXIT: tuple[str] = ("exit", "quit", "q")
    MAP: tuple[str] = ("map", "m")
    HELP: tuple[str] = ("help", "h")
    NORTH: tuple[str] = ("north", "n")
    SOUTH: tuple[str] = ("south", "s")
    EAST: tuple[str] = ("east", "e")
    WEST: tuple[str] = ("west", "w")


for command in Commands:
    print(command.value)
