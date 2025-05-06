#include "enemies.h"

void enemy_init(Enemy *enemy, int level, EnemyType type) {
  enemy->type = type;
  enemy->level = level;

  if (enemy->type == ZOMBIE) {
    enemy->base_health = 50;
    enemy->base_damage = 5;
    enemy->health_growth_rate = 1.10f;
    enemy->damage_growth_rate = 1.05f;
  }
  if (enemy->type == GOBLIN) {
    enemy->base_health = 40;
    enemy->base_damage = 7;
    enemy->health_growth_rate = 1.08f;
    enemy->damage_growth_rate = 1.06f;
  }
  if (enemy->type == SKELETON) {
    enemy->base_health = 45;
    enemy->base_damage = 6;
    enemy->health_growth_rate = 1.09f;
    enemy->damage_growth_rate = 1.05f;
  }
  if (enemy->type == ORC) {
    enemy->base_health = 70;
    enemy->base_damage = 10;
    enemy->health_growth_rate = 1.12f;
    enemy->damage_growth_rate = 1.08f;
  }
  if (enemy->type == TROLL) {
    enemy->base_health = 100;
    enemy->base_damage = 8;
    enemy->health_growth_rate = 1.15f;
    enemy->damage_growth_rate = 1.04f;
  }
  if (enemy->type == VAMPIRE) {
    enemy->base_health = 65;
    enemy->base_damage = 12;
    enemy->health_growth_rate = 1.10f;
    enemy->damage_growth_rate = 1.10f;
  }
  if (enemy->type == WEREWOLF) {
    enemy->base_health = 80;
    enemy->base_damage = 11;
    enemy->health_growth_rate = 1.12f;
    enemy->damage_growth_rate = 1.09f;
  }
  if (enemy->type == DEMON) {
    enemy->base_health = 90;
    enemy->base_damage = 14;
    enemy->health_growth_rate = 1.13f;
    enemy->damage_growth_rate = 1.12f;
  }
  if (enemy->type == DRAGON) {
    enemy->base_health = 150;
    enemy->base_damage = 20;
    enemy->health_growth_rate = 1.18f;
    enemy->damage_growth_rate = 1.15f;
  }
  if (enemy->type == BANDIT) {
    enemy->base_health = 55;
    enemy->base_damage = 9;
    enemy->health_growth_rate = 1.09f;
    enemy->damage_growth_rate = 1.07f;
  }
  if (enemy->type == WITCH) {
    enemy->base_health = 60;
    enemy->base_damage = 13;
    enemy->health_growth_rate = 1.08f;
    enemy->damage_growth_rate = 1.13f;
  }
}

bool enemy_is_alive(Enemy *enemy) { return enemy->base_health > 0; }
