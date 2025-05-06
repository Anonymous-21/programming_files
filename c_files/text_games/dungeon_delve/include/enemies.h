#ifndef ENEMIES_H
#define ENEMIES_H

#include <stdbool.h>

#define NAME_SIZE 20

typedef enum {
  ZOMBIE,
  GOBLIN,
  SKELETON,
  ORC,
  TROLL,
  VAMPIRE,
  WEREWOLF,
  DEMON,
  DRAGON,
  BANDIT,
  WITCH,

} EnemyType;

typedef struct Enemy {
  int level;
  EnemyType type;
  char name[NAME_SIZE];
  int base_damage;
  int base_health;
  float health_growth_rate; // per level multiplier
  float damage_growth_rate; // per level multiplier

} Enemy;

void enemy_init(Enemy *enemy, int level, EnemyType type);
bool enemy_is_alive(Enemy *enemy);

#endif  // ENEMIES_H;