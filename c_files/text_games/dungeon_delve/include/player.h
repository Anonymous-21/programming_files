#ifndef PLAYER_H
#define PLAYER_H

#include <stdbool.h>
#include "utils.h"

typedef struct Player {
  Vector2 position;
  int health;
  int damage;
  int gold;

} Player;

void player_init(Player *player);
bool player_is_alive(Player *player);

#endif  // PLAYER_H