#include "raylib.h"
#include <math.h>
#include <stdlib.h>

#include "enemy.h"
#include "player.h"

#define MIN_DISTANCE 400 // minimum enemy spawn distance from player

void initEnemy(Enemy *enemy, Player *player)
{
    Vector2 enemy_pos = genEnemySpawnCoordinates(player);
    enemy->x = enemy_pos.x;
    enemy->y = enemy_pos.y;
    enemy->width = 30;
    enemy->height = 30;
    enemy->initial_color = GREEN;
    enemy->color = enemy->initial_color;
    enemy->speed = 2;
    enemy->damage = 1;
    enemy->health = 10;
}

Vector2 genEnemySpawnCoordinates(Player *player)
{
    double angle = (rand() / (double)RAND_MAX) * (PI * 2);
    double distance = ((rand() / (double)RAND_MAX) * 100) + MIN_DISTANCE;
    double spawn_x = player->x + distance * cos(angle);
    double spawn_y = player->y + distance * sin(angle);

    return (Vector2){spawn_x, spawn_y};
}

void drawEnemy(Enemy *enemy)
{
    DrawRectangleRec((Rectangle){enemy->x,
                                 enemy->y,
                                 enemy->width,
                                 enemy->height},
                     enemy->color);
}

void updateEnemy(Enemy *enemy, Player *player)
{
    double distance_x = player->x - enemy->x;
    double distance_y = player->y - enemy->y;
    double distance = sqrt(pow(distance_x, 2) + pow(distance_y, 2));

    if (distance > 0)
    {
        distance_x /= distance;
        distance_y /= distance;

        enemy->x += distance_x * enemy->speed;
        enemy->y += distance_y * enemy->speed;
    }
}