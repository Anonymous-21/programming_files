#ifndef COMMANDS_H
#define COMMANDS_H

#define USER_INPUT_SIZE 50

#include "map.h"
#include "player.h"

typedef enum Commands {
  EXIT,
  HELP,
  MAP,
  POS,
  NORTH,
  SOUTH,
  EAST,
  WEST,

  INVALID_COMMAND,

} Commands;

Commands get_user_commands();
void print_available_commands();
void execute_commands(Commands current_command, Player *player, Map *map);

#endif  // COMMANDS_H