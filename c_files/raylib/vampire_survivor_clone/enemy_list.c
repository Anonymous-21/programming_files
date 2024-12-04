#include "raylib.h"
#include <stdio.h>
#include <stdlib.h>

#include "enemy.h"
#include "enemy_list.h"
#include "player.h"

void initEnemyList(EnemyList *enemy_list)
{
    enemy_list->capacity = 10;
    enemy_list->size = 0;
    enemy_list->list = (Enemy *)malloc(enemy_list->capacity * sizeof(Enemy));
    if (enemy_list->list == NULL)
    {
        printf("Enemy list memory not allocated\n");
        exit(1);
    }
    enemy_list->frames_counter = 0;
    enemy_list->enemy_spawn_interval = 20;
}

void drawEnemyList(EnemyList *enemy_list)
{
    for (int i = 0; i < enemy_list->size; i++)
    {
        drawEnemy(&enemy_list->list[i]);
    }
}

void updateEnemyList(EnemyList *enemy_list, Player *player)
{
    reallocateMemoryEnemyList(enemy_list);

    enemy_list->frames_counter++;
    if (enemy_list->frames_counter > enemy_list->enemy_spawn_interval)
    {
        enemy_list->frames_counter = 0;

        Enemy enemy;
        initEnemy(&enemy, player);

        if (enemy_list->list != NULL)
        {
            enemy_list->size++;
            enemy_list->list[enemy_list->size - 1] = enemy;
        }
    }

    for (int i = enemy_list->size - 1; i >= 0; i--)
    {
        updateEnemy(&enemy_list->list[i], player);
    }
}

void reallocateMemoryEnemyList(EnemyList *enemy_list)
{
    if (enemy_list->size >= enemy_list->capacity)
    {
        enemy_list->capacity += 10;
        Enemy *new_list = (Enemy *)realloc(enemy_list->list, enemy_list->capacity * sizeof(Enemy));
        if (new_list == NULL)
        {
            printf("Enemy list memory not allocated\n");
            exit(1);
        }

        enemy_list->list = new_list;
    }
}

void freeMemoryEnemyList(EnemyList *enemy_list)
{
    free(enemy_list->list);
    enemy_list->list = NULL;
}