#include "collision_handler.h"
#include "enemy_list.h"
#include "player.h"
#include "bullet_list.h"
#include "enemy.h"
#include "bullet.h"

void playerCollisionEnemy(EnemyList *enemy_list, Player *player)
{
    for (int i = 0; i < enemy_list->size; i++)
    {
        if (CheckCollisionRecs((Rectangle){player->x,
                                           player->y,
                                           player->width,
                                           player->health},
                               (Rectangle){enemy_list->list[i].x,
                                           enemy_list->list[i].y,
                                           enemy_list->list[i].width,
                                           enemy_list->list[i].height}))
        {
            player->health -= enemy_list->list[i].damage;
        }
    }
}