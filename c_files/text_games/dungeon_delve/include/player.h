#ifndef PLAYER_H
#define PLAYER_H

#include <stdbool.h>

#include "commands.h"
#include "utils.h"

typedef enum PlayerType {
  WARRIOR,
  RANGER,
  MAGE,
  CLERIC,
  ROGUE,
  PALADIN,
  BERSERKER,
  NECROMANCER,
  DRUID,
  MONK,

} PlayerType;

typedef struct Player {
  Vector2 position;
  PlayerType type;
  int level;
  int gold;
  int base_damage;
  int base_health;
  float health_growth_rate;
  float damage_growth_rate;

} Player;

void player_init(Player *player, Vector2 start_pos);
bool player_is_alive(Player *player);
void player_move(Player *player, Commands command);

#endif  // PLAYER_H