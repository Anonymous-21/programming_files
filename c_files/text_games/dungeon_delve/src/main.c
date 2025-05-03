#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "map.h"

#define INPUT_SIZE 20

// *********************************************
// GAME ENUMS
// *********************************************

typedef enum GameState {
  START_MENU,

} GameState;

typedef enum Commands {
  EXIT,
  HELP,
  MAP,
  NORTH,
  SOUTH,
  EAST,
  WEST,

  INVALID_COMMAND,

} Commands;

// *********************************************
// GAME MANAGER
// *********************************************

typedef struct Game {
  GameState state;
  Commands current_command;

  Map map;

} Game;

void print_start_menu() {
  printf("*********************************\n");
  printf("\tDUNGEON DELVE\n");
  printf("*********************************\n\n");
}

Commands get_user_input() {
  char *user_command = malloc(INPUT_SIZE * sizeof(char));

  fgets(user_command, INPUT_SIZE, stdin);
  user_command[strcspn(user_command, "\n")] = '\0';

  // lowercase user input
  for (int i = 0; i < INPUT_SIZE; i++) {
    user_command[i] = tolower(user_command[i]);
  }

  // return appropriate command
  if (strncmp(user_command, "exit", INPUT_SIZE) == 0 ||
      strncmp(user_command, "quit", INPUT_SIZE) == 0 ||
      strncmp(user_command, "q", INPUT_SIZE) == 0) {
    return EXIT;
  } else if (strncmp(user_command, "help", INPUT_SIZE) == 0 ||
             strncmp(user_command, "h", INPUT_SIZE) == 0) {
    return HELP;
  } else if (strncmp(user_command, "map", INPUT_SIZE) == 0 ||
             strncmp(user_command, "m", INPUT_SIZE) == 0) {
    return MAP;
  } else if (strncmp(user_command, "north", INPUT_SIZE) == 0 ||
             strncmp(user_command, "n", INPUT_SIZE) == 0) {
    return NORTH;
  } else if (strncmp(user_command, "south", INPUT_SIZE) == 0 ||
             strncmp(user_command, "s", INPUT_SIZE) == 0) {
    return SOUTH;
  } else if (strncmp(user_command, "east", INPUT_SIZE) == 0 ||
             strncmp(user_command, "e", INPUT_SIZE) == 0) {
    return EAST;
  } else if (strncmp(user_command, "west", INPUT_SIZE) == 0 ||
             strncmp(user_command, "w", INPUT_SIZE) == 0) {
    return WEST;
  } else {
    return INVALID_COMMAND;
  }

  free(user_command);
}

void print_available_commands() {
  printf("EXIT: 'exit', 'quit', 'q'\n");
  printf("HELP: 'help', 'h'\n");
  printf("MAP: 'map', 'm'\n");
  printf("NORTH: 'north', 'n'\n");
  printf("SOUTH: 'south', 's'\n");
  printf("EAST: 'east', 'e'\n");
  printf("WEST: 'west', 'w'\n");
}

void execute_commands(Game *game) {
  switch (game->current_command) {
    case EXIT:
      printf("Exiting...\n");
      exit(0);
    case HELP:
      print_available_commands();
      break;
    case MAP:
      map_draw(&game->map);
      break;
    case INVALID_COMMAND:
      printf("Command not found. Type 'help' for available commands\n");
      break;
  }
}

void game_init(Game *game) {
  map_init(&game->map);
  print_start_menu();
}

void game_update(Game *game) {
  while (1) {
    // get user commands
    printf("> ");
    game->current_command = get_user_input();
    execute_commands(game);
  }
}

// *********************************************
// MAIN
// *********************************************

int main(void) {
  Game game;

  game_init(&game);
  game_update(&game);

  return 0;
}