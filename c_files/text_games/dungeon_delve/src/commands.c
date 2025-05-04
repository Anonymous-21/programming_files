#include "commands.h"

#include <stdio.h>
#include <stdlib.h>

#include "utils.h"

Commands get_user_commands() {
  char *user_command = malloc(USER_INPUT_SIZE * sizeof(char));

  fgets(user_command, USER_INPUT_SIZE, stdin);
  user_command[strcspn(user_command, "\n")] = '\0';

  // lowercase user input
  for (int i = 0; i < USER_INPUT_SIZE; i++) {
    user_command[i] = tolower(user_command[i]);
  }

  // return appropriate command
  if (strncmp(user_command, "exit", USER_INPUT_SIZE) == 0 ||
      strncmp(user_command, "quit", USER_INPUT_SIZE) == 0 ||
      strncmp(user_command, "q", USER_INPUT_SIZE) == 0) {
    return EXIT;
  } else if (strncmp(user_command, "help", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "h", USER_INPUT_SIZE) == 0) {
    return HELP;
  } else if (strncmp(user_command, "map", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "m", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "show map", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "show m", USER_INPUT_SIZE) == 0) {
    return MAP;
  } else if (strncmp(user_command, "pos", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "p", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "position", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "show position", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "show p", USER_INPUT_SIZE) == 0) {
    return POS;
  } else if (strncmp(user_command, "north", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "n", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "move north", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "move n", USER_INPUT_SIZE) == 0) {
    return NORTH;
  } else if (strncmp(user_command, "south", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "s", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "move south", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "move s", USER_INPUT_SIZE) == 0) {
    return SOUTH;
  } else if (strncmp(user_command, "east", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "e", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "move east", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "move e", USER_INPUT_SIZE) == 0) {
    return EAST;
  } else if (strncmp(user_command, "west", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "w", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "move west", USER_INPUT_SIZE) == 0 ||
             strncmp(user_command, "move w", USER_INPUT_SIZE) == 0) {
    return WEST;
  } else {
    return INVALID_COMMAND;
  }

  free(user_command);
}

void print_available_commands() {
  printf("\nEXIT: 'exit', 'quit', 'q'\n");
  printf("HELP: 'help', 'h'\n");
  printf("MAP: 'map', 'm', 'show map', 'show m'\n");
  printf(
      "PLAYER POSITION: 'pos', 'p', 'position', 'show position', 'show p'\n");
  printf("MOVE NORTH: 'north', 'n', 'move north', 'move n'\n");
  printf("MOVE SOUTH: 'south', 's', 'move south', 'move s'\n");
  printf("MOVE EAST: 'east', 'e', 'move east', 'move e'\n");
  printf("MOVE WEST: 'west', 'w', 'move west', 'move w'\n\n");
}

void execute_commands(Commands current_command, Player *player, Map *map) {
  Vector2 room_position;

  switch (current_command) {
    case EXIT:
      printf("Exiting...\n");
      exit(0);
    case HELP:
      print_available_commands();
      break;
    case MAP:
      map_display(&map, player->position);
      break;
    case POS:
      printf("(%d, %d)\n", player->position.x, player->position.y);
      break;
    case NORTH:
      room_position.x = player->position.x;
      room_position.y = player->position.y - 1;
      if (map_check_available_room(&map, room_position)) {
        player_move(&player, NORTH);
      } else {
        printf("No room to the North\n");
      }
      break;
    case SOUTH:
      room_position.x = player->position.x;
      room_position.y = player->position.y + 1;
      if (map_check_available_room(&map, room_position)) {
        player_move(&player, SOUTH);
      } else {
        printf("No room to the South\n");
      }
      break;
    case EAST:
      room_position.x = player->position.x + 1;
      room_position.y = player->position.y;
      if (map_check_available_room(&map, room_position)) {
        player_move(&player, EAST);
      } else {
        printf("No room to the East\n");
      }
      break;
    case WEST:
      room_position.x = player->position.x - 1;
      room_position.y = player->position.y;
      if (map_check_available_room(&map, room_position)) {
        player_move(&player, WEST);
      } else {
        printf("No room to the West\n");
      }
      break;
    case INVALID_COMMAND:
      printf("Command not found. Type 'help' for available commands\n");
      break;
  }
}
