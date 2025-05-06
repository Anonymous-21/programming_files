#include "player.h"

#include "commands.h"

void player_init(Player *player, PlayerType type, Vector2 start_pos) {
  player->position.x = start_pos.x;
  player->position.y = start_pos.y;
  player->type = type;
  player->level = 1;
  player->gold = 0;

  if (player->type == WARRIOR) {
    player->base_health = 90;
    player->base_damage = 8;
    player->health_growth_rate = 1.12f;
    player->damage_growth_rate = 1.06f;
  }
  if (player->type == RANGER) {
    player->base_health = 60;
    player->base_damage = 11;
    player->health_growth_rate = 1.08f;
    player->damage_growth_rate = 1.12f;
  }
  if (player->type == MAGE) {
    player->base_health = 50;
    player->base_damage = 14;
    player->health_growth_rate = 1.05f;
    player->damage_growth_rate = 1.15f;
  }
  if (player->type == CLERIC) {
    player->base_health = 65;
    player->base_damage = 6;
    player->health_growth_rate = 1.10f;
    player->damage_growth_rate = 1.04f;
  }
  if (player->type == ROGUE) {
    player->base_health = 55;
    player->base_damage = 13;
    player->health_growth_rate = 1.07f;
    player->damage_growth_rate = 1.14f;
  }
  if (player->type == PALADIN) {
    player->base_health = 80;
    player->base_damage = 9;
    player->health_growth_rate = 1.11f;
    player->damage_growth_rate = 1.08f;
  }
  if (player->type == BERSERKER) {
    player->base_health = 70;
    player->base_damage = 12;
    player->health_growth_rate = 1.10f;
    player->damage_growth_rate = 1.13f;
  }
  if (player->type == NECROMANCER) {
    player->base_health = 50;
    player->base_damage = 10;
    player->health_growth_rate = 1.06f;
    player->damage_growth_rate = 1.10f;
  }
  if (player->type == DRUID) {
    player->base_health = 65;
    player->base_damage = 9;
    player->health_growth_rate = 1.10f;
    player->damage_growth_rate = 1.09f;
  }
  if (player->type == MONK) {
    player->base_health = 60;
    player->base_damage = 10;
    player->health_growth_rate = 1.09f;
    player->damage_growth_rate = 1.10f;
  }
}

bool player_is_alive(Player *player) { return player->base_health > 0; }

void player_move(Player *player, Commands command) {
  if (command == NORTH) {
    player->position.y -= 1;
  } else if (command == SOUTH) {
    player->position.y += 1;
  } else if (command == EAST) {
    player->position.x += 1;
  } else if (command == WEST) {
    player->position.x -= 1;
  }
}