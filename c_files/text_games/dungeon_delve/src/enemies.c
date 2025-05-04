#include "enemies.h"

void enemy_init(Enemy *enemy, int level, EnemyType type) {
  enemy->type = type;
  enemy->level = level;

  if (enemy->type == ZOMBIE) {
    enemy->name = "Zombie";
    enemy->base_health = 50;
    enemy->base_damage = 5;
    enemy->health_growth_rate = 1.10f;
    enemy->damage_growth_rate = 1.05f;
  }
  if (enemy->type == GOBLIN) {
    enemy->name = "Goblin";
    enemy->base_health = 40;
    enemy->base_damage = 7;
    enemy->health_growth_rate = 1.08f;
    enemy->damage_growth_rate = 1.06f;
  }
  if (enemy->type == SKELETON) {
    enemy->name = "Skeleton";
    enemy->base_health = 45;
    enemy->base_damage = 6;
    enemy->health_growth_rate = 1.09f;
    enemy->damage_growth_rate = 1.05f;
  }
  if (enemy->type == ORC) {
    enemy->name = "Orc";
    enemy->base_health = 70;
    enemy->base_damage = 10;
    enemy->health_growth_rate = 1.12f;
    enemy->damage_growth_rate = 1.08f;
  }
  if (enemy->type == TROLL) {
    enemy->name = "Troll";
    enemy->base_health = 100;
    enemy->base_damage = 8;
    enemy->health_growth_rate = 1.15f;
    enemy->damage_growth_rate = 1.04f;
  }
  if (enemy->type == VAMPIRE) {
    enemy->name = "Vampire";
    enemy->base_health = 65;
    enemy->base_damage = 12;
    enemy->health_growth_rate = 1.10f;
    enemy->damage_growth_rate = 1.10f;
  }
  if (enemy->type == WEREWOLF) {
    enemy->name = "Werewolf";
    enemy->base_health = 80;
    enemy->base_damage = 11;
    enemy->health_growth_rate = 1.12f;
    enemy->damage_growth_rate = 1.09f;
  }
  if (enemy->type == DEMON) {
    enemy->name = "Demon";
    enemy->base_health = 90;
    enemy->base_damage = 14;
    enemy->health_growth_rate = 1.13f;
    enemy->damage_growth_rate = 1.12f;
  }
  if (enemy->type == DRAGON) {
    enemy->name = "Dragon";
    enemy->base_health = 150;
    enemy->base_damage = 20;
    enemy->health_growth_rate = 1.18f;
    enemy->damage_growth_rate = 1.15f;
  }
  if (enemy->type == BANDIT) {
    enemy->name = "Bandit";
    enemy->base_health = 55;
    enemy->base_damage = 9;
    enemy->health_growth_rate = 1.09f;
    enemy->damage_growth_rate = 1.07f;
  }
  if (enemy->type == WITCH) {
    enemy->name = "Witch";
    enemy->base_health = 60;
    enemy->base_damage = 13;
    enemy->health_growth_rate = 1.08f;
    enemy->damage_growth_rate = 1.13f;
  }
}

void enemy_is_alive(Enemy *enemy) { return enemy->base_health > 0; }
