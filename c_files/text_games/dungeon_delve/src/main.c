#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "commands.h"
#include "map.h"
#include "player.h"

// *********************************************
// GAME ENUMS
// *********************************************

typedef enum GameState {
  TITLE_SCREEN,
  PLAYER_SELECTION,

} GameState; 

// *********************************************
// GAME MANAGER
// *********************************************

typedef struct Game {
  GameState state;
  Commands current_command;

  Map map;
  Player player;

} Game;

void print_title() {
  printf("\n*********************************\n");
  printf("          DUNGEON DELVE          \n");
  printf("*********************************\n\n");
}

void game_state_handler(Game *game) {
  if (game->state == TITLE_SCREEN) {
    print_title();
    game->state = PLAYER_SELECTION;
  }
}

void game_init(Game *game) {
  game->state = TITLE_SCREEN;
  game_state_handler(game);

  map_init(&game->map);
  player_init(&game->player, WARRIOR, game->map.list[0].position);
}

void game_update(Game *game) {
  while (1) {
    // get user commands
    printf("> ");
    game->current_command = get_user_commands();
    execute_commands(game->current_command, &game->player, &game->map);
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