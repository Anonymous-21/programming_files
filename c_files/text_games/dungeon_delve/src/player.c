#include "player.h"

void player_init(Player *player) {
  player->position.x = 0;
  player->position.y = 0;
  player->damage = 1;
  player->health = 100;
  player->gold = 0;
}

bool player_is_alive(Player *player) { return player->health > 0; }