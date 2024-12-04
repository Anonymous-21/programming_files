#ifndef ENEMY_LIST_H
#define ENEMY_LIST_H

#include "raylib.h"

typedef struct Player Player;
typedef struct Enemy Enemy;

typedef struct EnemyList
{
    Enemy *list;
    int size;
    int capacity;
    int frames_counter;
    int enemy_spawn_interval;

} EnemyList;

void initEnemyList(EnemyList *enemy_list);
void drawEnemyList(EnemyList *enemy_list);
void updateEnemyList(EnemyList *enemy_list, Player *player);

void reallocateMemoryEnemyList(EnemyList *enemy_list);
void freeMemoryEnemyList(EnemyList *enemy_list);

#endif