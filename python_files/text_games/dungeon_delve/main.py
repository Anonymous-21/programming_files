from enum import Enum
from os import system

from levels import Level
import player
from commands import CommandHandler


class GameState(Enum):
    TITLE_SCREEN = 0
    PLAYER_TYPE_SELECTION = 1
    GAME_RUN = 2


class Game:
    def __init__(self) -> None:
        system("clear")
        self.game_state = GameState.TITLE_SCREEN
        self.game_state_handler()

    def get_user_input(self) -> str:
        user_input: str = input("> ").lower().strip()

        # quit game
        if user_input in ["exit", "quit"]:
            quit()

        return user_input

    def game_state_handler(self) -> None:
        if self.game_state == GameState.TITLE_SCREEN:
            self.print_title_screen()
            self.game_state = GameState.PLAYER_TYPE_SELECTION
        if self.game_state == GameState.PLAYER_TYPE_SELECTION:
            self.player_type_selection()
            self.game_state = GameState.GAME_RUN
        if self.game_state == GameState.GAME_RUN:
            self.game_run()

    def print_title_screen(self) -> None:
        print("""
************************************************
                DUNGEON DELVE
************************************************
""")

    def player_type_selection(self) -> None:
        while True:
            for type in player.player_types:
                print(f"- {type.capitalize()}")

            print()
            user_input: str = self.get_user_input()

            if user_input == "warrior":
                temp_player = player.Warrior()
                print()
                print(f"Base Health: {temp_player.base_health}")
                print(f"Base Health: {temp_player.base_damage}")
                print()
                choice: str = input("Are you sure? ").strip().lower()
                print()
                if choice in ["yes", "y"]:
                    self.player = player.Warrior()
                    break
            elif user_input == "ranger":
                temp_player = player.Ranger()
                print()
                print(f"Base Health: {temp_player.base_health}")
                print(f"Base Health: {temp_player.base_damage}")
                print()
                choice = input("Are you sure? ").strip().lower()
                print()
                if choice in ["yes", "y"]:
                    self.player = player.Ranger()
                    break
            elif user_input == "mage":
                temp_player = player.Mage()
                print()
                print(f"Base Health: {temp_player.base_health}")
                print(f"Base Health: {temp_player.base_damage}")
                print()
                choice = input("Are you sure? ").strip().lower()
                print()
                if choice in ["yes", "y"]:
                    self.player = player.Mage()
                    break
            elif user_input == "cleric":
                temp_player = player.Cleric()
                print()
                print(f"Base Health: {temp_player.base_health}")
                print(f"Base Health: {temp_player.base_damage}")
                print()
                choice = input("Are you sure? ").strip().lower()
                print()
                if choice in ["yes", "y"]:
                    self.player = player.Cleric()
                    break
            elif user_input == "rogue":
                temp_player = player.Rogue()
                print()
                print(f"Base Health: {temp_player.base_health}")
                print(f"Base Health: {temp_player.base_damage}")
                print()
                choice = input("Are you sure? ").strip().lower()
                print()
                if choice in ["yes", "y"]:
                    self.player = player.Rogue()
                    break
            elif user_input == "paladin":
                temp_player = player.Paladin()
                print()
                print(f"Base Health: {temp_player.base_health}")
                print(f"Base Health: {temp_player.base_damage}")
                print()
                choice = input("Are you sure? ").strip().lower()
                print()
                if choice in ["yes", "y"]:
                    self.player = player.Paladin()
                    break
            elif user_input == "berserker":
                temp_player = player.Berserker()
                print()
                print(f"Base Health: {temp_player.base_health}")
                print(f"Base Health: {temp_player.base_damage}")
                print()
                choice = input("Are you sure? ").strip().lower()
                print()
                if choice in ["yes", "y"]:
                    self.player = player.Berserker()
                    break
            elif user_input == "necromancer":
                temp_player = player.Necromancer()
                print()
                print(f"Base Health: {temp_player.base_health}")
                print(f"Base Health: {temp_player.base_damage}")
                print()
                choice = input("Are you sure? ").strip().lower()
                print()
                if choice in ["yes", "y"]:
                    self.player = player.Necromancer()
                    break
            elif user_input == "druid":
                temp_player = player.Druid()
                print()
                print(f"Base Health: {temp_player.base_health}")
                print(f"Base Health: {temp_player.base_damage}")
                print()
                choice = input("Are you sure? ").strip().lower()
                print()
                if choice in ["yes", "y"]:
                    self.player = player.Druid()
                    break
            elif user_input == "monk":
                temp_player = player.Monk()
                print()
                print(f"Base Health: {temp_player.base_health}")
                print(f"Base Health: {temp_player.base_damage}")
                print()
                choice = input("Are you sure? ").strip().lower()
                print()
                if choice in ["yes", "y"]:
                    self.player = player.Monk()
                    break
            else:
                print()
                print("Invalid type. Try again")
                print()

    def game_run(self) -> None:
        self.level = Level(self.player)

        while True:
            user_input: str = self.get_user_input()
            CommandHandler(user_input, self.level, self.player)


if __name__ == "__main__":
    game = Game()
